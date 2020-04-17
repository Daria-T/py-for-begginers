# Используюя numpy вычислить сумму ряда 0 - input()

import numpy as np
right_border = int(input('Введите верхнюю границу диапозона: '))
values = np.array(range(right_border + 1))
print(np.sum(values))
