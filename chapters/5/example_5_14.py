from dataclasses import dataclass, field

# The default_factory parameter lets you provide a function, class, or any other call‐
# able, which will be invoked with zero arguments to build a default value each time an
# instance of the data class is created. This way, each instance of ClubMember will have
# its own list—instead of all instances sharing the same list from the class, which is
# rarely what we want and is often a bug.

@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)