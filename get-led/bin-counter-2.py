import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

up = 9
down = 10

GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

num = 0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2
while True:
    if GPIO.input(up):
        num = num + 1
    	print(num, dec2bin(num))
    	time.sleep(sleep_time)
	if GPIO.input(down):
		num = num - 1
    	print(num, dec2bin(num))
    	time.sleep(sleep_time)
	if (num<0 or num>63):
		num=0
    for i in range(len(leds)):
		chisla=dec2bin(num)
		if chisla[i]==0:
			GPIO.output(leds[i], 0)
		else:
			GPIO.output(leds[i], 1)

	#GPIO.output(leds, dec2bin(num))
