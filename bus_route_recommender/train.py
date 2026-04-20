# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:25:03 2026

@author: nupur
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("routes.csv")

# simple rule-based label (best = 1, good = 2, avg = 3)
df["score"] = (
    df["popularity"] * 0.4 +
    (1 / df["travel_time_min"]) * 100 +
    (1 / df["distance_km"]) * 50
)

df["label"] = pd.qcut(df["score"], 3, labels=[1,2,3])

X = df[['distance_km','travel_time_min','popularity','stops_count']]
y = df['label']

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("Model saved")