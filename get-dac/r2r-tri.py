import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    dac = None
    try:
        dac = r2r.R2RDAC(leds=[16, 20, 21, 25, 26, 17, 27, 22],
                         dynamic_range=3.3,
                         verbose=False)

        t = 0.0
        while True:
            voltage = amplitude * sg.get_sin_wave_amplitude(signal_frequency, t)
            dac.set_voltage(voltage)

            sg.wait_for_sampling_period(sampling_frequency)

            t += 1 / sampling_frequency

    finally:
        if dac is not None:
            dac.deinit()