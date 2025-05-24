import pandas as pd
from datetime import datetime
import random

# Simulate sensor data
def generate_sensor_data(num_entries=10):
    data = {
        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(num_entries)],
        "Camera_Input": [random.choice(['clear', 'obstacle', 'turn']) for _ in range(num_entries)],
        "LiDAR_Distance_m": [round(random.uniform(0.5, 10.0), 2) for _ in range(num_entries)],
        "Ultrasonic_cm": [round(random.uniform(10, 100), 1) for _ in range(num_entries)],
    }
    return pd.DataFrame(data)

# Simulate robotic task execution log
def generate_robotic_log(num_tasks=5):
    tasks = {
        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(num_tasks)],
        "Task": [random.choice(['pick', 'place', 'idle']) for _ in range(num_tasks)],
        "Status": [random.choice(['completed', 'pending', 'error']) for _ in range(num_tasks)],
    }
    return pd.DataFrame(tasks)

# Simulate secure communication log
def generate_comm_log(num_entries=10):
    logs = {
        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(num_entries)],
        "Data_Type": [random.choice(['sensor', 'command', 'status']) for _ in range(num_entries)],
        "Encrypted": [random.choice([True, False]) for _ in range(num_entries)],
        "Protocol": [random.choice(['MQTT', 'HTTP', 'TLS']) for _ in range(num_entries)]
    }
    return pd.DataFrame(logs)

# Simulate test feedback log
def generate_test_log(num_cases=5):
    feedback = {
        "
