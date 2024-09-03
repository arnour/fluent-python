from dataclasses import dataclass, field


@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)  # list[str] means “a list of str.”
    athlete: bool = field(
        default=False, repr=False
    )  # If you want to create an athlete field with a default value of False, and also omit that field from the __repr__ method


m = ClubMember("Arnour", ["Eduardo", "Bruno"], True)

assert str(m) == "ClubMember(name='Arnour', guests=['Eduardo', 'Bruno'])"
