# -*- coding: utf-8 -*-
"""

@author: nupur
"""

import pandas as pd
from sklearn.neighbors import NearestNeighbors

def create_dataset():
    """
    Creates a sample bus route dataset.
    Features:
    - Distance (km)
    - Travel Time (minutes)
    - Popularity (1-100 scale)
    """
    data = {
        "Route": ["R1", "R2", "R3", "R4", "R5"],
        "Distance_km": [10, 7, 15, 5, 12],
        "TravelTime_min": [25, 20, 35, 18, 30],
        "Popularity": [80, 65, 90, 70, 85],
    }

    df = pd.DataFrame(data).set_index("Route")
    return df


def train_model(df):
    """
    Trains KNN model using Euclidean distance.
    """
    model = NearestNeighbors(metric="euclidean", n_neighbors=2)
    model.fit(df)
    return model


def recommend_route(model, df):
    """
    Takes user input and recommends closest matching route.
    """
    print("\nEnter your preferred route details:")

    distance = float(input("Preferred Distance (km): "))
    time = float(input("Preferred Travel Time (minutes): "))
    popularity = float(input("Preferred Popularity (1-100): "))

    user_preference = [[distance, time, popularity]]

    distances, indices = model.kneighbors(user_preference)

    print("\nRecommended Bus Route(s):")
    for index in indices[0]:
        print(f"- {df.index[index]}")


def main():
    print("=== Bus Route Recommendation System (KNN) ===")

    df = create_dataset()
    print("\nAvailable Bus Routes:")
    print(df)

    model = train_model(df)
    recommend_route(model, df)


if __name__ == "__main__":
    main()


