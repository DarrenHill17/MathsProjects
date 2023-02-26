import numpy as np

class Polynomial:
    '''Handling the calculus of polynomials'''
    @staticmethod
    def calculate_derivative(input_coefficients: tuple, show_working: bool = False) -> tuple:
        '''Input the coefficients of y = (an)x^n + ... + (a2)x^2 + (a1)x +  (a0) to calculate the coefficients of dy/dx'''
        input_coefficients = tuple(reversed(input_coefficients))
        basis_functions_matrix = np.diag(np.array(tuple(range(1,len(input_coefficients)))), k=1)
        input_matrix = np.array(input_coefficients, dtype=float)

        output_matrix = basis_functions_matrix * input_matrix

        if show_working:
            print('Basis Functions Matrix:\n', basis_functions_matrix)
            print('\nInputted Coefficients Matrix:\n', input_matrix)
            print('\nOutput Matrix:\n', output_matrix)

        return tuple(reversed(np.diag(output_matrix, k=1)))

    @staticmethod
    def calculate_integral(input_coefficients: tuple, integration_constant = 'c', show_working: bool = False) -> tuple:
        '''Input the coefficients of dy/dx = (an)x^n + ... + (a2)x^2 + (a1)x +  (a0) to calculate the coefficients of y'''
        input_coefficients = tuple(reversed(input_coefficients))
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
            output_list.append(integration_constant)

        return tuple(output_list)
