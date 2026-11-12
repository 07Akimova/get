import time
import RPi.GPIO as GPIO

import mcp3021_driver
import adc_plot

dynamic_range = 5.0   # динамический диапазон АЦП, В (подставь значение с мультиметра)
charge_time = 40.0    # сколько секунд подаём напряжение на 14-й пин, с
duration = 180.0      # продолжительность измерений, с
power_pin = 14        # пин, через который заряжаем конденсатор (нумерация BCM)
sample_period = 0.01  # пауза между измерениями, с

GPIO.setmode(GPIO.BCM)
GPIO.setup(power_pin, GPIO.OUT, initial=GPIO.LOW)

adc = mcp3021_driver.MCP3021(dynamic_range)

voltage_values = []
time_values = []

try:
    GPIO.output(power_pin, GPIO.HIGH)   # подаём напряжение — конденсатор заряжается
    print("Напряжение на 14-м пине подано, идёт заряд...")
    start_time = time.time()
    powered = True

    while time.time() - start_time < duration:
        if powered and time.time() - start_time >= charge_time:
            GPIO.output(power_pin, GPIO.LOW)   # снимаем напряжение — разряд
            powered = False
            print("Напряжение снято, идёт разряд...")

        voltage_values.append(adc.get_voltage())
        time_values.append(time.time() - start_time)
        time.sleep(sample_period)

    print(f"Измерения закончены, точек: {len(time_values)}")

    with open("capacitor_data.txt", "w") as f:
        f.write("t, s\tU, V\n")
        for t, u in zip(time_values, voltage_values):
            f.write(f"{t:.4f}\t{u:.4f}\n")

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)

finally:
    GPIO.output(power_pin, GPIO.LOW)
    GPIO.cleanup()
    adc.deinit()