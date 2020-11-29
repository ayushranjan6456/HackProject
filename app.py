from flask import Flask, render_template, url_for, request
import numpy as np
import sklearn
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    print("index Started")
    return render_template('index.html')
    
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    gender = int_features[0]
    age = int_features[1]
    blood_pressure = int_features[2]
    chol = int_features[3]
    fbs = int_features[4]
    restecg = int_features[5]
    heart_beat = int_features[5]
    induced_angina = int_features[6]
    oldpeak = int_features[7]
    if(int_features[8] == 0):
        cp0 = 1
        cp1 = 0
        cp2 = 0
    if(int_features[8] == 1):
        cp0 = 0
        cp1 = 1
        cp2 = 0
    if(int_features[8] == 2):
        cp0 = 0
        cp1 = 0
        cp2 = 1
    if(int_features[8] == 3):
        cp0 = 0
        cp1 = 0
        cp2 = 0

    if(int_features[9] == 0):
        slope0 = 1
        slope1 = 0
    if(int_features[9] == 1):
        slope0 = 0
        slope1 = 1
    if(int_features[9] == 2):
        slope0 = 0
        slope1 = 0

    if(int_features[10] == 0):
        ca0 = 1
        ca1 = 0
        ca2 = 0
        ca3 = 0
    if(int_features[10] == 1):
        ca0 = 0
        ca1 = 1
        ca2 = 0
        ca3 = 0
    if(int_features[10] == 2):
        ca0 = 0
        ca1 = 0
        ca2 = 1
        ca3 = 0
    if(int_features[10] == 3):
        ca0 = 0
        ca1 = 0
        ca2 = 0
        ca3 = 1
    if(int_features[11] == 0):
        thal1=1
        thal2=0 
        thal3=0   
    if(int_features[11] == 1):
        thal1=0
        thal2=1
        thal3=0
    if(int_features[11] == 2):
        thal1=0
        thal2=0
        thal3=1
    if(int_features[11] == 3):
        thal1=0
        thal2=0
        thal3=0
    
    cp_text=""
    if(cp0==1):
        cp_text="No Chest Pain"
    if(cp1==1):
        cp_text="Chest Pain Probably becuase of indigestion, reflux or muscle strain"
    if(cp2==1):
        cp_text="Inflammation in the rib joints near the breastbone and shingles"

    bp_text=""
    if(blood_pressure<90):
        bp_text="Low blood pressure, Some medicines can cause low blood pressure as a side effect. It can also be caused by a number of underlying conditions, including heart failure and dehydration."
    if(blood_pressure>90 and blood_pressure<120):
        bp_text="Blood Pressure is Normal"
    if(blood_pressure>120 and blood_pressure<140):
        bp_text="Blood Pressure Higher than normal unhealthy badits such as junk food etc should be stopped"    
    if(blood_pressure>140):
        bp_text="High blood pressure, unhealthy lifestyle habits, such as smoking, drinking too much alcohol, being overweight and not exercising enough."

    sugar_text="Sugar is normal"
    if(fbs==1):
        sugar_text="skipped or forgot your insulin, have an infection, are ill, are under stress, not exercising"



    true_features = [age, gender, blood_pressure, chol, fbs, restecg, heart_beat, induced_angina, oldpeak, cp0, cp1, cp2, slope0, slope1, ca0, ca1, ca2, ca3, thal1, thal2,thal3]

    final_features = [np.array(true_features)]
    print(int_features)
    print(true_features)
    print(final_features)
    prediction = model.predict(final_features)
    if prediction[0] == 1:
        output = "Congratulations You don't have any disease."
    else:
        output = "Consult the doctor about your health."
    return render_template('result.html', prediction_text='{}'.format(output),cp_text='{}'.format(cp_text), bp_text='{}'.format(bp_text), sugar_text='{}'.format(sugar_text))

if __name__ == "__main__":
    app.run(debug=True)
