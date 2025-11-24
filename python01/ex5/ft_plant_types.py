#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.age = days


class Flower(Plant):
    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, days: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, shade: int) -> None:
        print(f"{self.name} provides {shade} square meters of shade")

    def show(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, days: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} if rich in {self.nutritional_value}")


def main():
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
