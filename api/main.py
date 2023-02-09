from fastapi import FastAPI

import pandas as pd

import numpy as np


app = FastAPI()


@app.get("/")

def home():

    return {
        "message": "NeuralRetail API Running"
    }


@app.get("/health")

def health():

    return {
        "status": "healthy"
    }


@app.get("/predict/demand")

def predict_demand():

    predicted_sales = np.random.randint(
        1000,
        5000
    )

    return {

        "predicted_sales": int(predicted_sales)

    }


@app.get("/predict/churn")

def predict_churn():

    churn_probability = round(
        np.random.uniform(0,1),
        2
    )

    return {

        "churn_probability": churn_probability

    }