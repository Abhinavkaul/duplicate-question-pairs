import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from fuzzy_features import fuzz
class Token:
    def fetch_token_features(self,row):
        
        q1 = row['question1']
        q2 = row['question2']
        
        SAFE_DIV = 0.0001 

        STOP_WORDS = stopwords.words("english")
        
        token_features = [0.0]*8
        
        # Converting the Sentence into Tokens: 
        q1_tokens = q1.split()
        q2_tokens = q2.split()
        
        if len(q1_tokens) == 0 or len(q2_tokens) == 0:
            return token_features

        # Get the non-stopwords in Questions
        q1_words = set([word for word in q1_tokens if word not in STOP_WORDS])
        q2_words = set([word for word in q2_tokens if word not in STOP_WORDS])
        
        #Get the stopwords in Questions
        q1_stops = set([word for word in q1_tokens if word in STOP_WORDS])
        q2_stops = set([word for word in q2_tokens if word in STOP_WORDS])
        
        # Get the common non-stopwords from Question pair
        common_word_count = len(q1_words.intersection(q2_words))
        
        # Get the common stopwords from Question pair
        common_stop_count = len(q1_stops.intersection(q2_stops))
        
        # Get the common Tokens from Question pair
        common_token_count = len(set(q1_tokens).intersection(set(q2_tokens)))
        
        
        token_features[0] = common_word_count / (min(len(q1_words), len(q2_words)) + SAFE_DIV)
        token_features[1] = common_word_count / (max(len(q1_words), len(q2_words)) + SAFE_DIV)
        token_features[2] = common_stop_count / (min(len(q1_stops), len(q2_stops)) + SAFE_DIV)
        token_features[3] = common_stop_count / (max(len(q1_stops), len(q2_stops)) + SAFE_DIV)
        token_features[4] = common_token_count / (min(len(q1_tokens), len(q2_tokens)) + SAFE_DIV)
        token_features[5] = common_token_count / (max(len(q1_tokens), len(q2_tokens)) + SAFE_DIV)
        
        # Last word of both question is same or not
        token_features[6] = int(q1_tokens[-1] == q2_tokens[-1])
        
        # First word of both question is same or not
        token_features[7] = int(q1_tokens[0] == q2_tokens[0])
        
        return token_features
    
    def fetch_length_features(self,row):
        
        q1 = row['question1']
        q2 = row['question2']
        
        length_features = [0.0]*2
        
        # Converting the Sentence into Tokens: 
        q1_tokens = q1.split()
        q2_tokens = q2.split()
        
        if len(q1_tokens) == 0 or len(q2_tokens) == 0:
            return length_features
        
        # Absolute length features
        length_features[0] = abs(len(q1_tokens) - len(q2_tokens))
        
        #Average Token Length of both Questions
        length_features[1] = (len(q1_tokens) + len(q2_tokens))/2
        
        return length_features
    
    

t=Token()    
def token(new_df):
    token_features = new_df.apply(t.fetch_token_features, axis=1)

    new_df["cwc_min"]       = list(map(lambda x: x[0], token_features))
    new_df["cwc_max"]       = list(map(lambda x: x[1], token_features))
    new_df["csc_min"]       = list(map(lambda x: x[2], token_features))
    new_df["csc_max"]       = list(map(lambda x: x[3], token_features))
    new_df["ctc_min"]       = list(map(lambda x: x[4], token_features))
    new_df["ctc_max"]       = list(map(lambda x: x[5], token_features))
    new_df["last_word_eq"]  = list(map(lambda x: x[6], token_features))
    new_df["first_word_eq"] = list(map(lambda x: x[7], token_features))
    
    
    length_features = new_df.apply(t.fetch_length_features, axis=1)

    new_df['abs_len_diff'] = list(map(lambda x: x[0], length_features))
    new_df['mean_len'] = list(map(lambda x: x[1], length_features))
    
    new_df=fuzz(new_df)
    return new_df