#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    day = 1
    while day < 8:
        print(f"=== Day {day} ===")
        plant1.get_info()
        plant1.grow()
        plant1.age()
        day += 1
    print(f"Growth this week: +{day - 2}cm")
