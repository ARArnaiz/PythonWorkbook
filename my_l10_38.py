
class Scoop:
    def __init__(self, flavor: str):
        self.flavor = flavor

    def __str__(self) -> str:
        return f"Scoop('{self.flavor}')"

def scoops(flavor1: str, flavor2: str, flavor3: str) -> list[Scoop]:
    return [Scoop(flavor) for flavor in (flavor1, flavor2, flavor3)]



s1, s2, s3 = scoops("vanilla", "chocolate", "strawberry")
for scoop in (s1, s2, s3):
    print(scoop, scoop.flavor)

s4 = Scoop("peanut butter")
print(s4, s4.flavor)