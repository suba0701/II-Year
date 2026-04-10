class Fan:
    def __init__(self, speed="Medium"):
        self.speed = speed

    def status(self):
        print(f"Fan speed: {self.speed}")

# Example usage
if __name__ == "__main__":
    f = Fan()         # default speed "Medium"
    f.status()        # Fan speed: Medium

    f2 = Fan("High")  # custom speed
    f2.status()       # Fan speed: High

