#!/usr/bin/env python3

def water_plants(plant_list: list[str]) -> None:
    """
    Simulate watering a list of plants, handling type errors gracefully.

    Args:
        plant_list (List[Optional[str]]): List of plant names to water.

    Notes:
        - If a plant is not a string, a TypeError is caught
            and an error message is printed.
        - The cleanup code in 'finally' always executes.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Demonstrate the watering system with normal and error cases.

    Tests include:
        - Normal watering of a list of valid plant names.
        - Watering with a list containing an invalid plant
            (None) to trigger an error.
    """
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
