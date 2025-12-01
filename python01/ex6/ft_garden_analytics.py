#!/usr/bin/env python3

class Plant:
    """
    Represents a generic plant with a name and height.
    """
    def __init__(self, name: str, height: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): The plant's name.
            height (int): Height of the plant in centimeters.
        """
        self.name = name
        self.height = height

    def show(self) -> None:
        """
        Displays plant information in an organized way
        """
        print(f"{self.name}: {self.height}cm")

    def grow(self, amount=1) -> None:
        """
        Increase the plant's height by a given amount.

        Args:
            amount (int, optional): Height to grow incentimeters.
            Defaults to 1.
        """
        self.height += amount
        print(f"{self.name} grew {amount}cm")


class FloweringPlant(Plant):
    """
    Represents a flowering plant with color and blooming status.
    """
    def __init__(self, name: str, height: int, color: str,
                 blooming: bool = True) -> None:
        """
        Initialize a FloweringPlant instance.

        Args:
            name (str): The plant's name.
            height (int): Height in centimeters.
            color (str): Flower color.
            blooming (bool, optional): Whether the plant is blooming.
            Defaults to True.
        """
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming

    def bloom(self) -> None:
        """
        Set the plant's blooming status to True and print a message.
        """
        self.blooming = True
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        """
        Displays flowering plant information in an organized way
        """
        if self.blooming:
            print(f"{self.name}: {self.height}cm, {self.color} "
                  "flowers (blooming)")
        else:
            print(f"{self.name}: {self.height}cm, {self.color} flowers")


class PrizeFlower(FloweringPlant):
    """
    Represents a flowering plant with an associated prize value.
    """
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        """
        Initialize a PrizeFlower instance.

        Args:
            name (str): Plant name.
            height (int): Height in centimeters.
            color (str): Flower color.
            prize (int): Prize points for the plant.
        """
        super().__init__(name, height, color)
        self.prize = prize

    def show(self) -> None:
        """
        Displays prize flower information in an organized way
        """
        if self.blooming:
            print(f"{self.name}: {self.height}cm, {self.color} "
                  f"flowers (blooming), Prize points: {self.prize}")
        else:
            print(f"{self.name}: {self.height}cm, {self.color} "
                  f"flowers, Prize points: {self.prize}")


class Garden:
    """
    Represents a garden that contains plants of different types and
    tracks statistics.
    """
    def __init__(self, name: str, plants=None) -> None:
        """
        Initialize a Garden instance.

        Args:
            name (str): The garden's name.
            plants (list[Plant], optional): Initial list of plants.
            Defaults to None.
        """
        self.name = name
        self.plants = plants if plants is not None else []
        self.regular_plants = 0
        self.flower_plants = 0
        self.prize_flowers = 0
        self.total_growth = 0
        for plant in self.plants:
            self.select_type(plant)

    def add_plants(self, plants: list[Plant]) -> None:
        """
        Add plants to the garden and update type counts.

        Args:
            plants (list[Plant]): List of Plant instances to add.
        """
        for p in plants:
            self.plants += [p,]
            self.select_type(p)
            print(f"Added {p.name} to {self.name}'s garden")

    def select_type(self, plant: Plant) -> None:
        """
        Classify a plant and update type counts.

        Args:
            plant (Plant): Plant instance to classify.
        """
        if plant.__class__ == PrizeFlower:
            self.prize_flowers += 1
        elif plant.__class__ == FloweringPlant:
            self.flower_plants += 1
        else:
            self.regular_plants += 1

    def show_garden(self) -> None:
        """
        Displays garden information in an organized way.
        """
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("- ", end='')
            plant.show()
        print()
        print(f"Plants added: {self.regular_plants +
                               self.flower_plants + self.prize_flowers}"
              f", Total growth: {self.total_growth}")
        print(f"Plant types: {self.regular_plants} regular, "
              f"{self.flower_plants} flowering, "
              f"{self.prize_flowers} prize flowers")

    def grow_plants(self, amount=1) -> None:
        """
        Grow all plants in the garden by a specified amount.

        Args:
            amount (int, optional): Growth in centimeters. Defaults to 1.
        """
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.total_growth += amount


class GardenManager:
    """
    Manages multiple gardens and provides statistics for them.
    """
    total_gardens = 0

    def __init__(self) -> None:
        """
        Initialize a GardenManager instance.
        """
        self.gardens = {}

    def add_garden(self, garden: Garden) -> None:
        """
        Add a garden to the manager and update the total count.

        Args:
            garden (Garden): Garden instance to add.
        """
        self.gardens[garden.name] = garden
        GardenManager.add_to_total()

    @classmethod
    def add_to_total(cls) -> None:
        """
        Increment the total number of gardens managed.
        """
        cls.total_gardens += 1

    @classmethod
    def get_total(cls) -> int:
        """
        Return the total number of gardens managed.

        Returns:
            int: Total gardens count.
        """
        return cls.total_gardens

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """
        Create a sample garden network with predefined gardens and plants.

        Returns:
            GardenManager: A manager with sample gardens added.
        """
        manager = cls()
        manager.add_garden(Garden("Alice"))
        manager.add_garden(Garden("Bob", [PrizeFlower("Tulip",
                                                      52, "violet", 10),]))
        return manager

    class GardenStats:
        """
        Provides static methods for garden validation and statistics.
        """
        @staticmethod
        def height_validation(gardens: dict) -> None:
            """
            Check that all plants have non-negative heights.

            Args:
                gardens (dict): Dictionary of garden_name -> Garden instances.
            """
            print("Height validation test: ", end='')
            for key in gardens:
                for plant in gardens[key].plants:
                    if plant.height < 0:
                        print("False")
                        return None
            print("True")

        @staticmethod
        def garden_score(garden: Garden) -> int:
            """
            Calculate a garden's score based on plant heights and prize points.

            Args:
                garden (Garden): The garden to score.

            Returns:
                int: Total score of the garden.
            """
            score = 0
            for plant in garden.plants:
                score += plant.height
                if plant.__class__ == PrizeFlower:
                    score += 4 * plant.prize
            return score

        @staticmethod
        def show_statistics(gardens: dict) -> None:
            """
            Display height validation and scores for all gardens.

            Args:
                gardens (dict): Dictionary of garden_name -> Garden instances.
            """
            GardenManager.GardenStats.height_validation(gardens)
            print("Garden scores - ", end='')
            i = 0
            for key in gardens:
                score = GardenManager.GardenStats.garden_score(gardens[key])
                if i > 0:
                    print(", ", end='')
                print(f"{gardens[key].name}: {score}", end='')
                i += 1
            print()
            print(f"Total gardens managed: {GardenManager.get_total()}")


def main() -> None:
    """
    Demonstrate the Garden Management System by creating a sample network,
    adding plants, growing them, and showing statistics.
    """
    print("=== Garden Management System Demo ===")
    manager = GardenManager.create_garden_network()
    manager.gardens["Alice"].add_plants([
        Plant("Oak tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10),
    ])
    print()
    manager.gardens["Alice"].grow_plants()
    print()
    manager.gardens["Alice"].show_garden()
    print()
    GardenManager.GardenStats.show_statistics(manager.gardens)


if __name__ == "__main__":
    main()
