# CS121 Lab 3: Functions

import math

def distance(point1, point2):
    '''
    Computes the distance between two points

    Inputs:
        point1: (int, int)
        point2: (int, int)
    
    Returns: distance
    '''
    (x, y) = point1
    (i, j) = point2
    return math.sqrt((x - i)**2 + (y - j)**2)

def perimeter(point1, point2, point3):
    '''
    Computes the perimeter of a triangle given its edges

    Inputs:
        point1: (int, int)
        point2: (int, int)
        point3: (int, int)
    
    Returns: perimeter
    '''
    return distance(point1, point2) + distance(point1, point3) + distance(point2, point3)

def go():
    '''
    Write a small amount of code to verify that your functions work

    Verify that the distance between the points (0, 1) and (1, 0) is
    close to math.sqrt(2)

    After that is done, verify that the triangle with vertices at 
    (0, 0), (0, 1), (1, 0) has a perimeter 2 + math.sqrt(2)
    '''
    print("Points: (0, 1) and (1, 0)\n")
    print("Distance: {}\n".format(distance((0, 1), (1, 0))))
    print("Points: (0, 0), (0, 1), and (1, 0)\n")
    print("Perimeter: {}\n".format(perimeter((0, 0), (0, 1), (1, 0))))

if __name__ == "__main__":
    go()
       

