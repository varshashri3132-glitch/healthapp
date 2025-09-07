import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyBUGM6jtNuRVUUCjX9XkwDXj4Y1DcL-bFU")
model=genai.GenerativeModel(model_name="gemini-2.5-flash-lite")

st.title("This is my BMI calculator")
st.write("Hello everyone")
name=st.text_input("Enter your name")
height=st.number_input("Enter your height in cms")
weight=st.number_input("Enter your weight in kgs")
age=st.number_input("Enter your age")
gender=st.radio("Pick gender:",["Male","Female","Third Gender"])

st.write(f"Your name is {name}, {age} year old {gender}. Your height is {height} cms and Your weight is {weight} kgs")


if st.button("Calculate BMI"):
   bmi = round(weight/(height/100)**2,2)
   st.write(f"Your BMI is {bmi}")
   prompt=f"Act like nutritional expect and comment on the BMI with the following data: Height is {height} cms, weight is {weight}, age {age}, gender {gender}        and bmi is {bmi} "
   response=model.generate_content(prompt)
   st.markdown(response.text)
  