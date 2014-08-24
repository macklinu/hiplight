class Status:
    def __init__(self, json_response):
        self.current = None
        self.options = {
            True: {
                'status': 'available',
                'color': '0 255 0'
            },
            'xa': {
                'status': 'away',
                'color': '255 255 0'
            },
            'dnd': {
                'status': 'do_not_disturb',
                'color': '255 0 0'
            },
            False: {
                'status': 'offline',
                'color': '0 0 0'
            }
        }
        self.determine_status(json_response)

    def determine_status(self, response):
        if response['presence']:
            presence = response['presence']
            try:
                self.current = self.options[presence['show']]
            except KeyError:
                self.current = self.options[presence['is_online']]

            try:
                self.current['message'] = self.options['status']
            except KeyError:
                self.current['message'] = None
        else:
            self.current = self.options[False]
            
    def get_color(self):
        return self.current['color']
