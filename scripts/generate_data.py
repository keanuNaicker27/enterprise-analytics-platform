import json
import random
import uuid
from datetime import datetime, timedelta

def generate_sample_data(count=100):
    event_types = ["page_view", "login", "add_to_cart", "purchase", "logout", "search"]
    sources = ["web-front", "ios-app", "android-app"]
    user_ids = [f"u-{random.randint(100, 999)}" for _ in range(20)] # 20 unique users
    
    records = []
    start_time = datetime.now()

    for i in range(count):
        # Create a realistic timeline
        timestamp = (start_time + timedelta(minutes=i*random.randint(1, 10))).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        event = {
            "event_id": str(uuid.uuid4())[:8],
            "timestamp": timestamp,
            "user_id": random.choice(user_ids),
            "event_type": random.choice(event_types),
            "context": {
                "source": random.choice(sources),
                "ip": f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}",
                "session_duration": random.randint(10, 3600)
            }
        }
        records.append(event)
    
    # Save as JSON Lines (Standard for BigQuery/Glue)
    with open('datasets/sample-data.json', 'w') as f:
        for record in records:
            f.write(json.dumps(record) + '\n')

if __name__ == "__main__":
    generate_sample_data(100)
    print("Successfully generated 100 records in datasets/sample-data.json")
