from transformers import pipeline

model = pipeline(model="seara/rubert-tiny2-russian-sentiment")
model("Привет, ты мне нравишься!")