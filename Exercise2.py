from itertools import combinations
from functions import distance,isParallelToAxes,checkIfSquare

#Getting input of coordinates from user
# example input [0,0],[0,1],[1,1],[1,0],[2,1],[2,0],[3,1],[3,0],[1,2],[0,2]
userInput = input('Enter coordinates in the format [x1,y1],[x2,y2],... : ')
coordinate_strings = userInput.strip("[]").split("],[")
coordinates = [list(map(int, coord.split(','))) for coord in coordinate_strings]

#Making a set of all possible quadrilaterals from the given coordinates
quads = set()
quads = tuple((combinations(coordinates, 4)))

#Finding out number of squares
squares = 0
for vertices in quads:
    #leave if it is not axes aligned
    if not isParallelToAxes(vertices):
        continue

    #Finding side and diagonal lengths
    v1,v2,v3,v4 = vertices[0],vertices[1],vertices[2],vertices[3]
    distances = list(combinations([v1,v2,v3,v4],2)) 
    s = [distance(distances[i][0],distances[i][1]) for i in range(6)]

    #Checking if lengths satisfy sqaure properties
    if checkIfSquare(s):
        squares = squares+1


print("No of possible squares: ",squares)
