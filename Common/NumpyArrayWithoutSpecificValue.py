#%% https://stackoverflow.com/a/55472364/4510954

import numpy as np
a = np.arange(-5,6)
b = np.where([np.arange(-5,6) != 0])[1]
c = numpy.where(numpy.in1d(a, [0]))
d = random.choice(list(numpy.select([a != 0, a == 0], [a, -1])))
# to generate matrix 5 x 5:
e = np.random.choice(list(numpy.select([a != 0, a == 0], [a, -1])), (5, 5))
