import time

import mcp3021_driver
import adc_plot

dynamic_range = 5.0   # динамический диапазон АЦП, В (подставь значение с мультиметра)
duration = 3.0        # продолжительность измерений, с

adc = mcp3021_driver.MCP3021(dynamic_range)

voltage_values = []
time_values = []

try:
    start_time = time.time()

    while time.time() - start_time < duration:
        voltage_values.append(adc.get_voltage())
        time_values.append(time.time() - start_time)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()