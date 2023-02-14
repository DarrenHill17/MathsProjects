import complex_number as c
import numpy as np


def find_roots(num: c.Complex, power: int) -> tuple[c.Complex]:
    numbers = []
    for k in range(power):
        output = c.Complex(num.get_modulus() ** (1/power), (num.get_angle() + 2 * np.pi * k)/power, c.Complex.INPUT_POLAR)
        numbers.append(output)
    return tuple(numbers)

test_num = c.Complex(16, (2/3)*np.pi, c.Complex.INPUT_POLAR)
test_power = 40

for root in find_roots(test_num, test_power):
    print(root.print_polar(c.Complex.UNIT_RADIANS))
