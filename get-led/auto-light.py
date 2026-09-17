import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led=26
GPIO.setup(led, GPIO.OUT)

button = 6
GPIO.setup(button, GPIO.IN)
state=1
while True:
    state=GPIO.input(button)
    GPIO.output(led, not state)