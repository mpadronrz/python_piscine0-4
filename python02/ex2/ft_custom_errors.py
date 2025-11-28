#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant: str):
        super().__init__(f"The {plant} plant is wilting!")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


class Plant:
    def __init__(self, name: str, water: int = 1) -> None:
        self.name = name
        self.water_amount = water

    def water(self):
        self.water_amount += 1
        if self.water_amount > 2:
            raise PlantError(self.name)


class Garden:
    def __init__(self, name: str, plants=None, water: int = 0):
        self.name = name
        self.plants = plants if plants is not None else []
        self.water = water

    def add_plants(self, plants: list[Plant]):
        for p in plants:
            self.plants += [p,]
            print(f"Added {p.name} to {self.name}'s garden")

    def water_plant(self, plant: Plant):
        if self.water < 1:
            raise WaterError()
        self.water -= 1
        plant.water()

    def fill_tank(self, amount: int = 1):
        self.water += amount


def test_garden_errors():
    print("=== Custom Garden Errors Demo ===")
    garden = Garden("my_garden", [Plant("tomato", 2),
                                  Plant("rose", 1)], 1)
    print("\nTesting PlantError...")
    try:
        garden.water_plant(garden.plants[0])
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print("\nTesting WaterError...")
    try:
        garden.water_plant(garden.plants[1])
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    garden.fill_tank()
    print("\nTesting catching all garden errors...")
    try:
        garden.water_plant(garden.plants[0])
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    try:
        garden.water_plant(garden.plants[1])
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_garden_errors()
