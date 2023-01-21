import pandas as pd
from preprocessing import preprocess
import os
from pathlib import Path
import pickle


main= Path(__file__).parent.parent
model_path =os.path.join(main,"models","model.pkl")
with open(model_path,"rb") as f:
        model=pickle.load(f)
        
q1=input()
q2=input()
data = {'question1':  [q1],
        'question2': [q2]
        }
new_df1 = pd.DataFrame(data)    
final_df=preprocess(new_df1)

#column_names = list(final_df.columns)
#print("length=",len(column_names))

arr = final_df.to_numpy()
result=model.predict(arr)
if result==[1]:
        print("DUPLICATE")
else:
        print("NOT DUPLICATE")