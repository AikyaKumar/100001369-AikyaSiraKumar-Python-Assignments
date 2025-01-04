from math import sqrt


#Find distance between all sides
def distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return sqrt(((x1-x2))**2 +((y1-y2))**2)


#Checking if Quadrilateral is parallel to x an y axis
def isParallelToAxes(points):
    if len(points) != 4:
        return False

    #Getting unique x and y coordinates
    x_coords = set(point[0] for point in points)
    y_coords = set(point[1] for point in points)

    #If there are more than 2 unique x or y, it is not parallel to the axes
    if len(x_coords) == 2 and len(y_coords) == 2:
        return True
    return False


#Checking if a quadrilateral is a squareS
def checkIfSquare(distances):
    # Get unique distances
    unique_distances = set(distances)
    # Check for the presence of side and diagonal lengths
    if len(unique_distances) != 2:
        return False # More than two unique distances
    else:
        return True