import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200)  # объект управления ШИМ-сигналом на GPIO выходе
duty = 0.0  # переменная, хранязая текущий коэффициент заполнения
pwm.start(duty)  # генерация ШИМ-сигнала на GPIO выходе

while True:
    pwm.ChangeDutyCycle(duty)  # генерация ШИМ-сигнала на GPIO
    time.sleep(0.05)

    duty += 1.0
    if duty > 100.0:
        duty = 0.0