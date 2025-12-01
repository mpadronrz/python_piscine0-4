#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int | None:
    """
    Validate and check a temperature string for suitability for plants.

    Args:
        temp_str (str): Temperature input as a string.

    Returns:
        Optional[int]: The temperature as an integer if valid
        and within range (0-40°C), otherwise None.
    """
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants")
            return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """
    Demonstrate the check_temperature function with a set of test inputs.

    Tests include valid temperatures, negative values, overly high values,
    and invalid non-numeric inputs.
    """
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    for temp in tests:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
