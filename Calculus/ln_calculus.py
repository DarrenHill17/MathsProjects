import numpy as np
from polynomial_calculus import Polynomial

class Logarithm:
    '''Handles equations in the form y = log(a,b)'''

    def __init__(self, function, base: float = 10) -> None:
        self.function = function
        self.base = base

    def calculate_derivative(self) -> tuple:
        '''Return the derivative of the function y = log(a,b)'''

        # Derivative of y = ln|f(x)| -> dy/dx = f'(x)/f(x)
        if self.base == np.e:
            if isinstance(self.function, Polynomial):
                return ((self.function.calculate_derivative()), self.function.get_coefficients())
        
        # Derivative of y = log(a,f(x)) -> dy/dx = f'(x)/[ln(a)*f(x)]
        else:
            if isinstance(self.function, Polynomial):
                return ((self.function.calculate_derivative()), tuple(np.log(self.base) * coefficient for coefficient in self.function.get_coefficients()))
        return (0,0,0)
