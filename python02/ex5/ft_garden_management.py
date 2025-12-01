#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        if name is None or name == "":
            raise ValueError("Plant name cannot be empty!")
        self.name = name
        self.water_amount = water
        self.sun = sun

    def water(self):
        self.water_amount += 1
        print(f"Watering {self.name} - success")

    def check_health(self):
        if self.water_amount < 1:
            raise ValueError(f"Water level {self.water_amount} "
                             "is too low (min 1)")
        if self.water_amount > 10:
            raise ValueError(f"Water level {self.water_amount} "
                             "is too high (max 10)")
        if self.sun < 2:
            raise ValueError(f"Sunlight hours {self.sun} is too low (min 2)")
        if self.sun > 12:
            raise ValueError(f"Sunlight hours {self.sun} is too high (max 12)")
        print(f"{self.name}: healthy (water: "
              f"{self.water_amount}, sun: {self.sun})")


class GardenManager:
    def __init__(self, name: str, plants=None, water: int = 0):
        self.name = name
        self.plants = plants if plants is not None else []
        self.water = water

    def add_plants(self, plants: list[tuple[str, int, int]]):
        try:
            for data in plants:
                plant = Plant(data[0], data[1], data[2])
                self.plants += [plant,]
                print(f"Added {plant.name} succesfully")
        except ValueError as error:
            print(f"Error adding plant: {error}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.water < 1:
                    raise WaterError()
                self.water -= 1
                plant.water()
        except WaterError as error:
            print(f"Caught GardenError: {error}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        for plant in self.plants:
            try:
                plant.check_health()
            except ValueError as error:
                print(f"Error checking lettuce: {error}")

    def fill_tank(self, amount: int = 1):
        self.water += amount


def main():
    print("=== Garden Management System ===")
    garden = GardenManager("my_garden", None, 2)
    print("\nAdding plants to garden...")
    garden.add_plants([("tomato", 4, 8), ("lettuce", 14, 4), ("", 5, 5)])
    print("\nWatering plants...")
    garden.water_plants()
    print("\nChecking plant health...")
    garden.check_plant_health()
    print("\nTesting error recovery...")
    garden.water_plants()
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
