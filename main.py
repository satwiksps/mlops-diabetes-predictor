from fastapi import FastAPI
from app.schema import DiabetesInput
from app.model import load_model, predict_diabetes

app = FastAPI()
model = load_model()

@app.get("/")
def read_root():
    return {"message": "Diabetes Prediction API is running"}

@app.post("/predict")
def predict(input_data: DiabetesInput):
    prediction = predict_diabetes(model, input_data)
    return {"diabetic": prediction}
