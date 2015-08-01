#!/usr/bin/python

import math

# Referenceing parameters by numbered order
print '{0} and {1}'.format('spam', 'eggs')
print '{1} and {0}'.format('spam', 'eggs')

for x in range(1, 11):
    # Referenceing parameters by numbered order
    print '{0:2d} {2:3d} {1:4d}'.format(x, x**3, x**2)

# Referenceing parameters in order passed
print 'We are the {} who say "{}!"'.format('knights', 'Ni')

kargs = dict(food='spam', adjective='absolutely horrible')

# Referenceing parameters by name
print 'This {food} is {adjective}.'.format(food='spam',
                                           adjective='absolutely horrible')
# Exapnding a dictionary into named parameters
print 'This {food} is {adjective}.'.format(**kargs)

# Referncing a dictionary by parameter number
print 'This {0[food]} is {0[adjective]}.'.format(kargs)

# Referncing a dictionary by name
print 'This {dictionary[food]} is {dictionary[adjective]}.'.format(
        dictionary=kargs)

# Showing the difference between the repr of an object, and its str value
print 'The value of PI is approximately {}.'.format(math.pi)
print 'The value of PI is approximately {!r}.'.format(math.pi)

# Fills 5 zeros to the left of the string
print '12'.zfill(5) == "00012"

# Accounts for the negative sign, also the number specified
print '-3.14'.zfill(7) == "-003.14"
# ... and decimals
print '3.14159265359'.zfill(5)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
table = {'{0:7}'.format(key): '{0:10}'.format(value)
         for (key, value) in table.items()}

print table == {
    'Sjoerd ': '      4127',
    'Jack   ': '      4098',
    'Dcab   ': '      7678'
}
