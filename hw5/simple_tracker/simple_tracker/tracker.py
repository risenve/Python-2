class Tracker:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def save_to_file(self, path="data.txt"):
        with open(path, "w") as f:
            f.write(str(self.count))

    def __str__(self):
        return f"current count: {self.count}"
    
    def reset(self):
        self.count = 0
