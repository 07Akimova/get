import mcp4725_driver as mcp
import time
import time

import r2r_adc
import adc_plot

dynamic_range = 3.3   # динамический диапазон ЦАП, В
duration = 10.0        # продолжительность измерений, с

adc = r2r_adc.R2R_ADC(dynamic_range, compare_time=0.0001)

voltage_values = []
time_values = []


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    dac = None
    try:
        dac = mcp.MCP4725(dynamic_range=3.3, address=0x61, verbose=False)

        t = 0.0
        while True:
            voltage = amplitude
            dac.set_voltage(voltage)

            time.sleep(10)
            start_time = time.time()

            while time.time() - start_time < duration:
                voltage_values.append(adc.get_sc_voltage())
                time_values.append(time.time() - start_time)

            adc_plot.plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
            adc_plot.plot_sampling_period_hist(time_values)


    finally:
        if dac is not None:
            dac.deinit()
        if adc is not None:
            adc.deinit()





