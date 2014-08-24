import time
from pins import Pins
from hipchat import HipChat

if __name__ == '__main__':
    pins = Pins()
    hipchat = HipChat()

    pins.setup()

    try:
        while True:
            status = hipchat.get_user_status()
            pins.set_color(status.get_color())
            time.sleep(5)
    except KeyboardInterrupt:
        pins.teardown()
