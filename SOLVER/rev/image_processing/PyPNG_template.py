#!/usr/bin/env python3

import png


import numpy as np

# The following import is just for creating an interesting array
# of data.  It is not necessary for writing a PNG file with PyPNG.
from scipy.ndimage import gaussian_filter


# Make an image in a numpy array for this demonstration.
nrows = 3
ncols = 2

s = ['110010010011',
     '101011010100',
     '110010110101',
     '100010010011']
s = map(lambda x: map(int, x), s)


x = [3, 4, 5]
# y is our floating point demonstration data.
y = [0x55, 0x34]

# Use pypng to write z as a color PNG.
f = open('foo_color.png', 'wb')
writer = png.Writer(len(s[0]), len(s))
writer.write(f, s)
f.close()