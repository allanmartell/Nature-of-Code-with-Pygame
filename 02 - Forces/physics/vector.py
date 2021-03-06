# An Eucledean Vector Class in pure Python

# URL: https://gist.github.com/mcleonard/5351452

"""
The MIT License (MIT)
Copyright (c) 2015 Mat Leonard
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import math, random

class Vector(object):
    def __init__(self, *args):
        """ Create a vector, example: v = Vector(1,2) """
        if len(args)==0: self.values = (0,0)
        else: self.values = args

    def norm(self):
        """ Returns the norm (length, magnitude) of the vector """
        return math.sqrt(sum( comp**2 for comp in self ))

    def argument(self):
        """ Returns the argument of the vector, the angle clockwise from +y."""
        arg_in_rad = math.acos(Vector(0,1)*self/self.norm())
        arg_in_deg = math.degrees(arg_in_rad)
        if self.values[0]<0: return 360 - arg_in_deg
        else: return arg_in_deg

    def normalize(self):
        """ Returns a normalized unit vector """
        norm = self.norm()
        normed = tuple( comp/norm for comp in self )
        return Vector(*normed)

    def rotate(self, *args):
        """ Rotate this vector. If passed a number, assumes this is a
            2D vector and rotates by the passed value in degrees.  Otherwise,
            assumes the passed value is a list acting as a matrix which rotates the vector.
        """
        if len(args)==1 and type(args[0]) == type(1) or type(args[0]) == type(1.):
            # So, if rotate is passed an int or a float...
            if len(self) != 2:
                raise ValueError("Rotation axis not defined for greater than 2D vector")
            return self._rotate2D(*args)
        elif len(args)==1:
            matrix = args[0]
            if not all(len(row) == len(v) for row in matrix) or not len(matrix)==len(self):
                raise ValueError("Rotation matrix must be square and same dimensions as vector")
            return self.matrix_mult(matrix)

    def _rotate2D(self, theta):
        """ Rotate this vector by theta in degrees.

            Returns a new vector.
        """
        theta = math.radians(theta)
        # Just applying the 2D rotation matrix
        dc, ds = math.cos(theta), math.sin(theta)
        x, y = self.values
        x, y = dc*x - ds*y, ds*x + dc*y
        return Vector(x, y)

    def matrix_mult(self, matrix):
        """ Multiply this vector by a matrix.  Assuming matrix is a list of lists.

            Example:
            mat = [[1,2,3],[-1,0,1],[3,4,5]]
            Vector(1,2,3).matrix_mult(mat) ->  (14, 2, 26)

        """
        if not all(len(row) == len(self) for row in matrix):
            raise ValueError('Matrix must match vector dimensions')

        # Grab a row from the matrix, make it a Vector, take the dot product,
        # and store it as the first component
        product = tuple(Vector(*row)*self for row in matrix)

        return Vector(*product)

    def inner(self, other):
        """ Returns the dot product (inner product) of self and other vector
        """
        return sum(a * b for a, b in zip(self, other))

    def __mul__(self, other):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if type(other) == type(self):
            return self.inner(other)
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple( a * other for a in self )
            return Vector(*product)

    def __rmul__(self, other):
        """ Called if 4*self for instance """
        return self.__mul__(other)

    def __div__(self, other):
        if type(other) == type(1) or type(other) == type(1.0):
            divided = tuple( a / other for a in self )
            return Vector(*divided)

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        added = tuple( a + b for a, b in zip(self, other) )
        return Vector(*added)

    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        subbed = tuple( a - b for a, b in zip(self, other) )
        return Vector(*subbed)

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self):
        return str(self.values)


# Allan Martell's expansion of Mat Leonard's vector class (2020).
# Licensed under the same MIT lisence as the original vector class.
# The subclass PVector here takes the name from the eponymous class
# from processing (https://processing.org/) which is written in Java

# NOTE: all methods that returns vectors must return a PVector
#       than a Vector object

class PVector(Vector):

    def __init__(self, *args):
        """ Create a vector, example: v = Vector(1,2)
            values must be a list so that attributes
            can be updated after class has been called"""
        if len(args)==0: self.values = (0,0)
        else:
            self.values = args
            self.values = list(self.values)

    def mag(self):
        """ A vector's magnitude it's the distance between the origin
            (0,0) and it's current location (x,y). The Pythagoras'
            theorem calculates this. Called norm in parent class"""
        return math.sqrt(sum((val*val for val in self)))

    def normalize(self):
        """ Returns a normalized unit vector """
        m = self.mag()
        if m != 0: # only works if magnitude is not 0
            normed = tuple( comp/m for comp in self )
            return PVector(*normed)
        else:
            return self # return 0 vector

    def limit(self, max):
        """ Check the magnitude of self. If less than max, return the latter.
            If magnitude is more than max, return a new PVector whose magnitude
            is equal to max."""
        m = self.mag()
        if m <= max:
            return self
        elif m > max:
            return self.normalize()*max # PVector obj

    @staticmethod
    def random2D(): # can't use self in static methods
        """ Return 2D unit vector pointing in a random direction.
            Implemented from third (polar) approach
            Source: http://nbeloglazov.com/2017/04/09/random-vector-generation.html"""
        # 1. r = 1, unit vector
        r = 1
        # 2. ϕ = random number [0, 2*PI]
        phi = random.uniform(0, 2*math.pi)
        # 3. calculate: x = r*cos(ϕ), y = r*sin(ϕ)
        x = r * math.cos(phi)
        y = r * math.sin(phi)
        return PVector(x, y)

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        added = tuple( a + b for a, b in zip(self, other) )
        return PVector(*added)

    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        subbed = tuple( a - b for a, b in zip(self, other) )
        return PVector(*subbed)

    def __mul__(self, other):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if type(other) == type(self):
            return self.inner(other)
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple( a * other for a in self )
            return PVector(*product)

    def __truediv__(self, other):
        """Same code as __div__ in Vector, but adapted for python 3"""
        if type(other) == type(1) or type(other) == type(1.0):
            divided = tuple( a / other for a in self )
            return PVector(*divided)
