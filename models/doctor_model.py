from config.db import get_connection

def get_doctors_by_treatment(treatment):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT name, available_time FROM doctors WHERE specialization=%s"
    cursor.execute(query, (treatment,))

    results = cursor.fetchall()
    conn.close()
    return results