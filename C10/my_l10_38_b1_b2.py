
class Beverage:

    def __init__(self, name: str, temperature: float = 75.0):
        self.name = name
        self.temperature = temperature

    def __str__(self) -> str:
        return f"Beverage('{self.name}', {self.temperature})"

b1 = Beverage("Espresso", 93.3)
print(b1)
print(b1.name)
print(b1.temperature)

b2 = Beverage("Black tea", 100.0)
print(b2)
print(b2.name)
print(b2.temperature)

b3 = Beverage("Hot chocolate")
print(b3)
print(b3.name)
print(b3.temperature)