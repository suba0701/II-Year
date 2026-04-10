class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        """Initialize a Rectangle with length and width."""
        self.length = float(length)
        self.width = float(width)

    def area(self) -> float:
        """Return the area of the rectangle (length × width)."""
        return self.length * self.width


def main() -> None:
    r = Rectangle(5, 3)
    print("Area:", r.area())  # Area: 15.0

    # More examples
    r2 = Rectangle(7.5, 2)
    print("Area:", r2.area())  # Area: 15.0


if __name__ == "__main__":
    main()
