import time

import r2r_adc_two
import adc_plot

dynamic_range = 3.3  # динамический диапазон ЦАП, В
duration = 3.0  # продолжительность измерений, с

adc = r2r_adc_two.R2R_ADC(dynamic_range, compare_time=0.001)

voltage_values = []
time_values = []

try:
    start_time = time.time()

    while time.time() - start_time < duration:
        voltage_values.append(adc.get_sar_voltage())
        time_values.append(time.time() - start_time)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()
