from math import sqrt
def countSquares(points):

    points = points.strip('[]').split('],[')  # Remove outer brackets and split on "],["
    points = set([tuple(map(int, point.split(','))) for point in points])  # Convert each point to a tuple of integers
    print(points)
    #points = set(points)

    count = 0

    #coordinates = [list(map(int, coord.split(','))) for coord in points]
    #points = set(points)
    #print(points)
    #count = 0
    pointList = list(points)
    print(pointList)
    print(len(pointList))
    for i in range(len(pointList)):
        for j in range(i+1,len(pointList)):
            x1,y1 = pointList[i]
            x2,y2 = pointList[j]
            #x3,y3 = points[k]
            # Calculate distance and check if sides are parallel to x or y axes
            #if abs(x1 - x2) == abs(y1 - y2):
                #continue
            
            #d = sqrt(((x1-x2))**2 +((y1-y2))**2)

            # Calculate the diagonal distance
            diagonal_distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # Skip if diagonal is 0 (same point)
            if diagonal_distance == 0:
                continue

            # Check if the two points can form a diagonal of an axis-aligned square
            if abs(x1 - x2) == abs(y1-y2) and x1 != x2 and y1 != y2:
                point3 = (x1,y2)
                point4 = (x2,y1)
                if point3 in points and point4 in points:
                    count += 1
                
    return count//2
        
points = input("Enter coordinates in the format [x1,y1],[x2,y2],... :")
print("Number of squares :" ,countSquares(points))

#[0,0],[0,1],[1,1],[1,0],[2,1],[2,0],[3,1],[3,0]


# Time Complexity: O(n2)
# Space Complexity: O(n)


#worst case scenarios:
# two points are too far away from each other
# Points are not a square
# They arent parallel to the axis