from robot import Robot


class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 20

    def attack(self, robot):
        robot.health = robot.health - self.attack_power
