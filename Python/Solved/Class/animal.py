class Animal:
    def speak(self):
        """Default speak behavior for generic animals."""
        print("...")  # or raise NotImplementedError()

class Bird(Animal):
    def speak(self):
        """Bird-specific speak override."""
        print("Tweet")

# Example usage
if __name__ == "__main__":
    a = Animal()
    a.speak()   # prints "..."

    b = Bird()
    b.speak()   # prints "Tweet"

