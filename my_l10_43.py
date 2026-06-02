
# class Animal:
#     def __init__(self, species, color, number_of_legs=4):
#         self.species = species
#         self.color = color
#         self.number_of_legs = number_of_legs
#
#     def __repr__(self):
#         return f"{self.color.title()} {self.species} {self.number_of_legs} legs"
#
# class Sheep(Animal):
#     def __init__(self, color):
#         super().__init__("sheep", color, 4)
#
#
# class Wolf(Animal):
#     def __init__(self, color):
#         super().__init__("wolf", color, 4)
#
# class Snake(Animal):
#     def __init__(self, color):
#         super().__init__("snake", color, 0)
#
# class Parrot(Animal):
#     def __init__(self, color):
#         super().__init__("parrot", color, 2)

# Claude's
class Animal:
    SPECIES = None
    LEGS = None

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f"{self.color.title()} {self.SPECIES} {self.LEGS} legs"

class Sheep(Animal):
    SPECIES = "sheep"
    LEGS = 4

class Wolf(Animal):
    SPECIES = "wolf"
    LEGS = 4

class Snake(Animal):
    SPECIES = "snake"
    LEGS = 0

class Parrot(Animal):
    SPECIES = "parrot"
    LEGS = 2

s = Sheep("brown")
print(s)
w = Wolf("gray")
print(w)
sn = Snake("yellow")
print(sn)
p = Parrot("green")
print(p)
