import os
from pprint import PrettyPrinter

import requests


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


if __name__ == '__main__':
    main()