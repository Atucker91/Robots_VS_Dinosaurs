from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.weapon = [Weapon("Saber", 3), Weapon("Lazer", 5), Weapon("Rocket", 7)]

    def attack(self, dinosaur):
        pass
