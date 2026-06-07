class Animal:
    SPECIES = None
    LEGS = None
    SOUND = None

    def __init__(self, color):
        self.color = color
        self.SPECIES = self.__class__.__name__.lower()

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

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __repr__(self):
        animal_list = '\n\t'.join(str(a) for a in self.animals)
        return f"Cage {self.id_number} ({len(self.animals)} animals, {self._remaining_space()} space left):\n\t{animal_list}"


class BigCage(Cage):
    SPACE = 120


class IncompatibleAnimalError(Exception):
    pass


class CageFullError(Exception):
    pass


class NoColorGivenError(Exception):
    pass


class AnimalNotFoundError(Exception):
    pass


class NoCageAvailableError(Exception):
    pass


class Zoo:
    """A collection of cages."""

    def __init__(self):
        self.cages = []

    def __repr__(self):
        return '\n'.join(str(cage)
                         for cage in self.cages)

    def add_cages(self, *cages):
        self.cages.extend(cages)

    def animals_by_color(self, *colors):
        if not colors:
            raise NoColorGivenError("You must specify at least one color.")
        return [animal for cage in self.cages for animal in cage.animals if animal.color in colors]

    def animals_by_number_of_legs(self, legs):
        return [animal for cage in self.cages for animal in cage.animals if animal.LEGS == legs]

    def animals_by_properties(self, **properties):
        return [animal for cage in self.cages for animal in cage.animals if all(getattr(animal, key) == value for key, value in properties.items())]

    def get_animals(self, **kwargs):
       """Claude on Lerner's"""
        valid = {k: v for k, v in kwargs.items() if k in ('color', 'LEGS')}
        if not valid:
            raise ValueError("Must specify at least one of: color, LEGS")
        return [
            animal
            for cage in self.cages
            for animal in cage.animals
            if all(getattr(animal, key) == value for key, value in valid.items())
        ]

    def number_of_legs(self):
        return f'Number of legs in this zoo = {sum(animal.LEGS for cage in self.cages for animal in cage.animals)}'


    def transfer_animal(self, target_zoo, species):
        """
        Transfers an animal of the specified species from the current zoo's cages
        to the target zoo. Ensures that if no suitable cage in the target zoo is
        found, the animal is returned to its original cage. Raises an error if no
        animal of the specified species is found or if all cages in the target zoo
        are unsuitable.

        :param target_zoo: The zoo instance to which the animal should be transferred.
        :type target_zoo: Zoo
        :param species: The class of the species to be transferred.
        :type species: type
        :raises NoCageAvailableError: If no compatible cage is found in the target
            zoo for the animal.
        :raises AnimalNotFoundError: If no animal of the specified species exists
            in the current zoo.
        """
        for cage in self.cages:
            for animal in cage.animals:
                if isinstance(animal, species):
                    cage.remove_animal(animal)
                    for target_cage in target_zoo.cages:
                        try:
                            target_cage.add_animals(animal)
                            return
                        except (IncompatibleAnimalError, CageFullError):
                            continue
                    # No compatible cage found — put it back
                    cage.add_animals(animal)
                    raise NoCageAvailableError(f"No compatible cage in target zoo for {animal}.")
        raise AnimalNotFoundError(f"No animal of type {species.__name__} found.")


sheep1 = Sheep("brown")
sheep2 = Sheep("black")
sheep3 = Sheep("white")
sheep4 = Sheep("brown")
sheep5 = Sheep("black")
sheep6 = Sheep("white")
sheep7 = Sheep("brown")
sheep8 = Sheep("black")
sheep9 = Sheep("white")
sheep10 = Sheep("brown")
sheep11 = Sheep("black")
sheep12 = Sheep("white")

bc1 = BigCage(1)
bc1.add_animals(sheep1, sheep2, sheep3, sheep4, sheep5, sheep6, sheep7, sheep8, sheep9, sheep10, sheep11, sheep12)
# print(bc1)

wolf1 = Wolf("gray")
wolf2 = Wolf("gray")
wolf3 = Wolf("white")
wolf4 = Wolf("brown")
wolf5 = Wolf("black")
wolf6 = Wolf("white")

bc2 = BigCage(2)
bc2.add_animals(wolf1, wolf2, wolf3, wolf4, wolf5, wolf6)
# print(bc2)

snakes = [Snake("yellow"), Snake("black"), Snake("white"), Snake("red"), Snake("green"), Snake("red, black, white")]
c3 = Cage(3)
c3.add_animals(*snakes)
# print(c3)

parrots = [Parrot("green"), Parrot("red"), Parrot("yellow"), Parrot("black"), Parrot("white"), Parrot("white"),
           Parrot("green"), Parrot("grey")]
c4 = Cage(4)
c4.add_animals(*parrots)
# print(c4)

z1 = Zoo()
z1.add_cages(bc1, bc2, c3, c4)
print(f'Zoo 1:\n{z1}')

z2 = Zoo()
wolfa = Wolf("pink")
wolfb = Wolf("pink")
sheepa = Sheep("pink")
sheepb = Sheep("pink")
ca = BigCage(1)
cb = Cage(2)
ca.add_animals(wolfa, wolfb)
cb.add_animals(sheepa, sheepb)
z2.add_cages(ca, cb)
print(f'Zoo 2:\n{z2}')
z1.transfer_animal(z2, Wolf)
z1.transfer_animal(z2, Sheep)
z1.transfer_animal(z2, Snake)
z1.transfer_animal(z2, Parrot)
print(f'Zoo 1 after transfer:\n{z1}')
print(f'Zoo 2 after transfer:\n{z2}')


print(f'Zoo 2 animals by color "pink":\n{z2.animals_by_properties(color="pink")}'
)

print(f'Zoo 1 animals with 2 legs:\n{z1.animals_by_number_of_legs(2)}'
)
print(z1.animals_by_properties(color="black", LEGS=2))

