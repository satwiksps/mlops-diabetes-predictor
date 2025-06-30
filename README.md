# MLOps Diabetes Predictor

An end-to-end MLOps project that trains and deploys a machine learning model to predict diabetes based on patient health data. Built with **FastAPI**, **Docker**, and **Kubernetes**, this project demonstrates a real-world ML pipeline from training to deployment.

---

## Tech Stack

- **Machine Learning:** `scikit-learn`, `pandas`, `joblib`
- **API Framework:** `FastAPI`
- **Containerization:** `Docker`
- **Deployment:** `Kubernetes`
- **Dataset:** Pima Indians Diabetes Dataset

---

## Problem Statement

Predict whether a patient is diabetic based on:

- Pregnancies
- Glucose
- Blood Pressure
- BMI
- Age

---

## Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/mlops-diabetes-predictor.git
cd mlops-diabetes-predictor
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3️⃣  Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Train the Model
```bash
python train.py
```
This will download the dataset, train a Random Forest model, and save it as `diabetes_model.pkl`

### 5️⃣ Run the FastAPI App Locally
```bash
uvicorn main:app --reload
```
