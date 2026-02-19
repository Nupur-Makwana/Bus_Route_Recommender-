# -*- coding: utf-8 -*-
"""

@author: nupur
"""

import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Create dataset
data = {
    "Route": ["R1", "R2", "R3", "R4", "R5"],
    "Distance_km": [10, 7, 15, 5, 12],
    "TravelTime_min": [25, 20, 35, 18, 30],
    "Popularity": [80, 65, 90, 70, 85],
}

df = pd.DataFrame(data).set_index("Route")

# Train model
model = NearestNeighbors(metric="euclidean", n_neighbors=1)
model.fit(df)

st.title("Bus Route Recommendation System")

st.write("Enter your preferred route details:")

distance = st.number_input("Preferred Distance (km)", min_value=0.0)
time = st.number_input("Preferred Travel Time (minutes)", min_value=0.0)
popularity = st.number_input("Preferred Popularity (1-100)", min_value=0.0, max_value=100.0)

if st.button("Recommend Route"):
    user_input = [[distance, time, popularity]]
    distances, indices = model.kneighbors(user_input)
    recommended_route = df.index[indices[0][0]]
    st.success(f"Recommended Route: {recommended_route}")
