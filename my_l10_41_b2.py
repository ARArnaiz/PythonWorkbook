class Phone:

    def __init__(self, number):
        self.number = number

    def dial(self, number) -> str:
        return f"Dialing {number} from {self.number}..."


class SmartPhone(Phone):

    def __init__(self, number, os):
        super().__init__(number)
        self.os = os

    def run_app(self, app) -> str:
        return f"Running {app} on {self.os}..."


class iPhone(SmartPhone):
    # No __init__ needed — inherits SmartPhone's cleanly

    def run_app(self, app) -> str:
        return super().run_app(app).lower()

    def dial(self, number) -> str:
        return super().dial(number).lower()

# Phone
p = Phone("206-555-0100")
assert p.dial("800-555-0199") == "Dialing 800-555-0199 from 206-555-0100..."
print(p.dial("800-555-0199"))
# SmartPhone — inherits dial, adds run_app
sp = SmartPhone("425-319-3072", "Android")
assert "800-555-0199" in sp.dial("800-555-0199")   # inherited
print(sp.dial("800-555-0199"))
assert sp.run_app("Maps") == "Running Maps on Android..."
print(sp.run_app("Maps"))
# iPhone — both methods lowercased
ip = iPhone("425-891-7941", "iOS")
assert ip.dial("800-555-0199") == ip.dial("800-555-0199").lower()   # all lowercase
print(ip.dial("800-555-0199"))
assert ip.run_app("Safari") == "running safari on ios..."           # all lowercase
print(ip.run_app("Safari"))
assert "safari" in ip.run_app("Safari")

# MRO sanity — isinstance checks
assert isinstance(ip, iPhone)
assert isinstance(ip, SmartPhone)
assert isinstance(ip, Phone)