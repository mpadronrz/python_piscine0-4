#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def show(self):
        print(f"{self.name}: {self.height}cm")

    def grow(self, amount=1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str, blooming: bool=True) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming

    def bloom(self) -> None:
        self.blooming = True
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        if self.blooming:
            print(f"{self.name}: {self.height}cm, {self.color} flowers (blooming)")
        else:
            print(f"{self.name}: {self.height}cm, {self.color} flowers")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize = prize

    def show(self) -> None:
        if self.blooming:
            print(f"{self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.prize}")
        else:
            print(f"{self.name}: {self.height}cm, {self.color} flowers, Prize points: {self.prize}")


class Garden:
    def __init__(self, name: str, plants=None):
        self.name = name
        self.plants = plants if plants != None else []
        self.regular_plants = 0
        self.flower_plants = 0
        self.prize_flowers = 0
        self.total_growth = 0
        for plant in self.plants:
            self.select_type(plant)

    def add_plants(self, plants: list[Plant]):
        for p in plants:
            self.plants += [p,]
            self.select_type(p)
            print(f"Added {p.name} to {self.name}'s garden")

    def select_type(self, plant: Plant):
        if plant.__class__ == PrizeFlower:
            self.prize_flowers += 1
        elif plant.__class__ == FloweringPlant:
            self.flower_plants += 1
        else:
            self.regular_plants += 1

    def show_garden(self):
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("- ", end='')
            plant.show()
        print()
        print(f"Plants added: {self.regular_plants + self.flower_plants + self.prize_flowers}, Total growth: {self.total_growth}")
        print(f"Plant types: {self.regular_plants} regular, {self.flower_plants} flowering, {self.prize_flowers} prize flowers")

    def grow_plants(self, amount=1):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.total_growth += amount


class GardenManager:
    total_gardens = 0

    def __init__(self):
        self.gardens = {}

    def add_garden(self, garden: Garden) -> None:
        self.gardens[garden.name] = garden
        GardenManager.add_to_total()

    @classmethod
    def add_to_total(cls) -> None:
        cls.total_gardens += 1

    @classmethod
    def get_total(cls) -> int:
        return cls.total_gardens

    @classmethod
    def create_garden_network(cls):
        manager = cls()
        manager.add_garden(Garden("Alice"))
        manager.add_garden(Garden("Bob", [PrizeFlower("Tulip", 52, "violet", 10),]))
        return manager

    class GardenStats:
        @staticmethod
        def height_validation(gardens: dict):
            print("Height validation test: ", end='')
            for key in gardens:
                for plant in gardens[key].plants:
                    if plant.height < 0:
                        print("False")
                        return None
            print("True")

        @staticmethod
        def garden_score(garden: Garden) -> int:
            score = 0
            for plant in garden.plants:
                score += plant.height
                if plant.__class__ == PrizeFlower:
                    score += 4 * plant.prize
            return score

        @staticmethod
        def show_statistics(gardens: dict):
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


def main():
    print("=== Garden Management System Demo ===")
    manager = GardenManager.create_garden_network()
    manager.add_garden(Garden("Eve"))
    manager.add_garden(Garden("Martin"))
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
