class Animal:
    SPECIES = None
    LEGS = None
    SOUND = None

    def __init__(self, color):
        self.color = color
        self.species = self.__class__.__name__.lower()

    def __repr__(self):
        return f"{self.SOUND} {self.color} {self.SPECIES} {self.LEGS} legs"


class Quadruped(Animal):
    LEGS = 4


class Biped(Animal):
    LEGS = 2


class Legless(Animal):
    LEGS = 0


class Sheep(Quadruped):
    SOUND = "baa"
    SPACE_REQUIRED = 10


class Wolf(Quadruped):
    SOUND = "grr"
    SPACE_REQUIRED = 20


class Snake(Legless):
    SOUND = "hiss"
    SPACE_REQUIRED = 5


class Parrot(Biped):
    SOUND = "tweet"
    SPACE_REQUIRED = 2


COMPATIBILITY = {
    Sheep: [Sheep, Parrot, Snake],
    Wolf: [Wolf, Snake],
    Snake: [Snake, Sheep, Wolf],
    Parrot: [Parrot, Sheep]
}


class Cage:
    SPACE = 50

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals: list[Animal] = []

    def add_animals(self, *animals):
        """Add one or more animals to the cage. Returns None."""
        for animal in animals:
            for resident in self.animals:
                if type(animal) not in COMPATIBILITY.get(type(resident), []):
                    raise IncompatibleAnimalError(
                        f"Cannot add {type(animal).__name__}, incompatible with resident {type(resident).__name__}.")
            if animal.SPACE_REQUIRED > self._remaining_space():
                raise CageFullError(f"Cannot add {type(animal).__name__}, cage is full.")
            self.animals.append(animal)

    def _remaining_space(self):
        return self.SPACE - sum(a.SPACE_REQUIRED for a in self.animals)

    def __repr__(self):
        animal_list = '\n\t'.join(str(a) for a in self.animals)
        return f"Cage {self.id_number} ({len(self.animals)} animals, {self._remaining_space()} space left):\n\t{animal_list}"


class BigCage(Cage):
    SPACE = 100


class IncompatibleAnimalError(Exception):
    pass


class CageFullError(Exception):
    pass


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
c1.add_animals(wolf1, wolf2, snake1)
print(c1)
c2 = Cage(2)
c2.add_animals(snake1, parrot1)
print(c2)
c1.add_animals(snake1, sheep2)
print(c1)

bc1.add_animals(wolf2, snake2, sheep3, parrot1, snake1, wolf1, sheep2, sheep1)
print(bc1)
