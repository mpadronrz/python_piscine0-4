#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height += 1

    def age(self):
        self.age += 1


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    day = 1
    while day < 8:
        print(f"=== Day {day} ===")
        plant1.get_info()
        plant2.get_info()
        plant3.get_info()
        plant1.grow()
        plant2.grow()
        plant3.grow()
        plant1.age()
        plant2.age()
        plant3.age()
