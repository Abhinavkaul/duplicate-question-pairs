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
        return result
                
        
q1=input("enter question1 : ")
q2=input("enter question2 : ")
final_df=dataframe(q1,q2)
result=predictor(final_df)
if result==[1]:
        print("DUPLICATE")
else:
        print("NOT DUPLICATE")