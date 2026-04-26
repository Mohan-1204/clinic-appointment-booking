import streamlit as st
import pandas as pd
from config.db import get_connection

st.title("View Appointments")
st.subheader("📋 Appointment List")

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM appointments")
data = cursor.fetchall()

# column names (order must match DB)
columns = ["ID", "Name", "Age", "Email", "Treatment", "Doctor", "Time"]

df = pd.DataFrame(data, columns=columns)

st.dataframe(df)   # 🔥 nice table UI