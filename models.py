from db import get_connection

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_data (
        id SERIAL PRIMARY KEY,
        source VARCHAR(50),
        metric_name VARCHAR(100),
        metric_value FLOAT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE INDEX IF NOT EXISTS idx_metric_name ON raw_data(metric_name);
    CREATE INDEX IF NOT EXISTS idx_created_at ON raw_data(created_at);
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS aggregated_reports (
        id SERIAL PRIMARY KEY,
        metric_name VARCHAR(100),
        avg_value FLOAT,
        max_value FLOAT,
        min_value FLOAT,
        generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    cur.close()
    conn.close()
