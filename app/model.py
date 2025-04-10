import joblib
import numpy as np
from app.schema import DiabetesInput

def load_model(model_path: str = "diabetes_model.pkl"):
    """
    Loads the trained model from disk.
    """
    try:
        model = joblib.load(model_path)
        print("Model loaded successfully")
        return model
    except FileNotFoundError:
        raise RuntimeError("Model file not found. Please train the model first.")

def predict_diabetes(model, data: DiabetesInput) -> bool:
    """
    Uses the model to predict whether a person is diabetic.
    """
    features = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure, data.BMI, data.Age]])
    prediction = model.predict(features)[0]
    return bool(prediction)
