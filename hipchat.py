import os
import requests
from status import Status

class HipChat:
    def __init__(self):
        self.params = {
            'auth_token': os.environ.get('HIPCHAT_API_TOKEN')
        }
        self.url = ("https://api.hipchat.com/v2/user/%s" % os.environ.get('HIPCHAT_EMAIL_ADDRESS'))

    def get_user_status(self):
        response = requests.get(url=self.url, params=self.params).json()
        return Status(response)
