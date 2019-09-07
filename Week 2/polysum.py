'''
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is:  0.25∗n∗s2tan(π/n) 
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter 
of the regular polygon. The function returns the sum, rounded to 4 decimal places.
'''

import math

def polysum(n,s):
    area = 0.25*n*(s**2) / math.tan(math.pi/n)
    perimeter = n*s
    polysum = area+(perimeter**2)
    return float('{:.4f}'.format(polysum))

print(polysum(34,20))
