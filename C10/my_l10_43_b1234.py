class Animal:
    SPECIES = None
    LEGS = None
    SOUND = None

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f"{self.SOUND} {self.color} {self.SPECIES} {self.LEGS} legs"

class  Quadruped(Animal):
    LEGS = 4

class Biped(Animal):
    LEGS = 2

class Legless(Animal):
    LEGS = 0

class Sheep(Quadruped):
    SPECIES = "sheep"
    SOUND = "baa"


class Wolf(Quadruped):
    SPECIES = "wolf"
    SOUND = "grr"


class Snake(Legless):
    SPECIES = "snake"
    SOUND = "hiss"

class Parrot(Biped):
    SPECIES = "parrot"
    SOUND = "tweet"


s = Sheep("brown")
print(s)
w = Wolf("gray")
print(w)
sn = Snake("yellow")
print(sn)
p = Parrot("green")
print(p)