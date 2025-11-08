import time
from simple_tracker.tracker import Tracker

def read_config(path="../config/config.txt"):
    cfg = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                cfg[k.strip()] = v.strip()
    return cfg

def main():
    cfg = read_config()
    interval = int(cfg.get("interval", 2))
    tracker = Tracker()

    while True:
        tracker.increment()
        print(tracker)        
        tracker.save_to_file(path="data.txt")  
        time.sleep(interval)
