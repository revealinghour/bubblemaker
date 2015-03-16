import time
import RPi.GPIO as GPIO
import serial
from twython import TwythonStreamer

# Search terms
TERMS = '#puneiot'
ser = serial.Serial('/dev/ttyACM0', 9600)
# GPIO pin number of LED
LED = 22

# Twitter application authentication
APP_KEY = 'w7ayHY159gIzVBqgWnDbWI60x'
APP_SECRET = 'OoUwFZz6rR2PLlUUHZweWCjezm61wJJb9DJXlMkJN8YC7E1GIa'
OAUTH_TOKEN = '2835817897-JrMiN9yIjDuZ302gHiXHBESnHoibtZgW4GqLkje'
OAUTH_TOKEN_SECRET = '2uvpLHlXcOHMXfrknfif5wOJzDApNcwgmIpNz4AYwXQfu'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
 			print '-'
			ser.write('a')
			

# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()


