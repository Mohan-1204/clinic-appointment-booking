import os
import smtplib
from email.mime.text import MIMEText

def send_email(receiver_email, name, age, selected_doctor, doctor_time, treatment):

    sender_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    print("Sender:", sender_email)
    print("Receiver:", receiver_email)

    body = f"""
Hello {name},

Your appointment is confirmed.

Doctor: {selected_doctor}
Time: {doctor_time}
Treatment: {treatment}
"""

    msg = MIMEText(body)
    msg['Subject'] = "Appointment Confirmation"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()

        server.starttls()
        server.ehlo()

        server.login(sender_email, password)

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        print("EMAIL SENT SUCCESSFULLY")
        return True

    except Exception as e:
        print(f"EMAIL ERROR:{e}")
        print(e)
        return False