#!/usr/bin/env python3

class SecurePlant:
    """
    A safe plant model that validates height and age before updating them.
    """
    def __init__(self, name: str, height: int, days: int) -> None:
        """
        Initialize a SecurePlant instance and validate initial values.

        Args:
            name (str): The plant's name.
            height (int): Initial height in centimeters.
            days (int): Initial age in days.
        """
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(days)

    def get_height(self) -> int:
        """
        Return the plant's current height.

        Returns:
            int: The height in centimeters.
        """
        return self._height

    def get_age(self) -> int:
        """
        Return the plant's current age.

        Returns:
            int: The age in days.
        """
        return self._age

    def set_height(self, new_height: int) -> None:
        """
        Update the plant's height if the value is valid.
        Rejects negative heights and displays a warning.

        Args:
            new_height (int): The updated height in centimeters.
        """
        if new_height < 0:
            print(f"Invalid operation attempted: height "
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return None
        self._height = new_height
        print(f"Height updated: {new_height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        """
        Update the plant's age if the value is valid.
        Rejects negative ages and displays a warning.

        Args:
            new_age (int): The updated age in days.
        """
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} "
                  f"days [REJECTED]")
            print("Security: Negative age rejected")
            return None
        self._age = new_age
        print(f"Age updated: {new_age} days [OK]")

    def current_info(self) -> None:
        """
        Displays plant information in an organized way
        """
        print(f"Current plant: {self.name} ({self.get_height()}cm, "
              f"{self.get_age()} days)")


def main() -> None:
    """
    Demonstrate the SecurePlant system by creating a plant,
    attempting invalid updates, and displaying current values.
    """
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    print("")
    plant.set_height(-5)
    print("")
    plant.current_info()


if __name__ == "__main__":
    main()
