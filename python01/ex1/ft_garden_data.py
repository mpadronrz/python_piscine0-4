#!/usr/bin/env python3

class Plant:
    """
    Represents a plant with a name, height, and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new Plant instance.

        Args:
            name (str): The plant's name.
            height (int): Height of the plant in centimeters.
            age (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """
        Displays plant information in an organized way
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.get_info()
    plant2.get_info()
    plant3.get_info()
