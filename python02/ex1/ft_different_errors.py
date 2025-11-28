#!/usr/bin/env python3

def garden_operations(n: str, plants: dict, target: str,
                      file: str | None) -> None:
    total_height = 0
    for p in plants:
        total_height += plants[p]
    average = total_height / int(n)
    if average > plants[target]:
        message = "Target is below the average"
    else:
        message = "Target is above the average"
    if file:
        a = open(file, "r+")
        print(message, file=a)
    else:
        print(message)


def test_error_types():
    print("=== Garden Error Types Demo ===")
    plants = {"rose": 25, "sunflower": 80, "cactus": 15}
    print("\nTesting ValueError...")
    try:
        garden_operations("abc", plants, "rose", None)
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("0", plants, "rose", None)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("3", plants, "rose", "missing.txt")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    print("\nTesting KeyError...")
    try:
        garden_operations("3", plants, "missing_plant", None)
    except KeyError as error:
        print(f"Caught KeyError: {error}")
    print("\nTesting multiple errors together...")
    try:
        garden_operations("0", plants, "missing_plant", None)
    except (ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
