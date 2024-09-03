class TwilightBus:

    def __init__(self, passengers) -> None:
        if passengers is None:
            self.passengers = []
        else:
            # However, this assignment makes self.passengers an alias for passengers, which is itself an alias for the actual argument passed to __init__
            self.passengers = passengers

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


basketball_team = ["Sue", "Tina", "Maya", "Diana", "Pat"]

bus = TwilightBus(basketball_team)

bus.drop("Tina")
bus.drop("Pat")

assert basketball_team == ["Sue", "Maya", "Diana"]
