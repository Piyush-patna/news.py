import streamlit as st
import pickle
import spacy
!python -m spacy download en_core_web_sm
with open('data.pkl', 'rb') as model_file:
    model= pickle.load(model_file)

nlp= spacy.load('en_core_web_lg')
st.title("News Detection App")
st.write("This app dtects whether news is real or fake")

a= st.text_input('Enter News')

doc= nlp(a)
vector= doc.vector
prediction= model.predict([vector])
if prediction[0]== 1:
    st.write('Fake news')
else:
    st.write('Real News')
