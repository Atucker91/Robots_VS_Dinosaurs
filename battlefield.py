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

        self.fleet.create_fleet()
        self.herd.create_herd()

    def display_welcome(self):
        pass

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
