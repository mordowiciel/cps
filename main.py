import signal_generator
import noise_generator
import plot_utils

signal_generator.init_first_app_state()

sig_gauss = noise_generator.gaussian(5, 0, 10, 100)
plot_utils.plot_signal(sig_gauss, 'Uniform test')
