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

# class Cage:
#     count = 0
#     def __init__(self, *animals):
#         self.animals: list[Animal] = list(animals)
#         Cage.count += 1
#         self.id = self.count
#
#     def __repr__(self):
#         return f"Cage # {self.id}: {len(self.animals)} animals: {', '.join(str(animal) for animal in self.animals)}"
#
#     def add_animals_to_cage(self, *animals):
#         self.animals.extend(animals)

# Claude's
class Cage:
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals: list[Animal] = []

    def add_animals(self, *animals):
        """Add one or more animals to the cage. Returns None."""
        self.animals.extend(animals)          # your cleaner approach

    def __repr__(self):
        animal_list = ', '.join(str(a) for a in self.animals)
        return f"Cage {self.id_number} ({len(self.animals)} animals): {animal_list}"

sheep1 = Sheep("brown")
print(sheep1)
wolf1 = Wolf("gray")
print(wolf1)
snake1 = Snake("yellow")
print(snake1)
parrot1 = Parrot("green")
print(parrot1)

c1 = Cage(1)
c1.add_animals(wolf1, sheep1)
print(c1)
c2 = Cage(2)
c2.add_animals(snake1, parrot1)
print(c2)
c1.add_animals(snake1)
print(c1)