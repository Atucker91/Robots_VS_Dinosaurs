from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur("Dino1", 3)
        self.dinosaurs.append(dino_one)
        dino_two = Dinosaur("Dino2", 5)
        self.dinosaurs.append(dino_two)
        dino_three = Dinosaur("Dino3", 7)
        self.dinosaurs.append(dino_three)
