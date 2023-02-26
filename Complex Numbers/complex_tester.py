import complex_number as c
from decimal import Decimal

num1 = c.Complex(1,1,c.Complex.INPUT_RECT)

print(c.ComplexMath.power(num1, 2).print_rect())
print(c.ComplexMath.power(num1, 2).print_polar(c.Complex.UNIT_RADIANS))
print(Decimal.from_float(c.ComplexMath.power(num1, 2).get_modulus()))
print(repr(round(c.ComplexMath.power(num1, 2).get_modulus(), 10)))
