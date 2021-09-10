from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.weapon = [Weapon("Saber", 3), Weapon("Lazer", 5), Weapon("Rocket", 7)]

    def attack(self, dinosaur):
        weapon_option = input(
            "What weapon would you like to use to attack with? \n Enter 1 for Saber, 2 for Lazer, 3 for Rocket: "
        )
        if weapon_option == 1:
            dinosaur.health = dinosaur.health - self.weapon[0].attack_power
        elif weapon_option == 1:
            dinosaur.health = dinosaur.health - self.weapon[1].attack_power
        elif weapon_option == 1:
            dinosaur.health = dinosaur.health - self.weapon[2].attack_power
