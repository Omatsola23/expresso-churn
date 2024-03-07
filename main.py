#Import neccessary package
import pypickle as py
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np
#Add title and header to the app display
st.title("EXPRESSO CHURN")
st.header("Predict if your client will return")
#Load model from collab
model=py.load("lg.pkl")
#Give variable names to each input
user_input1=st.number_input('How frequent does the client recharge ')
user_input2=st.text_input('What pack does the client do ')
user_input3=st.number_input('How frequent is the top pack used ')
user_input4=st.number_input('How active is the client within 9o days ')
#Calling out encoder for string input
label_encoder = LabelEncoder()
predictions1= label_encoder.fit_transform([user_input2])
predictionx=[[user_input1,predictions1[0],user_input3,user_input4]]
#Calling out the model for output
predictx = model.predict(predictionx)
#Output based on prediction
if st.button('PREDICT'):
  if predictx==1:
    st.write("Customer will not return")
  else:
    st.write("Customer will return")