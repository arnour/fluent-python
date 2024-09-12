# duck typing and nominal typing


class Bird:
    pass


# Duck is a subclass of Bird
class Duck(Bird):
    def quack(self):
        print("Quack!")


# alert has no type hints, so the type checker ignores it.
def alert(birdie):
    birdie.quack()


# alert_duck takes one argument of type Duck.
def alert_duck(birdie: Duck) -> None:
    birdie.quack()


# alert_bird takes one argument of type Bird.
# the type hint declares the birdie parameter with type Bird,
# but the body of the function calls birdie.quack()—and
# the Bird class has no such method
def alert_bird(birdie: Bird) -> None:
    birdie.quack()
