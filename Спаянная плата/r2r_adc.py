import RPi.GPIO as GPIO
import time as time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def denit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        bits = [int(b) for b in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, bits)

    def sequential_counting_adc(self):

        '''a=[0,0,0,0,0,0,0,0]
        for i in range(7,-1,-1):
            n=0
            for j in range(7):
                if j==(7-i):
                    n += (2 ** (7 - j))
                else:
                    n+=(2**(7-j))*a[j]'''
        for n in range(256):
            self.number_to_dac(n)
            time.sleep(self.compare_time)
            comp = GPIO.input(self.comp_gpio)
            if comp == 1:
                return n
            else:
                return 255

    def get_sc_voltage(self):
        a=self.sequential_counting_adc()
        b=(a/255)*self.dynamic_range
        return b

if __name__ == "__main__":
    adc = None
    try:
        adc = R2R_ADC(3.3)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"U = {voltage:.3f} В")

    finally:
        if adc is not None:
            adc.denit()