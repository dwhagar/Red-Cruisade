# Define Character object
import random
import os

random.seed(os.urandom())

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
        self.typ = typ
    
        self.fly = False
        
        gender = random.randrange(0,1)
        if gender = 0:
            self.sex = 'm'
        else:
            self.sex = 'f'
        
        if self.typ = 6 or self.typ = 7:
            self.name = generate_name()
        else:
            self.name = self.kinds[self.typ]
            
        self.level_min = 0
        self.level_max = 0
        
        self.resistance = {"melee" : 0,
        "ranged" : 0,
        "magic" : 0}
        
        self.buffs = {'echo' : False,
            'poison' : False,
            'web' : False,
            'tail' : False,
            'scream' : False,
            'rain' : False}
        
    def bat_attributes(self):
        self.hp = random.randrange(2,4)
        self.fly = True
        self.speed = random.randrange(80,120)
        self.level_min = 1
        self.level_max = random.randrange(3,5)
    
    def generate_name(self):
        male_names = [
            "Fred",
            "Jerry",
            "Zach",
            "George",
            "Brandon",
            "Obama",
            "Scotty",
            "Pippin",
            "Frank",
            "Jimmy",
            "Parker",
            "Tyler",
            "Wyatt",
            "Jacob",
            "Paul",
            "Brayden",
            "Todd",
            "John",
            "Tyreek",
            "Caleb",
            "Walter",
            "Kenneth",
            "Gustavo",
            "Mike",
            "Jessie",
            "Justin",
            "Dough",
            "Cayden",
            "Chad",
            "Gary",
            "Curt",
            "Ernest",
            "Cole",
            "Aiden",
            "Carter"
        ]
        female_names = [
            "Skylar",
            "Brittany",
            "Rachel",
            "Ashley",
            "Jessica",
            "Hope",
            "Karen",
            "Faith",
            "Rylee",
            "Joan",
            "Tracy",
            "Izzy",
            "Dawn",
            "Becca",
            "Madison",
            "Rae",
            "Naomi",
            "Addie",
            "Arial",
            "Jane",
            "Jennifer",
            "Jeanette",
            "Avery",
            "Felcia",
            "Rebecca",
            "Gabby",
            "Emma",
            "Catherine",
            "Buttecup",
            "Bubbles",
            "Pinky",
            "Patricia"
        ]
        
        result = ""
        
        if self.gender = "m":
            result = self.random_name(male_names)
        else:
            result = self.random_name(female_names)
        
        return result
        
        def random_name(self, names):
            total = len(names)
            pick = random.randrange(0, total)
            return names[pick]