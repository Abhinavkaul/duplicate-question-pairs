import fuzzywuzzy.fuzz as fuzzy
class Fuzzy:
    def fetch_fuzzy_features(self,row):
        
        q1 = row['question1']
        q2 = row['question2']
        
        fuzzy_features = [0.0]*4
        
        # fuzz_ratio
        fuzzy_features[0] = fuzzy.QRatio(q1, q2)

        # fuzz_partial_ratio
        fuzzy_features[1] = fuzzy.partial_ratio(q1, q2)

        # token_sort_ratio
        fuzzy_features[2] = fuzzy.token_sort_ratio(q1, q2)

        # token_set_ratio
        fuzzy_features[3] = fuzzy.token_set_ratio(q1, q2)

        return fuzzy_features
    
f=Fuzzy()    
def fuzz(new_df):
    fuzzy_features = new_df.apply(f.fetch_fuzzy_features, axis=1)

    # Creating new feature columns for fuzzy features
    new_df['fuzz_ratio'] = list(map(lambda x: x[0], fuzzy_features))
    new_df['fuzz_partial_ratio'] = list(map(lambda x: x[1], fuzzy_features))
    new_df['token_sort_ratio'] = list(map(lambda x: x[2], fuzzy_features))
    new_df['token_set_ratio'] = list(map(lambda x: x[3], fuzzy_features))
    
    return new_df