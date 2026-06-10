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
    SPACE_REQUIRED = 10


class Wolf(Quadruped):
    SPECIES = "wolf"
    SOUND = "grr"
    SPACE_REQUIRED = 20


class Snake(Legless):
    SPECIES = "snake"
    SOUND = "hiss"
    SPACE_REQUIRED = 5

class Parrot(Biped):
    SPECIES = "parrot"
    SOUND = "tweet"
    SPACE_REQUIRED = 2

class Cage:
    SPACE = 50
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals: list[Animal] = []

    def add_animals(self, *animals):
        """Add one or more animals to the cage. Returns None."""
        for animal in animals:
            remaining = self.SPACE - sum(a.SPACE_REQUIRED for a in self.animals)
            if remaining >= animal.SPACE_REQUIRED:
                self.animals.append(animal)
            else:
                raise ValueError(
                    f"Cannot add {animal}, cage is full."
                )

    def __repr__(self):
        animal_list = ', '.join(str(a) for a in self.animals)
        return f"Cage {self.id_number} ({len(self.animals)} animals): {animal_list}"

class BigCage(Cage):
   SPACE = 100

sheep1 = Sheep("brown")
print(sheep1)
wolf1 = Wolf("gray")
print(wolf1)
snake1 = Snake("yellow")
print(snake1)
parrot1 = Parrot("green")
print(parrot1)
sheep2 = Sheep("brown")
sheep3 = Sheep("brown")
wolf2 = Wolf("gray")
snake2 = Snake("yellow")
bc1 = BigCage(1)
parrot2 = Parrot("green")

c1 = BigCage(1)
print(c1.SPACE)
c1.add_animals(wolf1, sheep1)
print(c1)
c2 = Cage(2)
c2.add_animals(snake1, parrot1)
print(c2)
c1.add_animals(snake1, sheep2)
print(c1)

bc1.add_animals(wolf2, snake2, sheep3, parrot1, snake1, wolf1, sheep2, sheep1)
print(bc1)