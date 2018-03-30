import operations
from noises import *
from signals import *
import signals_utils as su

# szum_gaussowski(5, 0, 10)
# plot_sin_classic(2, 0.5, 0, 10)
# plot_trojkatny(5, 1, 0.8, 0, 10)

# y_sin = plot_sin_classic(2, 0.5, 0, 10)
# y_prost = plot_prostokatny(5, 1, 0.5, 0, 10)
#
# t = np.arange(0.0, 10.0, 0.01)
# y_sum = operations.add_signals(y_sin, y_prost, t)

# y_sig = plot_sin_classic(1, 1, 0, 1)
## 100 - probkowanie co 0.01 w przedziale (0,1)
# avg = su.calculate_abs_average(0, 100, y_sig)
# abs_avg = su.calculate_abs_average(0, 100, y_sig)
# avg_pow = su.calculate_avg_power(0, 100, y_sig)
# variance = su.calculate_variance(0, 100, y_sig)
# rms = su.calculate_root_mean_square(0, 100, y_sig)
#
# print 'Average:', avg
# print 'Absolute average:', abs_avg
# print 'Average power:', avg_pow
# print 'Variance:', variance
# print 'Root mean square:', rms

y_sig = plot_prostokatny(5, 1, 0.5, 0, 1)
# 100 - probkowanie co 0.01 w przedziale (0,1)
avg = su.calculate_abs_average(0, 100, y_sig)
abs_avg = su.calculate_abs_average(0, 100, y_sig)
avg_pow = su.calculate_avg_power(0, 100, y_sig)
variance = su.calculate_variance(0, 100, y_sig)
rms = su.calculate_root_mean_square(0, 100, y_sig)

print 'Average:', avg
print 'Absolute average:', abs_avg
print 'Average power:', avg_pow
print 'Variance:', variance
print 'Root mean square:', rms
