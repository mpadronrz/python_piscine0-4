#!/usr/bin/env python3

class Plant:
    total_plants = {None: 0}
    growth = {None: 0}

    def __init__(self, name: str, height: int, garden=None) -> None:
        self.name = name
        self.height = height
        self.garden = garden
        self.__class__.add_plant()

    def show(self):
        print(f"{self.name}: {self.height}cm")

    def grow(self, amount=1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")
        Plant.register_growth(self.garden, amount)

    @classmethod
    def add_plant(cls, key=None):
        if key in cls.total_plants:
            cls.total_plants[key] +=1
        else:
            cls.total_plants[key] = 1

    @classmethod
    def change_plant(cls, origin, end):
        cls.total_plants[origin] -= 1
        if end in cls.total_plants:
            cls.total_plants[end] += 1
        else:
            cls.total_plants[end] = 1

    @classmethod
    def get_plants(cls, key=None) -> int:
        if key in cls.total_plants:
            return cls.total_plants[key]
        else:
            return 0

    @classmethod
    def register_growth(cls, garden, amount):
        if garden in cls.growth:
            cls.growth[garden] += amount
        else:
            cls.growth[garden] = amount

    @classmethod
    def total_growth(cls, garden):
        if garden in cls.growth:
            return cls.growth[garden]
        else:
            return 0


class FloweringPlant(Plant):
    total_plants = {None: 0}

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
    total_plants = {None: 0}

    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize = prize

    def show(self) -> None:
        if self.blooming:
            print(f"{self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.prize}")
        else:
            print(f"{self.name}: {self.height}cm, {self.color} flowers, Prize points: {self.prize}")


class Garden:
    def __init__(self, name: str):
        self.name = name
        self.plants = []
        self.total_plants = 0

    def add_plants(self, plants: list[Plant]):
        for p in plants:
            self.plants += [p,]
            p.__class__.change_plant(p.garden, self.name)
            p.garden = self.name
            self.total_plants += 1
            print(f"Added {p.name} to {self.name}'s garden")

    def show_garden(self):
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("- ", end='')
            plant.show()
        print()
        print(f"Plants added: {self.total_plants}, Total growth: {Plant.total_growth(self.name)}")
        print(f"Plant types: {Plant.get_plants(self.name)} regular, {FloweringPlant.get_plants(self.name)} flowering, {PrizeFlower.get_plants(self.name)} prize flowers")

    def grow_plants(self, amount=1):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)


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
    manager = GardenManager()
    manager.add_garden(Garden("Alice"))
    manager.add_garden(Garden("Bob"))
    manager.gardens["Alice"].add_plants([
        Plant("Oak tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10),
        Plant("Cactus", 12)
    ])
    manager.gardens["Bob"].add_plants([
        PrizeFlower("Tulip", 52, "violet", 10),
    ])
    print()
    manager.gardens["Alice"].grow_plants()
    print()
    manager.gardens["Alice"].show_garden()
    print()
    GardenManager.GardenStats.show_statistics(manager.gardens)




if __name__ == "__main__":
    main()
