import pandas as pd
from preprocessing import df
df1=pd.read_csv('train.csv')
new_df=df1.sample(35000)
new_df=df(new_df)
column_names = list(new_df.columns)
print(column_names)
print(len(column_names))