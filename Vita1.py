# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:12:12 2023

@author: Admin
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
diabetes_model = pickle.load(open('C:/Users/Gaurav/OneDrive/Desktop/Vitapredict/Saved models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Gaurav/OneDrive/Desktop/Vitapredict/Saved models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/Gaurav/OneDrive/Desktop/Vitapredict/Saved models/parkinsons_model.sav', 'rb'))


# Sidebar for navigation with enhanced design
st.sidebar.title("Vitapredict ML Models")
st.sidebar.write("Select a prediction model:")

# Updated navigation using option_menu
selected = option_menu(
    None,
    ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
    icons=['activity', 'heart', 'person'],
    default_index=0,
    orientation='vertical',
    styles={
        "container": {
            "padding": "0px", 
            "background-color": "#f8f9fa", 
            "border-radius": "10px",  # Adding rounded corners for the sidebar
        },
        "nav-link": {
            "font-size": "16px", 
            "text-align": "left", 
            "margin": "5px", 
            "--hover-color": "#e0e0e0", 
            "padding": "10px",  # Padding to make it more clickable
            "border-radius": "5px",  # Rounded borders for navigation items
        },
        "nav-link-selected": {
            "background-color": "#1f77b4", 
            "color": "white", 
            "font-weight": "bold",  # Highlight the selected item
        },
        "icon": {
            "font-size": "18px",  # Increase icon size for better visibility
            "color": "#007bff",  # Blue color for icons
        },
    }
)

# Code for prediction pages remains the same

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
            Glucose = st.text_input('Glucose Level')
            BloodPressure = st.text_input('Blood Pressure value')
            SkinThickness = st.text_input('Skin Thickness value')
        with col2:
            Insulin = st.text_input('Insulin Level')
            BMI = st.text_input('BMI value')
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
            Age = st.text_input('Age of the Person')

        diab_diagnosis = ''
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            diab_diagnosis = 'The person is Diabetic' if diab_prediction[0] == 1 else 'The person is Not Diabetic'
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input('Age of the Person')
            sex = st.number_input('Sex of the Person')
            cp = st.number_input('Chest pain types')
            trestbps = st.number_input('Resting Blood Pressure')
            chol = st.number_input('Serum Cholestoral in mg/dl')
            fbs = st.number_input('Fasting blood sugar > 120 mg/dl')
        with col2:
            restecg = st.number_input('Resting Electrocardiographic results')
            thalach = st.number_input('Maximum Heart Rate achieved')
            exang = st.number_input('Exercise Induced Angina')
            oldpeak = st.number_input('ST depression induced by exercise')
            slope = st.number_input('Slope of the peak exercise ST segment')
            ca = st.number_input('Major vessels colored by flourosopy')
            thal = st.number_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

        heart_diagnosis = ''
        if st.button('Heart Test Result'):
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            heart_diagnosis = 'The person is suffering from Heart disease' if heart_prediction[0] == 1 else 'The person is Not suffering from Heart disease'
        st.success(heart_diagnosis)

# Parkinsons Prediction Page
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')
            fhi = st.text_input('MDVP:Fhi(Hz)')
            flo = st.text_input('MDVP:Flo(Hz)')
            Jitter_percent = st.text_input('MDVP:Jitter(%)')
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
            RAP = st.text_input('MDVP:RAP')
            PPQ = st.text_input('MDVP:PPQ')
            DDP = st.text_input('Jitter:DDP')
        with col2:
            Shimmer = st.text_input('MDVP:Shimmer')
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
            APQ3 = st.text_input('Shimmer:APQ3')
            APQ5 = st.text_input('Shimmer:APQ5')
            APQ = st.text_input('MDVP:APQ')
            DDA = st.text_input('Shimmer:DDA')
            NHR = st.text_input('NHR')
            HNR = st.text_input('HNR')
            RPDE = st.text_input('RPDE')
            DFA = st.text_input('DFA')
            spread1 = st.text_input('spread1')
            spread2 = st.text_input('spread2')
            D2 = st.text_input('D2')
            PPE = st.text_input('PPE')

        parkinsons_diagnosis = ''
        if st.button('Parkinsons Test Result'):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            parkinsons_diagnosis = 'The person is suffering from Parkinsons disease' if parkinsons_prediction[0] == 1 else 'The person is Not suffering from Parkinsons disease'
        st.success(parkinsons_diagnosis)
