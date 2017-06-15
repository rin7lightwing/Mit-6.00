# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
    def __init__(self, base, height):
        """
        base: base of the triangle
        height: height of the triangle
        """
        self.base = float(base)
        self.height = float(height)
    def area(self):
        """
        Returns area of the triangle
        """
        return 0.5*self.base*self.height
    def __str__(self):
        return 'Triangle with base %s and height %s' % (str(self.base), str(self.height))
    def __eq__(self, other):
        """
        Two triangles are equal if they have the same base and height.
        other: object to check for equality
        """
        return type(other) == Triangle and self.base == other.base and self.height == other.height

# t = Triangle(3.0, 4.0)
# print Triangle.area(t)


# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet(object):  # or ShapeSet(object)?
    # nextIdnNum = 0
    def __init__(self):
        """
        Initialize any needed variables
        """
        # self.names = []
        self.members = []
        self.place = None
        # self.idNum = ShapeSet.nextIdnNum
        # ShapeSet.nextIdnNum += 1
        ## TO DO

    # def getIdNum(self):
    #     return self.idNum

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        # print type(sh)
        for s in self.members:
            if s == sh:
                raise ValueError('duplicate shape')
        self.members.append(sh)
        # self.names.append(sh.__name__)

        ## TO DO
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.place = 0
        return self

    def next(self):
        if self.place >= len(self.members):
            raise StopIteration
        self.place += 1
        return ''

            ## TO DO
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        # set_str = ''
        # for s in self.members:
        #     set_str += str(s) + '\n'
        # return set_str
        for s in self.members:
            print s
        return ''
        ## TO DO

# sh1 = Circle(2.0)
# sh2 = Square(4.0)
# sh3 = Square(1.0)
# sh4 = Triangle(1.0, 1.0)
#
# shapeSet = ShapeSet()
# shapeSet.addShape(sh1)
# shapeSet.addShape(sh2)
# shapeSet.addShape(sh3)
# shapeSet.addShape(sh4)
# # for each in shapeSet.members:
# #     print type(each)
# print shapeSet

# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    largest_area = 0
    largest_shape = ()
    for s in shapes.members:
        if s.area() > largest_area:
            largest_area = s.area()
    for s in shapes.members:
        if s.area() == largest_area:
            largest_shape += (s,)
    return largest_shape
    ## DONE

# ss = ShapeSet()
# ss.addShape(Triangle(1.2,2.5))
# ss.addShape(Circle(4))
# ss.addShape(Square(3.6))
# ss.addShape(Triangle(1.6,6.4))
# ss.addShape(Circle(2.2))
#
# # for each in ss.members:
# #     print each.area()
#
# largest = findLargest(ss)
# for e in largest: print e


# ss = ShapeSet()
# ss.addShape(Triangle(3,8))
# ss.addShape(Circle(1))
# ss.addShape(Triangle(4,6))
# largest = findLargest(ss)
# for e in largest: print e

# t = Triangle(6,6)
# c = Circle(1)
# ss = ShapeSet()
# ss.addShape(t)
# ss.addShape(c)
# largest = findLargest(ss)
# print largest[0] is t
# print largest[0] is c



# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    file_shapes = ShapeSet()
    inFile = open(filename, 'r')
    for line in inFile:
        info = line.split(",")
        if info[0] == 'circle':
            shape = Circle(info[1])
        elif info[0] == 'square':
            shape = Square(info[1])
        elif info[0] == 'triangle':
            shape = Triangle(info[1], info[2])
        file_shapes.addShape(shape)
    return file_shapes

# test_ss = readShapesFromFile('shapes.txt')
# print test_ss


    ## Done

