'''Random Python gibberish to do what numpy already does'''
import re
import numpy

class Complex:
    '''Custom class for working with complex numbers'''
    re_component = None
    im_component = None
    modulus = None
    angle = None

    RECT_REGEX = r'z=([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?i'
    POLAR_REGEX = r'z=([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?(cis|∠)([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?'

    UNIT_RADIANS = 0
    UNIT_DEGREES = 1

    INPUT_RECT = 0
    INPUT_POLAR = 1

    def __init__(self, val_1: float, val_2: float, input_type: int, input_number_string: str = None) -> None:

        # Check for text input, parse if found
        if input_number_string is not None:
            # Check whether input is rectangular or polar
            if len(re.findall(self.RECT_REGEX, input_number_string)) > 0 and len(re.findall(self.RECT_REGEX, input_number_string)[0]) == 4:
                # Initializing the class variables
                self.re_component = float(re.findall(self.RECT_REGEX, input_number_string)[0][0])
                self.im_component = float(re.findall(self.RECT_REGEX, input_number_string)[0][2])
                self.modulus = (self.re_component ** 2 + self.im_component ** 2) ** 0.5
                self.angle = numpy.arcsin(self.im_component / self.modulus)
            elif len(re.findall(self.POLAR_REGEX, input_number_string)) > 0 and len(re.findall(self.POLAR_REGEX, input_number_string)[0]) == 5:
                # Initializing the class variables
                self.modulus = float(re.findall(self.POLAR_REGEX, input_number_string)[0][0])
                self.angle = float(re.findall(self.POLAR_REGEX, input_number_string)[0][3])
                self.re_component = self.modulus * numpy.cos(self.angle)
                self.im_component = self.modulus * numpy.sin(self.angle)
            else:
                print('Text input is invalid')
        # Parse numerical input
        else:
            if input_type == Complex.INPUT_RECT:
                self.re_component = val_1
                self.im_component = val_2
                self.modulus = (self.re_component ** 2 + self.im_component ** 2) ** 0.5
                self.angle = numpy.arcsin(self.im_component / self.modulus)
            elif input_type == Complex.INPUT_POLAR:
                self.modulus = val_1
                self.angle = val_2
                self.re_component = self.modulus * numpy.cos(self.angle)
                self.im_component = self.modulus * numpy.sin(self.angle)
            else:
                print('Input type is invalid')

        # Normalize angle to: -pi < angle <= pi
        self.angle = self.normalize_angle(self.angle)

    def get_re_component(self) -> float:
        '''Returns the Re(number)'''
        return self.re_component

    def get_im_component(self) -> float:
        '''Returns the Im(number)'''
        return self.im_component

    def get_modulus(self) -> float:
        '''Return the modulus of the number'''
        return self.modulus

    def get_angle(self) -> float:
        '''Return the polar angle of the number'''
        return self.angle

    def normalize_angle(self, angle: float) -> float:
        '''Normalize input angles to -pi < angle <= pi'''
        if angle <= -1 * numpy.pi:
            while angle <= -1 * numpy.pi:
                angle += 2 * numpy.pi
        elif angle > numpy.pi:
            while angle > numpy.pi:
                angle -= 2 * numpy.pi
        return angle
    
    def print(self, angle_unit: int) -> str:
        '''Rectangular and polar print statement'''
        if angle_unit == Complex.UNIT_RADIANS:
            return_angle = self.angle
        else:
            return_angle = self.angle * (180 / numpy.pi)
        if self.im_component < 0:
            return f'z={self.re_component}{self.im_component}i\nz={self.modulus}∠{return_angle}'
        return f'z={self.re_component}+{self.im_component}i\nz={self.modulus}∠{return_angle}'

    def print_polar(self, angle_unit: int) -> str:
        '''{Polar print statement'''
        if angle_unit == Complex.UNIT_RADIANS:
            return_angle = self.angle
        else:
            return_angle = self.angle * (180 / numpy.pi)
        if self.im_component < 0:
            return f'z={self.modulus}∠{return_angle}'
        else:
            return f'z={self.modulus}∠{return_angle}'

    def print_rect(self) -> str:
        '''Rectangular print statement'''
        if self.im_component < 0:
            return f'z={self.re_component}{self.im_component}i'
        else:
            return f'z={self.re_component}+{self.im_component}i'

class ComplexMath:
    '''Custom class for doing maths with complex numbers'''
    @staticmethod
    def add(*nums: Complex) -> Complex:
        '''Adds n complex numbers'''
        re_sum = 0
        im_sum = 0
        for num in nums:
            re_sum += num.get_re_component()
            im_sum += num.get_im_component()
        return Complex(re_sum, im_sum, Complex.INPUT_RECT)

    @staticmethod
    def subtract(*nums: Complex) -> Complex:
        '''Subtracts n complex numbers'''
        re_sum = nums[0].get_re_component()
        im_sum = nums[0].get_im_component()
        for num in nums[1:]:
            re_sum -= num.get_re_component()
            im_sum -= num.get_im_component()
        return Complex(re_sum, im_sum, Complex.INPUT_RECT)

    @staticmethod
    def multiply(num1: Complex, num2: Complex) -> Complex:
        '''Multiplies 2 complex numbers'''
        re_sum = num1.get_re_component() * num2.get_re_component() - num1.get_im_component() * num2.get_im_component()
        im_sum = num1.get_re_component() * num2.get_im_component() + num1.get_im_component() * num2.get_re_component()
        return Complex(re_sum, im_sum, Complex.INPUT_RECT)

    @staticmethod
    def divide(num1: Complex, num2: Complex) -> Complex:
        '''Divides 2 complex numbers'''
        # Check to prevent any weird behaviour in divison, such as 0.9999999999999991
        re_term_numerator = (num1.get_re_component() * num2.get_re_component() + num1.get_im_component() * num2.get_im_component())
        im_term_numerator = (num1.get_im_component() * num2.get_re_component() - num1.get_re_component() * num2.get_im_component())
        denominator =  (num2.get_re_component() ** 2 + num2.get_im_component() ** 2)
        if float(re_term_numerator).is_integer() and float(im_term_numerator).is_integer() and float(denominator).is_integer():
            return Complex(re_term_numerator/ denominator, im_term_numerator / denominator, Complex.INPUT_RECT)

        # Number is not in the form x/y where x and y in R, thus use the quick method
        return Complex(num1.get_modulus() / num2.get_modulus(), num1.get_angle() - num2.get_angle(), Complex.INPUT_POLAR)

    @staticmethod
    def power(num: Complex, exponent: float) -> Complex:
        '''Raises a complex number to a float exponent'''
        return Complex(num.get_modulus() ** exponent, num.get_angle() * exponent, Complex.INPUT_POLAR)

    @staticmethod
    def find_roots(num: Complex, power: int) -> tuple[Complex]:
        '''Calculates the roots of the equation x^n=a+bi using De Moivre's Theorem'''
        numbers = []
        for k in range(power):
            output = Complex(num.get_modulus() ** (1/power), (num.get_angle() + 2 * numpy.pi * k)/power, Complex.INPUT_POLAR)
            numbers.append(output)
        return tuple(numbers)
