
class Person:
    population = 0

    def __init__(self, name) -> None:
        self.name = name
        Person.population += 1

    def __del__(self):
        Person.population -= 1

    @classmethod
    def get_population(cls) -> int:
        return cls.population

p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person("Charlie")
p4 = Person("Dave")
p5 = Person("Eve")

print(Person.get_population())
print(Person.population)
print(p1.population)
print(Person.population == p1.population == p2.population == p3.population == p4.population == p5.population)
print(Person.population is p1.population is p2.population is p3.population is p4.population is p5.population)
del p1, p2, p3, p4, p5
print(Person.get_population())
print(Person.population)