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
        self.show_dino_opponent_options()

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        option = input(
            "Robo turn: What would you like to do:\n Enter H for health check or A for attack "
        )

        if option == "h":
            player_choice = input(
                "Which player would you like to check?\n Enter 1 for Robo1, 2 for Robo2, 3 for Robo3 \n 4 for Dino1, 5 for Dino2, 6 for Dino3 "
            )
            if player_choice == "1":
                print("Robo1 health is: ", self.fleet.robots[0].health)
            elif player_choice == "2":
                print(self.fleet.robots[1].health)
            elif player_choice == "3":
                print(self.fleet.robots[2].health)
            elif player_choice == "4":
                print(self.herd.dinosaurs[0].health)
            elif player_choice == "5":
                print(self.herd.dinosaurs[1].health)
            elif player_choice == "6":
                print(self.herd.dinosaurs[2].health)
            else:
                player_choice = input(
                    "Invalid selection, please try again \n Which player would you like to check? \n Enter 1 for Robo1, 2 for Robo2, 3 for Robo3, 4 for Dino1, 5 for Dino2, 6 for Dino3 "
                )

        elif option == "a":
            self.robo_turn()

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
