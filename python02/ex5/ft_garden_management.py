#!/usr/bin/env python3

class GardenError(Exception):
    """
    Base class for garden-related custom exceptions.
    """
    def __init__(self, message: str) -> None:
        """
        Initialize a GardenError instance.

        Args:
            message (str): Description of the error.
        """
        super().__init__(message)


class WaterError(GardenError):
    """
    Raised when there is not enough water in the garden's tank.
    """
    def __init__(self) -> None:
        """
        Initialize a WaterError instance.
        """
        super().__init__("Not enough water in the tank!")


class Plant:
    """
    Represents a plant with a name, water level, and sunlight exposure.
    """
    def __init__(self, name: str, water: int, sun: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            water (int): Initial water level.
            sun (int): Hours of sunlight.

        Raises:
            ValueError: If the plant name is empty.
        """
        if name is None or name == "":
            raise ValueError("Plant name cannot be empty!")
        self.name = name
        self.water_amount = water
        self.sun = sun

    def water(self) -> None:
        """
        Water the plant, increasing its water amount by 1.
        """
        self.water_amount += 1
        print(f"Watering {self.name} - success")

    def check_health(self) -> None:
        """
        Check the plant's health based on water and sunlight.

        Raises:
            ValueError: If water or sunlight levels are out of healthy ranges.
        """
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
    """
    Manages a collection of plants and a water tank.
    """
    def __init__(self, name: str, plants: list[Plant] | None = None,
                 water: int = 0) -> None:
        """
        Initialize a GardenManager instance.

        Args:
            name (str): Name of the garden.
            plants (Optional[List[Plant]], optional): Initial list of plants.
            Defaults to None.
            water (int, optional): Initial water in tank. Defaults to 0.
        """
        self.name = name
        self.plants = plants if plants is not None else []
        self.water = water

    def add_plants(self, plants: list[tuple[str, int, int]]) -> None:
        """
        Add multiple plants to the garden.

        Args:
            plants (List[Tuple[str, int, int]]): List of tuples
            (name, water, sun).

        Prints errors if a plant cannot be added.
        """
        try:
            for data in plants:
                plant = Plant(data[0], data[1], data[2])
                self.plants += [plant,]
                print(f"Added {plant.name} succesfully")
        except ValueError as error:
            print(f"Error adding plant: {error}")

    def water_plants(self) -> None:
        """
        Water all plants in the garden using the available water tank.

        Raises:
            WaterError: If water in tank is insufficient.

        Notes:
            Ensures cleanup with a 'finally' block even if an error occurs.
        """
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

    def check_plant_health(self) -> None:
        """
        Check the health of all plants in the garden.

        Prints errors if any plant's parameters are out of range.
        """
        for plant in self.plants:
            try:
                plant.check_health()
            except ValueError as error:
                print(f"Error checking lettuce: {error}")

    def fill_tank(self, amount: int = 1) -> None:
        """
        Fill the garden's water tank.

        Args:
            amount (int, optional): Amount of water to add. Defaults to 1.
        """
        self.water += amount


def main() -> None:
    """
    Demonstrate the GardenManager system.

    - Adds plants to the garden.
    - Waters plants and handles errors.
    - Checks plant health and recovers from errors.
    """
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
