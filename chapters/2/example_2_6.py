# Cartesian product in a generator expression

from typing import List, Tuple

colors: List[str] = ["black", "white"]
sizes: List[str] = ["S", "M", "L"]

# The generator expression yields items one by one; a list with all six T-shirt variations is never produced in this example.
for tshirt in (f"{c} {s}" for c in colors for s in sizes):
    print(tshirt)
