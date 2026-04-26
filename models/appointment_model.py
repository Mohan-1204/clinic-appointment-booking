from config.db import get_connection

def book_appointment(name, age, email, treatment, doctor, time):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO appointments (patient_name, age, email, treatment, doctor, time)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (name, age, email, treatment, doctor, time))
    conn.commit()
    conn.close()

