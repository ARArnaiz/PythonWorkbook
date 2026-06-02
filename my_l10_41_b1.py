class InsufficientPostageError(Exception):
    pass
class AlreadyMailedError(Exception):
    pass

class Envelope:
    postage_rate = 10

    def __init__(self, weight: float):
        self.weight = weight
        self.sent = False
        self.postage = 0

    def send(self):
        if self.sent:
            raise AlreadyMailedError("This envelope has already been sent.")
        if self.postage < self.postage_needed():
            raise  InsufficientPostageError("Insufficient postage for this envelope.")
        self.sent = True

    def add_postage(self, postage: float):
        self.postage += postage

    def postage_needed(self) -> float:
        return self.weight * self.postage_rate


class BigEnvelope(Envelope):
    postage_rate = 15


e1 = Envelope(10)
print(e1.weight, e1.sent, e1.postage)
e1.add_postage(99)
e1.add_postage(1)
print(e1.weight, e1.sent, e1.postage)
print(e1.postage_needed())
e1.send()
print(e1.weight, e1.sent, e1.postage)

e2 = BigEnvelope(30)
print(e2.weight, e2.sent, e2.postage)
e2.add_postage(449)
e2.add_postage(1)
print(e2.weight, e2.sent, e2.postage)
print(e2.postage_needed())
e2.send()
print(e2.weight, e2.sent, e2.postage)
# e2.send()
