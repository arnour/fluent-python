from collections.abc import Callable


def update(probe: Callable[[], float], display: Callable[[float], None]) -> None:
    temperature = probe()
    display(temperature)


def probe_ok() -> int:
    return 42


# display_wrong is not consistent-with Callable[[float], None] because there’s
# no guarantee that a function that expects an int can handle a float;
# for example, Python’s hex function accepts an int but rejects a float.
def display_wrong(temperature: int) -> None:
    print(hex(temperature))


# Mypy flags this line because display_wrong is incompatible with the type hint in the display parameter of update
update(probe_ok, display_wrong)


# display_ok is consistent-with Callable[[float], None] because a function that accepts a complex can also handle a float argument.
def display_ok(temperature: complex):
    print(temperature)


update(probe_ok, display_ok)
