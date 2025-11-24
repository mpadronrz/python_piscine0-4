#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(days)

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"Invalid operation attempted: height "
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return None
        self._height = new_height
        print(f"Height updated: {new_height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} "
                  f"days [REJECTED]")
            print("Security: Negative age rejected")
            return None
        self._age = new_age
        print(f"Age updated: {new_age} days [OK]")

    def current_info(self):
        print(f"Current plant: {self.name} ({self.get_height()}cm, "
              f"{self.get_age()} days)")


def main():
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    print("")
    plant.set_height(-5)
    print("")
    plant.current_info()


if __name__ == "__main__":
    main()
