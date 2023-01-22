import pandas as pd
from preprocessing import preprocess
import os
from pathlib import Path
import pickle


main= Path(__file__).parent.parent
model_path =os.path.join(main,"models","model.pkl")
with open(model_path,"rb") as f:
        model=pickle.load(f)

def dataframe(q1,q2):
        data = { 'question1':  [q1],'question2': [q2] }
        new_df1 = pd.DataFrame(data)    
        final_df=preprocess(new_df1)
        return final_df

def predictor(final_df):
        arr = final_df.to_numpy()
        result=model.predict(arr)
        if result==[1]:
                return "DUPLICATE"
        else:
                return "NOT DUPLICATE"


def test_sample1():
        q1="Which one dissolve in water quikly sugar, salt, methane and carbon di oxide?"
        q2="Which fish would survive in salt water?"
        final_df=dataframe(q1,q2)
        result=predictor(final_df)
        assert result == "NOT DUPLICATE" , "Should be 'not equal'"
        
def test_sample2():
        q1="Does a black hole have mass?"
        q2="Does a black hole have a finite mass?"
        final_df=dataframe(q1,q2)
        result=predictor(final_df)
        assert result == "DUPLICATE" , "Should be 'equal'"
        
def test_sample3():
        q1="How do I use Twitter as a business source?"
        q2="How do I use Twitter as a business source?"
        final_df=dataframe(q1,q2)
        result=predictor(final_df)
        assert result == "DUPLICATE" , "Should be 'equal'"
        
def test_sample4():
        q1="Which are the prospering towns in Kerala?"
        q2="Why are there so many Christians in Kerala?"
        final_df=dataframe(q1,q2)
        result=predictor(final_df)
        assert result == "NOT DUPLICATE" , "Should be 'not equal'"
        
def test_sample5():
        q1="What would happen if you cover one of your eyes with an eye patch for one year, then take the patch off?"
        q2="What happens if eye medicine enters the eye?"
        final_df=dataframe(q1,q2)
        result=predictor(final_df)
        assert result == "NOT DUPLICATE" , "Should be not equal"
        