#! /usr/bin/env python3

import math


def coordinates(coords: str) -> tuple[int] | None:
    coords = coords.split(",")
    try:
        num = tuple(int(i) for i in coords)
    except ValueError as error:
        print(f"Error parsing coordinate: {error}")
        print(f"Error details - Type: ValueError, Args: {error}")
        return None
    print(f"Parsed position: {num}")
    dist = 0
    for i in num:
        dist += i ** 2
    dist = math.sqrt(dist)
    print(f"Distance between (0, 0, 0) and {num}: {dist}")
    return num


def unpack_coordinates(coords: tuple[int]) -> None:
    print(f"Player at x={coords[0]}, y={coords[1]}, z={coords[2]}")
    print(f"Coordinates: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    coordinates("10,20,5")
    print('\nParsing coordinates: "3,4,0"')
    coords = coordinates("3,4,0")
    print('\nParsing invalid coordinates: "abc,def,ghi"')
    coordinates("abc,def,ghi")
    print("\nUnpacking demonstration:")
    unpack_coordinates(coords)


if __name__ == "__main__":
    main()
