import sys
import matplotlib.pyplot as plt
import math
import random
#returns average x and y coordinate
#Send in x and y list
def average(x_coords, y_coords):

    #makes sure they are the same size
    assert len(x_coords) == len(y_coords)

    total_x = 0
    total_y = 0

    for i in range(len(x_coords)):
        total_x += x_coords[i]
        total_y += y_coords[i]


    average_x = total_x / len(x_coords)
    average_y = total_y / len(y_coords)

    return average_x, average_y




#finds which center is closer
#send in x and y coordinate, and list of x and y centers
def whichIsCloser(x, y, x_centers, y_centers):

    closest = 0
    distanceFromCenter = math.sqrt( ((x - x_centers[0]) ** 2) + ((y - y_centers[0]) ** 2))

    #goes through all points and finds closest center point using distance formula
    for i in range(len(x_centers)):
        currentDistance = math.sqrt( ((x - x_centers[i]) ** 2) + ((y - y_centers[i]) ** 2))
        if currentDistance  < distanceFromCenter:
            distanceFromCenter = currentDistance
            closest = i


    return closest




def main():

    arguments = sys.argv

    numberOfClusters = int(arguments[1])
    filename = arguments[2]
    
    infile = open(filename, 'r')

    x_cord = []
    y_cord = []

    #gets points out of file
    for line in infile:
        x, y = line.split()
        x_cord.append(float(x))
        y_cord.append(float(y))



    #create random initial centers based upon number of clusters
    x_centers = []
    y_centers = []

    count = 0
    while count < numberOfClusters:
        x_centers.append(random.uniform(min(x_cord), max(x_cord)))
        y_centers.append(random.uniform(min(y_cord), max(y_cord)))

        count += 1


    #repeats x number of times to continue finding center
    numReps = 0
    while numReps < 10:
        #makes each key a list of values
        centers = {}

        for i in range(numberOfClusters):
            centers[i] = []

        #finds which points are closest to which center
        for i in range(len(x_cord)):
            closest = whichIsCloser(x_cord[i], y_cord[i], x_centers, y_centers)
            centers[closest].append((x_cord[i], y_cord[i]))
    


        #calculates average of each center
        for i in range(numberOfClusters):
            new_x = []
            new_y = []
            
            #get x and ys out tuples
            for j in range(len(centers[i])):
                new_x.append(centers[i][j][0])
                new_y.append(centers[i][j][1])

                if len(new_x) > 0:
                    x_centers[i], y_centers[i] = average(new_x, new_y)

        numReps += 1





#    plt.plot(x_cord, y_cord, 'ro')
#    plt.plot(x_centers, y_centers, 'go')
    colors = "bgrcmykw"
    color_index = 0
    for i in range(numberOfClusters):
        new_x = []
        new_y = []

        currentColor = colors[color_index]
        color_index += 1
        if color_index >= len(colors) - 1:
            color_index = 0

        for j in range(len(centers[i])):
            new_x.append(centers[i][j][0])
            new_y.append(centers[i][j][1])
            
            plt.scatter(new_x, new_y, color=currentColor, marker="o")


        plt.scatter(x_centers[i], y_centers[i], color=currentColor, marker="+", s=100)


    plt.show()

    return 0



main()
