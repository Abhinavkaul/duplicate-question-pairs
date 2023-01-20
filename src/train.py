import pandas as pd
from preprocessing import preprocess
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df1=pd.read_csv('train.csv')
new_df=df1.sample(35000)
final_df=preprocess(new_df)
column_names = list(final_df.columns)
print(len(column_names))


X_train,X_test,y_train,y_test = train_test_split(final_df.iloc[:,1:].values,final_df.iloc[:,0].values,test_size=0.2,random_state=1)

rf = RandomForestClassifier()
rf.fit(X_train,y_train)
y_pred = rf.predict(X_test)
score=accuracy_score(y_test,y_pred)
print(score)