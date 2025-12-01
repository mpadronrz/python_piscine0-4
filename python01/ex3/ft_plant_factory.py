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


class Factory:
    """
    A factory that creates and stores Plant objects.
    """
    def __init__(self) -> None:
        """
        Initialize the factory with an empty list of plants.
        """
        self.plants = []

    def add_plants(self, plant_info: list[tuple[str, int, int]]) -> None:
        """
        Create Plant instances from a list of plant data and store them.

        Args:
            plant_info (list[tuple[str, int, int]]):
                A list of tuples, each containing:
                - name (str): Plant name.
                - height (int): Plant height in centimeters.
                - days (int): Plant age in days.
        """
        total_plants = 0
        print("=== Plant Factory Output ===")
        for name, height, days in plant_info:
            plant = Plant(name, height, days)
            self.plants.append(plant)
            total_plants += 1
            print(f"Created: {name} ({height}cm, {days} days)")
        print(f"\nTotal plants created: {total_plants}")


def main() -> None:
    """
    Run the plant factory program by creating sample plant data
    and passing it to the Factory for processing.
    """
    plant_info = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    fact = Factory()
    fact.add_plants(plant_info)


if __name__ == "__main__":
    main()
