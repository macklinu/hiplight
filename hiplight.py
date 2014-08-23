import os
from pprint import PrettyPrinter
import requests
import RPi.GPIO as GPIO
from status import Status

pp = PrettyPrinter(indent=2)
red = 11
blue = 13
green = 15

def make_request():
  params = {'auth_token': os.environ.get('HIPCHAT_API_TOKEN')}
  return requests.get(url=("https://api.hipchat.com/v2/user/%s" % os.environ.get('HIPCHAT_EMAIL_ADDRESS')), params=params).json()

def setup_pins():
  GPIO.setmode(GPIO.BOARD)

  GPIO.setup(red, GPIO.OUT) #setup all the pins
  GPIO.setup(green, GPIO.OUT)
  GPIO.setup(blue, GPIO.OUT)

  Freq = 100 #Hz

  #setup all the colours
  RED = GPIO.PWM(red, Freq) #Pin, frequency
  RED.start(0) #Initial duty cycle of 0, so off
  GREEN = GPIO.PWM(green, Freq)
  GREEN.start(0)
  BLUE = GPIO.PWM(blue, Freq)
  BLUE.start(0)

def teardown():
  GPIO.cleanup()



if __name__ == '__main__':
    status = Status()
    setup_pins()
    response = make_request()
    status.determine_status(response)
    print status.get_availability()
    try:
        while True:
            i = 0
    except KeyboardInterrupt:
        teardown()
