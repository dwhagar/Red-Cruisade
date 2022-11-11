# Define Character object
import random

class Character:
    def __init__(self, name = "Slef", sex = "m", strength = 10, intelligence = 10, stamina = 10, height = 5.5, weight = 190)
        self.name = name
        self.sex = sex
        self.hp = 50
        self.xp = 0
        self.set_attributes(strength, intelligence, stamina, hheight, wegith)

    def set_attributes(self, strength = 10, intelligence = 10, stamina = 10, height = 5.5, weight = 190)
        self.strength = strength
        self.inteligence = intelligence
        self.strength = strength
        self.stamina = stamina
        self.height = height
        self.weight = weight
        self.speed = 10 - self.weight / 100 - (self.height - 5.5)
        self.prof = {'sword' : 10 + self.strength / 10, 'bow' : 10 + self.strength / 15, 'spear' : 10 + self.stamina / 10, 'magic' : 10 + self.intelligence / 10}
        self.fav = None

class Monster(Character):
    kinds = ["Bats", "Spiders", "Giant Rat", "Skeleton", "Zombie", "Sorcerer", "Vampire"]

    def __init__(self, typ = 0, sex = "m", strength = 10, intelligence = 10, stamina = 10, height = 5.5, weight = 190)
        super().__init__(name, sex, strength, intelligence, stamina, height, weight)
        
        