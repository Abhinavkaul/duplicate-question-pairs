import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1=pd.read_csv('train.csv')
new_df=df1.sample(35000)
print(new_df.shape)

print(new_df.isnull().sum())

new_df.dropna(inplace=True)
print(new_df.isnull().sum())

#distribution of duplicate and non duplicate questions
print('count:-')
print(new_df['is_duplicate'].value_counts())
print()
print("percentage:-")
print((new_df['is_duplicate'].value_counts()/new_df['is_duplicate'].count())*100)
new_df['is_duplicate'].value_counts().plot(kind='bar')

#repeated questions

qid=pd.Series(new_df['qid1'].tolist() + new_df['qid2'].tolist())
print('number of unique questions is :-',np.unique(qid).shape[0])
x=qid.value_counts()>1
print('number of questions getting repeated :-',x[x].shape[0])

#repeated questions histogram

plt.hist(qid.value_counts().values,bins=160)
plt.yscale('log')
plt.show()