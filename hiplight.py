import os
from pprint import PrettyPrinter
import requests
import RPi.GPIO as GPIO


def main():
    status = {
        True: {
            'status': 'available',
            'color': 'green'
        },
        'xa': {
            'status': 'away',
            'color': 'yellow'
        },
        'dnd': {
            'status': 'do_not_disturb',
            'color': 'red'
        },
        False: {
            'status': 'offline',
            'color': None
        }
    }

    pp = PrettyPrinter(indent=2)

    params = {'auth_token': os.environ.get('HIPCHAT_API_TOKEN')}
    r = requests.get(url=("https://api.hipchat.com/v2/user/%s" % os.environ.get('HIPCHAT_EMAIL_ADDRESS')), params=params).json()

    current = None
    if r['presence']:
        presence = r['presence']
        try:
            current = status[presence['show']]
        except KeyError:
            current = status[presence['is_online']]

        try:
            current['message'] = presence['status']
        except KeyError:
            current['message'] = None
    else:
        current = status[False]

    pp.pprint(current)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, 1)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(13, 1)
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(15, 1)

    try:
        while True:
            GPIO.output(11, 0)
            GPIO.output(11, 1)
            GPIO.output(11, 0)
    except KeyboardInterrupt:
        GPIO.cleanup()



if __name__ == '__main__':
    main()