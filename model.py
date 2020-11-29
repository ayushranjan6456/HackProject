# Importing the libraries
import pandas as pd
import numpy as np
import pickle
import sklearn
import joblib

# Importing the dataset
df = pd.read_csv("heart.csv")

# Dependent and independent variable
X = df.iloc[:,:-1]
y = df.iloc[:, 13]

#one hot encoding
ohe = pd.get_dummies(X['cp'])
X = pd.concat([X,ohe],axis=1)
X = X.drop(['cp'],axis=1)
X = X.drop([3],axis=1)
X = X.rename(columns={1:'cp1',0:'cp0',2:'cp2'})

ohe = pd.get_dummies(X['slope'])
X = pd.concat([X,ohe],axis=1)
X = X.drop(['slope'],axis=1)
X = X.drop([2],axis=1)
X = X.rename(columns={1:'slope1',0:'slope0'})

ohe = pd.get_dummies(X['ca'])
X = pd.concat([X,ohe],axis=1)
X = X.drop(['ca'],axis=1)
X = X.drop([4],axis=1)
X = X.rename(columns={1:'ca1',0:'ca0',2:'ca2',3:'ca3'})

ohe = pd.get_dummies(X['thal'])
X = pd.concat([X,ohe],axis=1)
X = X.drop(['thal'],axis=1)
X = X.drop([3],axis=1)
X = X.rename(columns={1:'thal1',0:'thal0',2:'thal2'})


# Linear Regression
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

acc = (cm[0][0]+cm[1][1])/(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1])
print(acc)

pickle.dump(classifier, open('model.pkl', 'wb'))
