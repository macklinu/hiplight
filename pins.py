import RPi.GPIO as GPIO

class Pins(object):
    def __init__(self):
        self.red_pin = 11
        self.green_pin = 13
        self.blue_pin = 15
        self.frequency = 100

    def setup(self):
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)

        self.red = GPIO.PWM(self.red_pin, self.frequency)
        self.green = GPIO.PWM(self.green_pin, self.frequency)
        self.blue = GPIO.PWM(self.blue_pin, self.frequency)

        self.set_color('0 0 0')

    def set_color(self, color_string):
        try:
            colors = self.check_color_string(color_string)
            self.red.start(colors[0])
            self.green.start(colors[1])
            self.blue.start(colors[2])
        except InvalidColorStringException:
            print 'invalid color string'

    def check_color_string(self, color_string):
        values = map(float, color_string.split())
        colors = map(self.scale, values)
        if len(colors) == 3:
            return colors
        else:
            raise InvalidColorStringException

    def scale(self, value):
        return (((value - 0) * (0 - 100)) / (255 - 0)) + 100

    def teardown(self):
        GPIO.cleanup()



class InvalidColorStringException(Exception):
    pass
