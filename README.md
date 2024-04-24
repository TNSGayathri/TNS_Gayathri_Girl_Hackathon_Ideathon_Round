**Problem Statement**:In today’s health care system, individuals often struggle to find relavant treatments to their symptoms and preferences.Due to the number of health care providers, individuals may often confuse for the best health care provider for their symptoms. Additionally, individuals can prioritize features such as doctor numbers and appointments, which are not always readily available.

**Medical Assistant**: Develop a healthcare recommendation system that analyzes user symptoms leveraging symptom data (using mock data), healthcare provider databases, and user ratings,  recommends doctors with matching specialties and aligned schedules

**Solution** :To solve these challenges, I an creating a healthcare recommendation system.This system analyze user symptoms using synthetic data to recommend doctors with relavant specialities and timing availability.Ultimately,this system aims to improve health care system ,customized medical care,and provides decision making for individuals .

**Predicting symptoms using AI Model** :

For the doctor recommendation system, I opted machine learning technology to train a machine learning model that predicts the symptoms of a patient and, based on those symptoms,it predicts the type of the disease. Once we get to know the disease, we can map the patients with the doctors based on their availability. For this, I used a sample dataset that has list of patients, their symptoms,the type of disease, and then I performed a couple of preprocessing steps to make sure that  the data was clean and ready to be processed. Eventually I used some ML algorithms like Random Forest, Naive Bayes, and Logistic Regression.The reason behind using the above ML algorithms is that, they give 100 percent accuracy.

**Random Forest**: Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and takes the average to improve the predictive accuracy of that dataset.

**Naive Bayes**: The Naive Bayes Classifier is one of the most simple and effective classification algorithms, which helps in building fast machine learning models that can make quick predictions.

**Logistic regression**:Logistic regression is a supervised machine learning algorithm that accomplishes binary classification tasks by predicting the probability of an outcome, event, or observation.

**Setup of local Environment**

1.Fork this repo.

2.Run the command git clone.

https://github.com/TNSGayathri/TNS_Gayathri_Girl_Hackathon_Ideathon_Round.git.

3.All the data used for training and testing the models (diseaseprediction) is in the folder temporary.

4.First install the python packages with the version >3.7.

5.Also install the Pandas,Flask,Pickle,Sklearn with the command pip install "package name".

6.Run the app.py in visual studio.

7.Click on the link http://127.0.0.1:5000 shown in terminal.

8.Click on choose file button and choose the prediction.csv file from temporary folder.

9.Click on the predict button, where it gives information about the doctor's ID relative to symptoms.

**Demo**
