class Status:
    def __init__(self):
        self.map = {
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
        self.current = None

    def determine_status(self, response):
        if response['presence']:
            presence = response['presence']
            try:
                self.current = self.map[presence['show']]
            except KeyError:
                self.current = self.map[presence['is_online']]

            try:
                self.current['message'] = self.map['status']
            except KeyError:
                self.current['message'] = None
        else:
            self.current = self.map[False]
        return self

    def get_availability(self):
        return self.current['status']

    def get_color(self):
        return self.current['color']
