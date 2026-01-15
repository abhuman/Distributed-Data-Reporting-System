import time
from data_ingestion import ingest_data
from fault_tolerance import retry

@retry(retries=3)
def process_batch(batch_id):
    print(f"Processing batch {batch_id}")
    ingest_data()
    time.sleep(0.5)

def simulate_distributed_processing(total_batches=10):
    for batch in range(total_batches):
        process_batch(batch)
