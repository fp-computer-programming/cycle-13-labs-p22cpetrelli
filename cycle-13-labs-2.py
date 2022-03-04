#author CJP 03/04/2022
def build_vehicle(a,b,c,d):
    wheels = a
    axels = b
    doors = c
    color = d
    print("The car has {0} wheels, {1} axels, {2} doors, and is {3}".format(wheels,axels,doors,color))

wheels = input("How many wheels does the car have? ")
axels = input("How many axels does the car have? ")
doors = input("How many doors does the car have? ")
color = input("What color is the car? ")

build_vehicle(wheels,axels,doors,color)