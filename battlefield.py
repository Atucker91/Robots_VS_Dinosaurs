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
        self.display_welcome()
        self.battle(turn)

    def display_welcome(self):
        print("Battle of robots VS dinosaurs will begin")

    def battle(self, turn):
        winner = ""

        if (
            self.fleet.robots[0].health < 0
            and self.fleet.robots[1].health < 0
            and self.fleet.robots[2].health < 0
        ):
            winner = "dino"
            turn = ""
            self.display_winners(winner)
        elif (
            self.herd.dinosaurs[0].health < 0
            and self.herd.dinosaurs[1].health < 0
            and self.herd.dinosaurs[2].health < 0
        ):
            winner = "robo"
            turn = ""
            self.display_winners(winner)

        if turn == "dino":
            self.show_robo_opponent_options()
        elif turn == "robo":
            self.show_dino_opponent_options()

    def dino_turn(self, dinosaur):
        print(
            "Which Robot would you like to attack?\nRobo1: Health= ",
            self.fleet.robots[0].health,
            "\nRobo2: Health= ",
            self.fleet.robots[1].health,
            "\nRobo3: Health= ",
            self.fleet.robots[2].health,
        )
        player_choice = input("Enter 1 for Robo1\n2 for Robo2\n3 for Robo3")
        if player_choice == "1":
            dinosaur.attack(self.fleet.robots[0])
            print(
                "Damage inflicted! Robo1 now has ",
                self.fleet.robots[0].health,
                " points of health",
            )
            self.battle("robo")
        elif player_choice == "2":
            dinosaur.attack(self.fleet.robots[1])
            print(
                "Damage inflicted! Robo2 now has ",
                self.fleet.robots[1].health,
                " points of health",
            )
            self.battle("robo")
        elif player_choice == "3":
            dinosaur.attack(self.fleet.robots[2])
            print(
                "Damage inflicted! Robo3 now has ",
                self.fleet.robots[2].health,
                " points of health",
            )
            self.battle("robo")

    def robo_turn(self, robot):
        print(
            "Which Dinosaur would you like to attack?\nDino1: Health= ",
            self.herd.dinosaurs[0].health,
            "\nDino2: Health= ",
            self.herd.dinosaurs[1].health,
            "\nDino3: Health= ",
            self.herd.dinosaurs[2].health,
        )
        player_choice = input("Enter 1 for Dino1\n2 for Dino2\n3 for Dino3")
        if player_choice == "1":
            robot.attack(self.herd.dinosaurs[0])
            print(
                "Damage inflicted! Dino1 now has ",
                self.herd.dinosaurs[0].health,
                " points of health",
            )
            self.battle("dino")
        elif player_choice == "2":
            robot.attack(self.herd.dinosaurs[1])
            print(
                "Damage inflicted! Dino2 now has ",
                self.herd.dinosaurs[1].health,
                " points of health",
            )
            self.battle("dino")
        elif player_choice == "3":
            robot.attack(self.herd.dinosaurs[2])
            print(
                "Damage inflicted! Dino3 now has ",
                self.herd.dinosaurs[2].health,
                " points of health",
            )
            self.battle("dino")

    def show_dino_opponent_options(self):

        attacker_choice = "1"

        print(
            "Team Health:\nRobo1: Health= ",
            self.fleet.robots[0].health,
            "\nRobo2: Health= ",
            self.fleet.robots[1].health,
            "\nRobo3: Health= ",
            self.fleet.robots[2].health,
        )

        while (
            attacker_choice == "1" or attacker_choice == "2" or attacker_choice == "3"
        ):
            attacker_choice = input(
                "Which Robot do you want to attack with? \n Enter 1 for Robo1, 2 for Robo2, 3 for Robo3: "
            )
            if attacker_choice == "1":
                if self.fleet.robots[0].health > 0:
                    self.robo_turn(self.fleet.robots[0])
                else:
                    print("Robo1 has been defeated, please choose another Robot")
            elif attacker_choice == "2":
                if self.fleet.robots[1].health > 0:
                    self.robo_turn(self.fleet.robots[1])
                else:
                    print("Robo2 has been defeated, please choose another Robot")
            elif attacker_choice == "3":
                if self.fleet.robots[2].health > 0:
                    self.robo_turn(self.fleet.robots[2])
                else:
                    print("Robo3 has been defeated, please choose another Robot")

    def show_robo_opponent_options(self):

        attacker_choice = "1"

        print(
            "Team Health\nDino1: Health= ",
            self.herd.dinosaurs[0].health,
            "\nDino2: Health= ",
            self.herd.dinosaurs[1].health,
            "\nDino3: Health= ",
            self.herd.dinosaurs[2].health,
        )

        while (
            attacker_choice == "1" or attacker_choice == "2" or attacker_choice == "3"
        ):
            attacker_choice = input(
                "Which Dinosaur do you want to attack with? \n Enter 1 for Dino1, 2 for Dino2, 3 for Dino3: "
            )
            if attacker_choice == "1":
                if self.herd.dinosaurs[0].health > 0:
                    self.dino_turn(self.herd.dinosaurs[0])
                else:
                    print("Dino1 has been defeated, please choose another Dinosaur")
            elif attacker_choice == "2":
                if self.herd.dinosaurs[1].health > 0:
                    self.dino_turn(self.herd.dinosaurs[1])
                else:
                    print("Dino2 has been defeated, please choose another Dinosaur")
            elif attacker_choice == "3":
                if self.herd.dinosaurs[2].health > 0:
                    self.dino_turn(self.herd.dinosaurs[2])
                else:
                    print("Dino3 has been defeated, please choose another Dinosaur")

    def display_winners(self, winner):
        if winner == "dino":
            print("All Robots Have Been Defeated, Dinosaurs Win!")
        elif winner == "robo":
            print("All Dinosaurs Have Been Defeated, Robots Win!")
