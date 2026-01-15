from db import get_connection

def generate_report():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO aggregated_reports (metric_name, avg_value, max_value, min_value)
        SELECT metric_name,
               AVG(metric_value),
               MAX(metric_value),
               MIN(metric_value)
        FROM raw_data
        GROUP BY metric_name;
    """)

    conn.commit()
    cur.close()
    conn.close()
