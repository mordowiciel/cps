import operations
from noises import *
from signals import *

# szum_gaussowski(5, 0, 10)
# plot_sin_classic(2, 0.5, 0, 10)
# plot_trojkatny(5, 1, 0.8, 0, 10)

y_sin = plot_sin_classic(2, 0.5, 0, 10)
y_prost = plot_prostokatny(5, 1, 0.5, 0, 10)

t = np.arange(0.0, 10.0, 0.01)
operations.divide_signals(y_sin, y_prost, t)
