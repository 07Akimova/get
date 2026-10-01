import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class PWM_DAC:
    def __init__ (self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):

        self.gpio_pin = gpio.pin
        self.pwm_frequency = pwm.frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def dec2bin(self, value):
        """Преобразует целое число (0..255) в список из 8 бит (старший бит первый)."""
        return [int(element) for element in bin(value)[2:].zfill(8)]

    def set_number(self, number):
        """Принимает целое число и подаёт его двоичное представление на вход R2R-ЦАП."""
        # Ограничиваем число диапазоном 0..255
        if number < 0:
            number = 0
        elif number > 255:
            number = 255

        bits = self.dec2bin(number)
        GPIO.output(self.gpio_bits, bits)

        if self.verbose:
            print(f"Число на вход ЦАП: {number}, биты: {bits}")


    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            number = 0
        else:
            number = int(voltage / self.dynamic_range * 255)

        self.set_number(number)

if __name__ == "__main__":
    try:
        dac = PWM_DAC (12, 500, 3.290)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
