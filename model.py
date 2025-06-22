# model.py
from sklearn.ensemble import IsolationForest
import pandas as pd

def train_isolation_forest(data, contamination):
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(data)
    return model

def predict_anomalies(model, data):
    preds = model.predict(data)
    result = data.copy()
    result['anomaly'] = ['Anomaly' if p == -1 else 'Normal' for p in preds]
    return result
