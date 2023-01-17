import numpy 

def convert_bases(input_string: str, input_base, output_base) -> str:
    '''Convert base n to'''
    # Convert to base 10
    input_numbers = input_string.split('_')
    exponent = 0
    base10 = 0
    for digit in input_numbers[::-1]:
        base10 += int(digit) * (input_base ** exponent)
        exponent += 1

    # Assign base10 value to variable for calculations
    carry = base10

    # Create output string
    output = ''
    while carry >= output_base:
        output = f'_{str(carry % output_base)}{output}'
        carry = carry // output_base
    output = f'{str(carry % output_base)}{output}'

    # Function return
    return f'{input_string} in base {input_base} converts to {output} in base {output_base}'

# Output
print(convert_bases('1_0_2_2', numpy.e, numpy.pi))
