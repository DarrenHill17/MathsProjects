from polynomial_calculus import Polynomial
from ln_calculus import Logarithm
import numpy as np

y = Polynomial((1,-5,4,5))
z = Logarithm(y, 3)
print(y.get_coefficients())
print(z.calculate_derivative())
# print(y.calculate_derivative())
# print(y.calculate_integral())

# x = Polynomial.add(y, z)
# print(x)
