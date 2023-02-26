from polynomial_calculus import Polynomial as p

# print('\nDerivative Coefficients:\n', calculate_derivative((1,5,4,5)))
# print('\nIntegral Coefficients:\n', calculate_integral((3,10,4)))

print(p.calculate_integral(p.calculate_derivative(input_coefficients=(1,5,4,5)), 5))
