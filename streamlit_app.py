import streamlit as st
from transformers import pipeline
model = pipeline(model="seara/rubert-tiny2-russian-sentiment")
model("Привет, ты мне нравишься!")
st.text("Привет, ты мне нравишься!")
