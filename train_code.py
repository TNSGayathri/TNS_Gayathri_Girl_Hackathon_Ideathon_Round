import pandas as pd
dataset = pd.read_csv('medicaldata.csv')


print(dataset.head())
print(dataset.shape)
print(dataset.columns)
print(dataset.describe())


dataset["ALLSymptoms"] = 0

for i in range(len(dataset)):
    row = dataset.iloc[i].values.tolist()
    
    if 0 in row:
        dataset["ALLSymptoms"][i] = row[1:row.index(0)]
        
    else:
        dataset["ALLSymptoms"][i] = row[1:]
        
print(dataset.head())

columns =dataset[['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4',
       'Symptom_5', 'Symptom_6', 'Symptom_7', 'Symptom_8', 'Symptom_9',
       'Symptom_10', 'Symptom_11', 'Symptom_12', 'Symptom_13', 'Symptom_14',
       'Symptom_15', 'Symptom_16', 'Symptom_17']].values.ravel()

symps = pd.unique(columns).tolist()
symps = [i for i in symps if str(i) != "nan"]

newdata=pd.DataFrame(columns = symps ,index = dataset.index)

newdata["Symptoms"] = dataset["ALLSymptoms"]



for i in symps:
    newdata[i] = newdata.apply(lambda x:1 if i in x.Symptoms else 0, axis=1)



newdata["Disease"] = dataset["Disease"]
newdata = newdata.drop(["Symptoms"],axis=1)

newdata.head()



x=newdata.iloc[:,:-1].values
y=newdata.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain , ytest = train_test_split(x ,y, random_state = 8,test_size=0.2)



from sklearn.linear_model import LogisticRegression
modelLR=LogisticRegression(max_iter = 1000)
modelLR.fit(xtrain,ytrain)

ypredLR=modelLR.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypredLR)*100)




from sklearn.naive_bayes import GaussianNB
modelnb=GaussianNB()
modelnb.fit(xtrain,ytrain)

yprednb=modelnb.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,yprednb)*100)




from sklearn.ensemble import RandomForestClassifier
modelrf=RandomForestClassifier()
modelrf.fit(xtrain,ytrain)

ypredrf=modelrf.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypredrf)*100)


import pickle

# Saving the models
with open('model.pkl', 'wb') as f:
    pickle.dump(modelnb, f)



print(modelnb.predict([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

testing=pd.read_csv('prediction.csv')
c=testing.values
print(modelnb.predict(c))