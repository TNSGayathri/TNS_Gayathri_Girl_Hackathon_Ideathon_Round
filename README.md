**Problem Statement**:In today’s health care system, individuals often struggle to find relavant treatments to their symptoms and preferences.Due to the number of health care providers, individuals may often confuse for the best health care provider for their symptoms. Additionally, individuals can prioritize features such as doctor numbers and appointments, which are not always readily available.

**Medical Assistant**: Develop a healthcare recommendation system that analyzes user symptoms leveraging symptom data (using mock data), healthcare provider databases, and user ratings,  recommends doctors with matching specialties and aligned schedules

**Solution** :To solve these challenges, I an creating a healthcare recommendation system.This system analyze user symptoms using synthetic data to recommend doctors with relavant specialities and timing availability.Ultimately,this system aims to improve health care system ,customized medical care,and provides decision making for individuals .

**Symptoms predict AI Model** :

For the doctor recommendation system, I opted for machine learning technology to train a machine learning model that takes the symptoms of a patient and, based on those symptoms, predicts the type of disease. Once we are able to know the disease, we can map patients with the doctors based on their availability. For this, I used a sample dataset that consisted of patient symptoms and the type of disease, and then I performed a couple of preprocessing steps to make sure the data was clean and ready to be processed. Then I used some ML algorithms like RandomForest, Naive Bayes, and logistic regression, all of which give 100 percent accuracy, so we can proceed with any of these 3 models.

**Random Forest**: Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and takes the average to improve the predictive accuracy of that dataset.

**Naive Bayes**: The Naive Bayes Classifier is one of the most simple and effective classification algorithms, which helps in building fast machine learning models that can make quick predictions.

**Logistic regression**:Logistic regression is a supervised machine learning algorithm that accomplishes binary classification tasks by predicting the probability of an outcome, event, or observation.

**Setup of local Environment**

