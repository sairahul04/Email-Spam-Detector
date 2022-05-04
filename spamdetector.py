import pickle
import streamlit as st
from win32com.client import Dispatch


def speak(text):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(text)


model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))

def main():
    st.title("Email Spam Classifier Website")
    st.subheader("Build with Streamlit and Python")
    # st.subheader("Artificial Intelligence Group Project")
   
    msg=st.text_input("Enter the text:")
    if st.button("Predict"):
        data=[msg]
        vect=cv.transform(data).toarray()
        prediction=model.predict(vect)
        result=prediction[0]
        if result==1:
            st.error("This is a spam mail!!")
            speak("This is a spam mail!!")
        else:
            st.success("This is not a spam mail!!!")
            speak("This is not a spam mail!!!")

main()