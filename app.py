import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("Rock_Mine_Prediction.pkl","rb"))

st.title("Rock vs Mine Prediction using Sonar Data")

st.write("Enter 60 sonar values to predict object")

# input values
input_data = [] #list

for i in range(60):
    value = st.number_input(f"Sonar Value {i+1}", step=0.01)# + 0.01 increase
    input_data.append(value)

if st.button("Predict"):

    input_array = np.array(input_data).reshape(1,-1)

    prediction = model.predict(input_array)

    if prediction[0] == "R":
        st.success("Result: Rock")
    else:
        st.error("Result: Mine")