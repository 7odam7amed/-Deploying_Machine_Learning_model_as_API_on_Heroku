from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class model_input(BaseModel):

    Pragnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int

diabetes_model = pickle.load(open('diabetes.sav', 'rb'))

@app.post('/diabetes_prediction')
def diabetes_prediction(input_parameters : model_input):

    input_dictionary = input_parameters.dict()

    preg = input_dictionary['Pragnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

    prediction = diabetes_prediction.predict([input_list])

    if(prediction[0] == 0):
        return 'This person is not diabetic'
    else:
        return 'This person is diabetic'
    
