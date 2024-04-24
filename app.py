from flask import *
import pickle
import pandas as pd
import os

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

data = pd.read_csv('Doctor.csv')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    file=request.files['file']
    folder_path = "temporary"
    file_path = os.path.join(folder_path, file.filename)
    file.save(file_path) 
    testing=pd.read_csv(file_path)
    c=testing.values
    k = model.predict(c)
    res=[]
    for i in k:
        result = data[data['Disease'] ==i]
        result = str(result)
        res.append(result)
    d=res[0].split(' ')
    return render_template('index.html',ans=k[0],res=d[-1])

app.run(debug=True)