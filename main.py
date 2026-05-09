import streamlit as st
from models.doctor_model import get_doctors_by_treatment
from models.appointment_model import book_appointment
from email_service import send_email
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Clinic App", layout="wide")
st.title("🏥 Clinic Appointment Booking System")

# Inputs
name = st.text_input("Patient Name",key="name")
age = st.number_input("Age", min_value=1,key="age")
email = st.text_input("Email",key="email")

# Treatment
treatment = st.selectbox("Select Treatment", ["Dental", "Cardiology", "General"])

# Doctors
doctors_data = get_doctors_by_treatment(treatment)
doctor_names = [doc[0] for doc in doctors_data]

selected_doctor = st.selectbox("Select Doctor", doctor_names)

# Time
doctor_time = ""
for doc in doctors_data:
    if doc[0] == selected_doctor:
        doctor_time = doc[1]

time_slots = doctor_time.split(",")
selected_time = st.selectbox("Available Time", time_slots)

# Button

if st.button("Book Appointment"):

    # Save appointment
    book_appointment(
        name,
        age,
        email,
        treatment,
        selected_doctor,
        selected_time
    )

    # Send email
    success = send_email(
        email,
        name,
        age,
        selected_doctor,
        selected_time,
        treatment
    )

    # Message
    if success:
        st.success("Appointment booked and email sent successfully ✅")
    else:
        st.warning("Appointment booked but email not sent ❌")