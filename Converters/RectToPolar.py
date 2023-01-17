import re
import numpy

RE_REGEX = r'z=([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?'
IM_REGEX = r'([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?i'

TEST_NUMBER_SIMPLE = 'z=3+8i'
TEST_NUMBER_WEIRD = 'z=-276.589305+5.878738738526i'

# complex_number = input('Enter a complex number in the form z=a±bi: ')
complex_number = TEST_NUMBER_SIMPLE

# Extracts Re and Im parts using regex
try:
    re_component = float(re.findall(RE_REGEX, complex_number)[0][0])
    im_component = float(re.findall(IM_REGEX, complex_number)[0][0])
except (ValueError, IndexError):
    print('Input is not a valid floating point number, or input formatting is unexpected.')
    exit()

# Find modulus
modulus = (re_component ** 2 + im_component ** 2) ** 0.5

# Print out interpretted number
if im_component < 0:
    print('Intrepretted Number', 'z=%s%si' % (re_component, im_component))
else:
    print('Intrepretted Number', 'z=%s+%si' % (re_component, im_component))


# Print out conjugate
if im_component > 0:
    print('Conjugate', 'z*=%s%si' % (re_component, (-1 * im_component)))
else:
    print('Conjugate', 'z*=%s+%si' % (re_component, (-1 * im_component)))

# Print modulus
print('Modulus', modulus)

# Convert to polar coordinates
angle = numpy.arcsin(im_component / modulus)
print('Polar Coordinates', '%s∠%s' % (modulus, angle))
