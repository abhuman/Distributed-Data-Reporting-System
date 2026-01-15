import random
from db import get_connection

def ingest_data(batch_size=500):
    conn = get_connection()
    cur = conn.cursor()

    for _ in range(batch_size):
        cur.execute(
            """
            INSERT INTO raw_data (source, metric_name, metric_value)
            VALUES (%s, %s, %s)
            """,
            ("sensor", "cpu_usage", random.uniform(10, 90))
        )

    conn.commit()
    cur.close()
    conn.close()
