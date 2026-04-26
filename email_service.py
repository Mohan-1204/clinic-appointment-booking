import smtplib
from email.mime.text import MIMEText

def send_email(receiver_email, name, age, selected_doctor, doctor_time, treatment):

    sender_email = "mohanyt54353@gmail.com"
    password = "glrtxmpvflmmxtvv"  # ⚠️ replace

    body = f"""
Hello {name},

# Your Age: {age}

Your appointment is confirmed with.

Doctor: {selected_doctor}
Time: {doctor_time}
Treatment: {treatment}

Thank you!
"""

    msg = MIMEText(body)
    msg['Subject'] = "Appointment Confirmation"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()