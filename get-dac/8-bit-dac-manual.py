import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = [16, 20, 21,25, 26, 17, 27, 22]

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)
dynamic_range=3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range: .2f} B)")
        print("Устанавливаем 0.0 B")
        return 0

    return int(voltage / dynamic_range * 255)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


def number_to_dac(number):
    GPIO.output(leds, dec2bin(number))
    a=dec2bin(number)
    b=a[0]*(2**7)+a[1]*(2**6)+a[2]*(2**5)+a[3]*(2**4)+a[4]*(2**3)+a[5]*(2**2)+a[6]*(2)+a[7]
    print("Число на вход ЦАП: ", b, "биты:", a)


try: 
    while True:
        try:
            voltage = float (input("Введите напряжение в Вольтах: "))
            number = voltage_to_number (voltage)
            number_to_dac (number)

        except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()


