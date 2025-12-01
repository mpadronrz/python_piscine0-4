#!/usr/bin/env python3

class Plant:
    """
    Represents a generic plant with a name, height, and age.
    """
    def __init__(self, name: str, height: int, days: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): The plant's name.
            height (int): Height of the plant in centimeters.
            days (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = days


class Flower(Plant):
    """
    Represents a flower plant with an additional color attribute.
    """
    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        """
        Initialize a Flower instance.

        Args:
            name (str): The flower's name.
            height (int): Height in centimeters.
            days (int): Age in days.
            color (str): The flower's color.
        """
        super().__init__(name, height, days)
        self.color = color

    def bloom(self) -> None:
        """
        Display a message indicating that the flower is blooming.
        """
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        """
        Displays flower information in an organized way
        """
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")


class Tree(Plant):
    """
    Represents a tree with an additional trunk diameter attribute.
    """
    def __init__(self, name: str, height: int, days: int,
                 trunk_diameter: int) -> None:
        """
        Initialize a Tree instance.

        Args:
            name (str): The tree's name.
            height (int): Height in centimeters.
            days (int): Age in days.
            trunk_diameter (int): Diameter of the tree trunk in centimeters.
        """
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, shade: int) -> None:
        """
        Display how much shade the tree provides.

        Args:
            shade (int): Shade area in square meters.
        """
        print(f"{self.name} provides {shade} square meters of shade")

    def show(self) -> None:
        """
        Displays tree information in an organized way
        """
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represents a vegetable plant with seasonal and nutritional attributes.
    """
    def __init__(self, name: str, height: int, days: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Initialize a Vegetable instance.

        Args:
            name (str): The vegetable's name.
            height (int): Height in centimeters.
            days (int): Age in days.
            harvest_season (str): When the vegetable is harvested.
            nutritional_value (str): Key nutritional characteristic.
        """
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        """
        Displays vegetable information in an organized way
        """
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} if rich in {self.nutritional_value}")


def main() -> None:
    """
    Demonstrate the different types of plants and their methods-
    """
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    rose.show()
    rose.bloom()
    print()
    oak = Tree("Oak", 500, 1825, 50)
    oak.show()
    oak.produce_shade(78)
    print()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    tomato.show()


if __name__ == "__main__":
    main()
