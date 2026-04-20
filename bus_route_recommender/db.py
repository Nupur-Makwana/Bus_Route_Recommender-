# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:25:15 2026

@author: nupur
"""

import pandas as pd
import mysql.connector

df = pd.read_csv("routes.csv")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="010906",
    database="bus_routes"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO routes VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()