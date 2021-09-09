from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robo_one = Robot("Robo1")
        self.robots.append(robo_one)
        robo_two = Robot("Robo2")
        self.robots.append(robo_two)
        robo_three = Robot("Robo3")
        self.robots.append(robo_three)
