
class Bowl:
    def __init__(self):
        self.scoops = []

    def add_scoop(self, *scoop: Scoop):
        self.scoops.extend(scoop)

    def __repr__(self) -> str:
        return "\n".join(scoop.flavor for scoop in self.scoops)

class Scoop:
    def __init__(self, flavor: str):
        self.flavor = flavor

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('strawberry')
s4 = Scoop('peanut butter')

b1 = Bowl()
b1.add_scoop(s1, s2, s3)
b1.add_scoop(s4)

print(b1)