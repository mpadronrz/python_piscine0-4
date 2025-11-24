#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


class Factory:
    def __init__(self) -> None:
        self.plants = []

    def add_plants(self, plant_info: list[tuple[str, int, int]]) -> None:
        total_plants = 0
        print("=== Plant Factory Output ===")
        for name, height, days in plant_info:
            plant = Plant(name, height, days)
            self.plants.append(plant)
            total_plants += 1
            print(f"Created: {name} ({height}cm, {days} days)")
        print(f"\nTotal plants created: {total_plants}")


def main() -> None:
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
