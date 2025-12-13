#! /usr/bin/env python3

import math


def distance(coordinates: tuple[str]):
    dist = 0
    for i in coordinates:
        dist += i ** 2
    dist = math.sqrt(dist)
    print(f"Distance between (0, 0, 0) and {coordinates}: {dist:.2f}")
    return dist


def parse_coordinates(data: str) -> tuple[int] | None:
    elems = data.split(",")
    i = 0
    for num in elems:
        try:
            int(num)
        except ValueError as error:
            print(f"Error parsing coordinates: {error}")
            print(f"Error details - Type: ValueError, Args: {error}")
            return None
        i += 1
    if i != 3:
        print("Error parsing coordinates: number of coordinates must be 3")
        return
    coordinates = tuple(int(num) for num in elems)
    print(f"Parsed position: {coordinates}")
    distance(coordinates)
    return coordinates


def create_position(coordinates: tuple[int]) -> tuple[int] | None:
    i = 0
    for num in coordinates:
        i += 1
    if i != 3:
        print("Error crating position: number of coordinates must be 3")
        return
    print(f"Position created: {coordinates}")
    distance(coordinates)


def unpack_coordinates(coordinates: tuple[int]) -> None:
    print(f"Player at x={coordinates[0]}, "
          f"y={coordinates[1]}, z={coordinates[2]}")
    x, y, z, = coordinates
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    create_position((10, 20, 5))

    print('\nParsing coordinates: "3,4,0"')
    coords = parse_coordinates("3,4,0")
    print('\nParsing invalid coordinates: "abc,def,ghi"')
    parse_coordinates("abc,def,ghi")
    print("\nUnpacking demonstration:")
    unpack_coordinates(coords)


if __name__ == "__main__":
    main()
