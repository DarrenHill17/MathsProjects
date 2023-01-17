import re
import numpy

MODULUS_REGEX = r'z=([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?'
ANGLE_REGEX = r'(cis|∠)([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?'

TEST_NUMBER = 'z=8.54400374531753∠1.2120256565243244'

complex_number = TEST_NUMBER


# Extracts Re and Im parts using regex
try:
    modulus = float(re.findall(MODULUS_REGEX, complex_number)[0][0])
    angle = float(re.findall(ANGLE_REGEX, complex_number)[0][1])
except (ValueError, IndexError):
    print('Input is not a valid floating point number, or input formatting is unexpected.')
    exit()

# Convert to rectangular coordinates
re_component = modulus * numpy.cos(angle)
im_component = modulus * numpy.sin(angle)

# Print out interpretted number
print('Interpretted Number', '%s∠%s' % (modulus, angle))

# Print out rectangular form
if im_component < 0:
    print('Rectangular Form', 'z=%s%si' % (re_component, im_component))
else:
    print('Rectangular Form', 'z=%s+%si' % (re_component, im_component))