#!/usr/bin/env python3

def ft_garden_intro(plant: str, height: int, age: str) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro("Rose", 25, 30)
