#This program is a Monte Carlo simulation that sets n random points
#within a square with side length 1 that has a circle inscribed
#within it. The idea behind this simulation is that if the points
#are set randomly, the ratio of the number of points that land within
#the circle to the total number of points set in the square will reflect
#the ratio of the area of the circle to the area of the square.
#Using the area formula's for each shape we can effectively predict
#the value of pi.
import sys, os, random, math

#number of points to place
n = 100000
circle = 0
square = n

for i in range(n):
    #place a random point
    sign_x = (-1)**(round(random.random()))
    sign_y = (-1)**(round(random.random()))
    x = sign_x * random.random() / 2
    y = sign_y * random.random() / 2

    #check if the point is within the circle
    distance = math.sqrt(x**2 + y**2)
    if distance <= 0.5:
        circle = circle + 1

#Area_circle/Area_square = (pi*R^2)/(2R)^2 = pi/4
#Therefore pi = 4 times the ratio of the circle points to the total
#points placed.
pi = 4*float(circle)/float(square)
print "pi = {}".format(pi)
    
