# Mutable Types as Parameter Defaults: Bad Idea


class HauntedBus:

    def __init__(self, passengers=[]) -> None:
        self.passengers = passengers

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


bus1 = HauntedBus(["Alice", "Bill"])


assert bus1.passengers == ["Alice", "Bill"]

bus1.pick("Charlie")
bus1.drop("Alice")

assert bus1.passengers == ["Bill", "Charlie"]

# bus2 starts empty, so the default empty list is assigned to self.passengers
bus2 = HauntedBus()

bus2.pick("Carrie")

assert bus2.passengers == ["Carrie"]

# bus3 also starts empty, again the default list is assigned.
bus3 = HauntedBus()

assert bus3.passengers == ["Carrie"]

bus3.pick("Dave")

assert bus2.passengers == ["Carrie", "Dave"]

# The problem: bus2.passengers and bus3.passengers refer to the same list.
assert bus2.passengers is bus3.passengers

assert bus1.passengers == ["Bill", "Charlie"]

# So if a default value is a mutable object, and you change it, the change will affect every future call of the function
assert HauntedBus.__init__.__defaults__ == ["Carrie", "Dave"]
