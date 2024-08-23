# Pattern Matching with Sequences
from typing import List
from time import sleep

class InvalidCommand(Exception):
    pass


class Led:
    def __init__(self, ident, intensity, red, green, blue) -> None:
        self.ident = ident
        self.intensity = intensity
        self.color = (red, green, blue)

    def set_brightness(self, ident, intensity) -> None:
        self.ident = ident
        self.intensity = intensity
        print('Setting brightness')
        
    def set_color(self, ident, red, green, blue)-> None:
        self.ident = ident
        self.color = (red, green, blue)
        print('Setting color')

class Robot:

    def __init__(self) -> None:
        self.leds = (
            Led(0, 0, 1, 2, 3),
            Led(1, 1, 3, 5, 6),
            Led(2, 1, 6, 8, 9)
        )

    def handle_command(self, message) -> None:
        match message:
            case ["BEEPER", float(frequency), int(times)]:
                self.beep(times, frequency)
            case ["NECK", int(angle)]:
                self.rotate_neck(angle)
            case ["LED", ident, intensity]:
                self.leds[ident].set_brightness(ident, intensity)
            case ["LED", ident, red, green, blue]:
                self.leds[ident].set_color(ident, red, green, blue)
            case _:
                raise InvalidCommand(message)

    def beep(self, times, frequency) -> None:
        for _ in range(times):
            print('Beeping...')
            sleep(frequency)

    def rotate_neck(self, angle: int) -> None:
        print(f'Neck rotated in {angle} degrees')

robot = Robot()

robot.handle_command(['BEEPER', 0.1, 3])
robot.handle_command(['NECK', 90])
robot.handle_command(['LED', 2, 40])
robot.handle_command(['LED', 2, 5, 6, 7])
robot.handle_command(['WALK', 40])