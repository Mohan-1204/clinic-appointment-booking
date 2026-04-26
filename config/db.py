import mysql.connector
import os
from urllib.parse import urlparse

def get_connection():
    url = os.getenv("DATABASE_URL")   # 👈 இத தான் use பண்ணணும்

    if not url:
        raise Exception("DATABASE_URL not found")

    parsed = urlparse(url)

    return mysql.connector.connect(
        host="shortline.proxy.rlwy.net",
        user="root",
        password="GmvCVUvwWfzuUTDuQpSFEtAngAUnrmla",
        database="railway",
        port=57116
    )