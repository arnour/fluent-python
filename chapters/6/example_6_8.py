# Deep and Shallow Copies of Arbitrary Objects
import copy


class Bus:

    def __init__(self, passengers=None) -> None:
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


bus1 = Bus(["Alice", "Bill", "Claire", "David"])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

assert bus1 is not bus2 and bus2 is not bus3

bus1.drop("Bill")

assert bus2.passengers == ["Alice", "Claire", "David"]

assert bus1.passengers is bus2.passengers

# bus3 is a deep copy of bus1, so its passengers attribute refers to another list
assert bus3.passengers == ["Alice", "Bill", "Claire", "David"]
