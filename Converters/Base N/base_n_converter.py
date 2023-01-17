def convert_bases(input_number: str, input_base, output_base) -> str:
    '''Convert base n to'''
    # Convert to base 10
    exponent = 0
    base10 = 0
    for digit in input_number[::-1]:
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
    return f'{input_number} in base {input_base} converts to {output} in base {output_base}'

# Output
print(convert_bases('4216', 7, 2))
