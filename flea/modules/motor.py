from RPi import GPIO
from ..utils import directions


def setup_motors(motors):
    for _, p in motors.items():
        GPIO.setup(p, GPIO.OUT)


def drive(motors, direction):
    # TODO: NOT IMPLEMENTED YET
    pass
