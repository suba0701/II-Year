class Dog:
    def __init__(self, name: str):
        self.name = name

    def bark(self):
        print(f"{self.name} says: Woof!")

# Example
d = Dog("Rex")
d.bark()
