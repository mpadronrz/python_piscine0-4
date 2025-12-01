#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """
    Check if a plant's water level and sunlight hours are
    within healthy ranges.

    Args:
        plant_name (str): Name of the plant.
        water_level (int): Amount of water given to the plant (1-10).
        sunlight_hours (int): Number of hours of sunlight received (2-12).

    Raises:
        ValueError: If the plant name is empty or any
        parameter is out of allowed range.
    """
    if plant_name is None or plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    Demonstrate the check_plant_health function with valid and invalid inputs.

    Tests include:
        - Valid plant health parameters.
        - Empty plant name.
        - Water level too high or too low.
        - Sunlight hours too high or too low.
    """
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        check_plant_health("tomato", 5, 5)
    except ValueError as error:
        print(f"Error: {error}")
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as error:
        print(f"Error: {error}")
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as error:
        print(f"Error: {error}")
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as error:
        print(f"Error: {error}")
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
