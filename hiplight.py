from pins import Pins
from hipchat import HipChat

if __name__ == '__main__':
    pins = Pins()
    hipchat = HipChat()

    pins.setup()
    status = hipchat.get_user_status()
    pins.set_color(status.get_color())

    try:
        while True:
            i = 0
    except KeyboardInterrupt:
        pins.teardown()
