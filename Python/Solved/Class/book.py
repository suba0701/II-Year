from typing import Optional

class Book:
    def __init__(self, title: str, author: str, year: Optional[int] = None) -> None:
        """
        Initialize a Book.

        :param title: Title of the book
        :param author: Author of the book
        :param year: (optional) publication year
        """
        self.title = title
        self.author = author
        self.year = year

    def display(self) -> None:
        """Print the book's title and author (and year if provided)."""
        if self.year is not None:
            print(f"Title: {self.title} | Author: {self.author} | Year: {self.year}")
        else:
            print(f"Title: {self.title} | Author: {self.author}")

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year!r})"


def main() -> None:
    # Examples
    b1 = Book("1984", "George Orwell", 1949)
    b2 = Book("The Little Prince", "Antoine de Saint-Exupéry")

    b1.display()   # Title: 1984 | Author: George Orwell | Year: 1949
    b2.display()   # Title: The Little Prince | Author: Antoine de Saint-Exupéry

    # You can also inspect the object
    print(repr(b1))


if __name__ == "__main__":
    main()
