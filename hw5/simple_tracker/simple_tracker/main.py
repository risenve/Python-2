import time
from tracker import Tracker
import os


config_path = os.path.join(os.path.dirname(__file__), "../config/config.txt")
interval = 2

try:
    with open(config_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("interval="):
                interval = float(line.split("=")[1])
except FileNotFoundError:
    print(f"Config file not found at {config_path}, using default interval={interval}")

tracker = Tracker()
data_file = os.path.join(os.path.dirname(__file__), "../data.txt")
while True:
    tracker.increment()
    print(tracker)  
    tracker.save_to_file(path=data_file) 
    time.sleep(interval)
