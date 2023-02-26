import numpy as np

class Polynomial:
    '''Handling polynomials'''

    def __init__(self, input_coefficients: tuple) -> None:
        self.coefficients = tuple(float(i) for i in input_coefficients)

    def __str__(self) -> str:
        output = ''
        for term in enumerate(self.coefficients):
            if term[1] == 0:
                continue
            power = len(self.coefficients) - term[0] - 1
            if term[1] > 0:
                sign = '+'
            else:
                sign = '-'
            output = f'{output}{sign}{abs(term[1])}(x^{power})'
        return output

    def get_coefficients(self) -> tuple:
        '''Returns the coefficients of the polynomial'''
        return self.coefficients

    def calculate_derivative(self, show_working: bool = False) -> tuple:
        '''Use the coefficients of y = (an)x^n + ... + (a2)x^2 + (a1)x +  (a0) to calculate the coefficients of dy/dx'''
        input_coefficients = tuple(reversed(self.coefficients))
        basis_functions_matrix = np.diag(np.array(tuple(range(1,len(input_coefficients)))), k=1)
        input_matrix = np.array(input_coefficients, dtype=float)

        output_matrix = basis_functions_matrix * input_matrix

        if show_working:
            print('Basis Functions Matrix:\n', basis_functions_matrix)
            print('\nInputted Coefficients Matrix:\n', input_matrix)
            print('\nOutput Matrix:\n', output_matrix)

        return tuple(reversed(np.diag(output_matrix, k=1)))

    def calculate_integral(self, integration_constant = 'C', show_working: bool = False) -> tuple:
        '''Use the coefficients of dy/dx = (an)x^n + ... + (a2)x^2 + (a1)x +  (a0) to calculate the coefficients of y'''
        input_coefficients = tuple(reversed(self.coefficients))
        basis_functions_matrix = np.diag(np.array(tuple(range(1,len(input_coefficients) + 1))))
        input_matrix = np.array(input_coefficients, dtype=float)

        output_matrix = (np.linalg.inv(basis_functions_matrix) * input_matrix).astype(float)

        if show_working:
            print('Basis Functions Matrix:\n', basis_functions_matrix)
            print('\nInputted Coefficients Matrix:\n', input_matrix)
            print('\nOutput Matrix:\n', output_matrix)

        output_list = np.diag(output_matrix).tolist()
        output_list.reverse()
        try:
            output_list.append(float(integration_constant))
        except ValueError:
            output_list.append(str(integration_constant))

        return tuple(output_list)

    # @classmethod
    # def add(*polynomials) -> Polynomial:
    #     sum_matrix = np.zeros(len(polynomials))
    #     for i in range(1, len(polynomials)):
    #         print(polynomials[i].get_polynomial())
    #         sum_matrix = sum_matrix + np.array(polynomials[i].get_polynomial(), dtype=float)
    #     return tuple(sum_matrix)

