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
        turn = "dino"
        self.battle(turn)

    def display_welcome(self):
        pass

    def battle(self, turn):
        if turn == "dino":
            self.show_robo_opponent_options()
        elif turn == "robo":
            self.show_dino_opponent_options()

    def dino_turn(self, dinosaur):
        player_choice = input(
            "Which Robot would you like to attack?\n Enter 1 for Robo1, 2 for Robo2, 3 for Robo3 "
        )
        if player_choice == "1":
            dinosaur.attack(self.fleet.robots[0])
            self.battle("robo")
        elif player_choice == "2":
            dinosaur.attack(self.fleet.robots[1])
            self.battle("robo")
        elif player_choice == "3":
            dinosaur.attack(self.fleet.robots[3])
            self.battle("robo")

    def robo_turn(self, robot):
        player_choice = input(
            "Which Dinosaur would you like to attack?\n Enter 1 for Dino1, 2 for Dino2, 3 for Dino3 "
        )
        if player_choice == "1":
            robot.attack(self.herd.dinosaurs[0])
            self.battle("dino")
        elif player_choice == "2":
            robot.attack(self.herd.dinosaurs[1])
            self.battle("dino")
        elif player_choice == "3":
            robot.attack(self.herd.dinosaurs[2])
            self.battle("dino")

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
                print("Robo2 health is: ", self.fleet.robots[1].health)
            elif player_choice == "3":
                print("Robo3 health is: ", self.fleet.robots[2].health)
            elif player_choice == "4":
                print("Dino1 health is: ", self.herd.dinosaurs[0].health)
            elif player_choice == "5":
                print("Dino2 health is: ", self.herd.dinosaurs[1].health)
            elif player_choice == "6":
                print("Dino3 health is: ", self.herd.dinosaurs[2].health)
            else:
                player_choice = input(
                    "Invalid selection, please try again \n Which player would you like to check? \n Enter 1 for Robo1, 2 for Robo2, 3 for Robo3, 4 for Dino1, 5 for Dino2, 6 for Dino3 "
                )

        elif option == "a":
            attacker_choice = input(
                "Which Robot do you want to attack with? \n Enter 1 for Robo1, 2 for Robo2, 3 for Robo3"
            )
            if attacker_choice == "1":
                self.robo_turn(self.fleet.robots[0])
            elif attacker_choice == "2":
                self.robo_turn(self.fleet.robots[1])
            elif attacker_choice == "3":
                self.robo_turn(self.fleet.robots[2])

    def show_robo_opponent_options(self):
        option = input(
            "Dino turn: What would you like to do:\n Enter H for health check or A for attack "
        )

        if option == "h":
            player_choice = input(
                "Which player would you like to check?\n Enter 1 for Robo1, 2 for Robo2, 3 for Robo3 \n 4 for Dino1, 5 for Dino2, 6 for Dino3 "
            )
            if player_choice == "1":
                print("Robo1 health is: ", self.fleet.robots[0].health)
            elif player_choice == "2":
                print("Robo2 health is: ", self.fleet.robots[1].health)
            elif player_choice == "3":
                print("Robo3 health is: ", self.fleet.robots[2].health)
            elif player_choice == "4":
                print("Dino1 health is: ", self.herd.dinosaurs[0].health)
            elif player_choice == "5":
                print("Dino2 health is: ", self.herd.dinosaurs[1].health)
            elif player_choice == "6":
                print("Dino3 health is: ", self.herd.dinosaurs[2].health)
            else:
                player_choice = input(
                    "Invalid selection, please try again \n Which player would you like to check? \n Enter 1 for Robo1, 2 for Robo2, 3 for Robo3, 4 for Dino1, 5 for Dino2, 6 for Dino3 "
                )

        elif option == "a":
            attacker_choice = input(
                "Which Dinosaur do you want to attack with? \n Enter 1 for Dino1, 2 for Dino2, 3 for Dino3"
            )
            if attacker_choice == "1":
                self.dino_turn(self.herd.dinosaurs[0])
            elif attacker_choice == "2":
                self.dino_turn(self.herd.dinosaurs[1])
            elif attacker_choice == "3":
                self.dino_turn(self.herd.dinosaurs[2])

    def display_winners(self):
        pass
