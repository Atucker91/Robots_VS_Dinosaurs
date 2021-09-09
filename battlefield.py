from fleet import Fleet
from herd import Herd
from herd import Herd
from robot import Robot
from weapon import Weapon
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.battle()

    def display_welcome(self):
        pass

    def battle(self):
        self.dino_turn(self.herd.dinosaurs[0])

    def dino_turn(self, dinosaur):
        dinosaur.attack(self.fleet.robots[0])

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        option = input(
            "Robo turn: What would you like to do:\n Enter H for health check or A for attack "
        )

        if option == h:
            input(
                "Which robo would you like to check?\n Enter 1 for Robo1, 2 for Robo2, 3 for Robo3"
            )
        elif option == a:
            pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
