# Используюя numpy вычислить среднее арифметическое для 100 случайных числе.

import numpy as np
from numpy import array
from numpy.random import seed
from numpy.random import rand

seed(3)
values = array(rand(100))
print(np.mean(values))
