# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:06:14 2026

@author: nupur
"""
import streamlit as st
import pandas as pd
import os
import joblib

# Load model + data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
df = pd.read_csv(os.path.join(BASE_DIR, "routes.csv"))

st.title("🚌 Bus Route Recommendation System")

# INPUTS
source = st.text_input("📍 Source")
destination = st.text_input("🎯 Destination")

distance = st.number_input("Distance (km)", 1, 50, 10)
time = st.number_input("Time (min)", 5, 120, 30)
popularity = st.slider("Popularity", 0, 100, 70)

# BUTTON
if st.button("Find Best Route"):

    if source == "" or destination == "":
        st.error("Please enter source and destination")

    else:
        #  STEP 1: FILTER DATA
        filtered_df = df[
            (df["source_stop"].str.lower() == source.lower()) &
            (df["destination_stop"].str.lower() == destination.lower())
        ]

        #  No route found
        if filtered_df.empty:
            st.error("No route found for this path")

        else:
            #  STEP 2: APPLY ML
            X = filtered_df[['distance_km','travel_time_min','popularity','stops_count']]

            filtered_df["score"] = model.predict(X)

            #  STEP 3: BEST ROUTE
            best = filtered_df.sort_values("score").iloc[0]

            #  STEP 4: ALTERNATIVES
            alternatives = (
                filtered_df
                .sort_values("score")
                .head(3)["route_id"]
                .tolist()
            )

            # OUTPUT
            st.success("Best Route Found 🚍")

            st.write("Route:", best["route_id"])
            st.write("From:", source)
            st.write("To:", destination)
            st.write("ETA:", best["travel_time_min"], "min")

            st.write("Alternatives:")
            st.write(alternatives)
