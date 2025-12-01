#!/usr/bin/env python3

def garden_operations(n: str, plants: dict, target: str,
                      file: str | None) -> None:
    """
    Perform operations on a garden, comparing a target plant's height
    against the average height of all plants and optionally writing
    the result to a file.

    Args:
        n (str): Total number of plants as a string.
        plants (dict[str, int]): Dictionary mapping plant names
        to their heights.
        target (str): Name of the plant to compare against the average.
        file (Optional[str]): File path to write the message to;
        prints to console if None.

    Raises:
        ValueError: If "n" cannot be converted to int.
        ZeroDivisionError: If "n" is zero.
        KeyError: If "target" is not in "plants".
        FileNotFoundError: If the file cannot be opened for writing.
    """
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
    """
    Demonstrate error handling for the garden_operations function
    with different types of errors.

    Tests include:
        - ValueError when "n" is invalid
        - ZeroDivisionError when `n` is zero
        - FileNotFoundError for a missing file
        - KeyError for a missing target plant
        - Multiple errors combined
    """
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
