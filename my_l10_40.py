class Bowl:
    """Represents an ice cream bowl with a limited number of scoops."""

    max_scoops = 3  # Maximum number of scoops allowed in a single bowl

    def __init__(self) -> None:
        """Initialize an empty bowl."""
        self.scoops: list[Scoop] = []

    def add_scoops(self, *scoops: Scoop):
        """Add one or more scoops to the bowl.

        Args:
            *scoops: One or more Scoop instances to add.

        Raises:
            ValueError: If adding the scoops would exceed the maximum allowed.
        """
        if len(self.scoops) + len(scoops) > Bowl.max_scoops:
            raise ValueError(
                f"Cannot add {len(scoops)} scoops: bowl already has "
                f"{len(self.scoops)}/{self.max_scoops}."
            )
        self.scoops.extend(scoops)

    def __repr__(self) -> str:
        """Return a string listing each scoop's flavor, one per line."""
        return "\n".join(scoop.flavor for scoop in self.scoops)


class Scoop:
    """Represents a single scoop of ice cream with a given flavor."""

    def __init__(self, flavor: str):
        """Initialize a scoop with the specified flavor.

        Args:
            flavor: A string describing the ice cream flavor.
        """
        self.flavor = flavor


# --- Create individual scoops ---
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('strawberry')
s4 = Scoop('peanut butter')  # This scoop will exceed the bowl limit

# --- Demonstrate bowl capacity enforcement ---
b1 = Bowl()
b1.add_scoops(s1, s2, s3)  # Fills the bowl to max_scoops (3)
b1.add_scoops(s4)           # Raises ValueError: bowl is already full

print(b1)