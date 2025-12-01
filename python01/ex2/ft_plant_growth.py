#!/usr/bin/env python3

class Plant:
    """
    Represents a plant with a name, height, and age.
    """
    def __init__(self, name: str, height: int, days: int) -> None:
        """
        Initialize a new Plant instance.

        Args:
            name (str): The plant's name.
            height (int): Height of the plant in centimeters.
            days (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.days = days

    def get_info(self) -> None:
        """
        Displays plant information in an organized way
        """
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self) -> None:
        """
        Increase the plant's height by 1 cm.
        """
        self.height += 1

    def age(self) -> None:
        """
        Increase the plant's age by 1 day.
        """
        self.days += 1


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    day = 1
    while day < 8:
        print(f"=== Day {day} ===")
        plant1.get_info()
        plant1.grow()
        plant1.age()
        day += 1
    print(f"Growth this week: +{day - 2}cm")
