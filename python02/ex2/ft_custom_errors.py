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


class PlantError(GardenError):
    """
    Raised when a plant receives too much water (wilting).
    """
    def __init__(self, plant: str) -> None:
        """
        Initialize a PlantError for a specific plant.

        Args:
            plant (str): Name of the plant causing the error.
        """
        super().__init__(f"The {plant} plant is wilting!")


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
    Represents a plant with a name and water level.
    """
    def __init__(self, name: str, water: int = 1) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Plant's name.
            water (int, optional): Initial water amount. Defaults to 1.
        """
        self.name = name
        self.water_amount = water

    def water(self) -> None:
        """
        Water the plant. Raises PlantError if overwatered.

        Raises:
            PlantError: If water amount exceeds 2.
        """
        self.water_amount += 1
        if self.water_amount > 2:
            raise PlantError(self.name)


class Garden:
    """
    Represents a garden with plants and a water tank.
    """
    def __init__(self, name: str, plants=None, water: int = 0) -> None:
        """
        Initialize a Garden instance.

        Args:
            name (str): Garden's name.
            plants (Optional[List[Plant]], optional): Initial list of plants.
            Defaults to None.
            water (int, optional): Initial water in tank. Defaults to 0.
        """
        self.name = name
        self.plants = plants if plants is not None else []
        self.water = water

    def add_plants(self, plants: list[Plant]) -> None:
        """
        Add plants to the garden.

        Args:
            plants (List[Plant]): List of Plant instances to add.
        """
        for p in plants:
            self.plants += [p,]
            print(f"Added {p.name} to {self.name}'s garden")

    def water_plant(self, plant: Plant) -> None:
        """
        Water a specific plant from the garden's tank.

        Args:
            plant (Plant): Plant instance to water.

        Raises:
            WaterError: If there is not enough water in the tank.
            PlantError: If the plant is overwatered.
        """
        if self.water < 1:
            raise WaterError()
        self.water -= 1
        plant.water()

    def fill_tank(self, amount: int = 1) -> None:
        """
        Fill the garden's water tank.

        Args:
            amount (int, optional): Amount of water to add. Defaults to 1.
        """
        self.water += amount


def test_garden_errors() -> None:
    """
    Demonstrate handling of custom garden errors.

    Tests include:
        - PlantError when overwatering a plant
        - WaterError when tank is empty
        - Catching any GardenError
    """
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
