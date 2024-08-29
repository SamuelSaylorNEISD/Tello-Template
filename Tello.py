#08/29/2024
#ask samuel saylor for more questions

from easytello import tello

drone = tello.Tello()

print(drone.get_battery()) # prints out the battery, i havent tested what kind of variable it is just yet
drone.takeoff() # Required to start the drone
drone.up(150) # Takeoff is really short so this helps get it high enough to not slice somebody's head off.

looper = True

def kill(): # I plan on replacing this function's code, but it's pretty self explanatory
    checker = input("Kill?")
    if checker == "y":
        looper = False
        print(drone.get_battery())

while looper == True:
    
    # All directional programs for drones must have an integer (measuring centimeters) plugged in
    drone.forward(10)
    drone.left(10)
    drone.right(10)
    drone.back(10)
    
    #clockwise and counterclockwise, angles has to be plugged in. do note that these drones are kinda cheap so they arent accurate
    drone.cw(90)
    drone.ccw(90)
    
    drone.flip("f") # Flips must have a string put into it, 'f' for forward, and so on so forth (i kinda dont know what goes into what honestly)
    
    kill()

drone.flip("b") 
drone.land() # required to land cause yeah