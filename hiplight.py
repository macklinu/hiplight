from pins import Pins
from hipchat import HipChat

def scale(value):
    return (((value - 0) * (0 - 100)) / (255 - 0)) + 100

if __name__ == '__main__':
    pins = Pins()
    hipchat = HipChat()

    pins.setup()
    # status = hipchat.get_user_status()
    # pins.set_color(status.get_color())

    try:
        while True:
            response = raw_input("RBG: ").split()
            floats = map(float, response)
            colors = map(scale, floats)
            print colors
            if len(colors) == 3:
                pins.set_color(colors)
    except KeyboardInterrupt:
        pins.teardown()
