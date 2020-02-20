from pythymiodw import *
from time import sleep
from libdw import pyrebase


url = 'https://thymio-week-4.firebaseio.com/'  # URL to Firebase database
apikey = 'AIzaSyC2dv-BGYMKYgS5K7laqnH7lDzJrJGUl3U'  # unique token used for authentication

config = {
    "apiKey": apikey,
    "authDomain": "thymio-week-4.firebaseapp.com",
    "databaseURL": url,
}

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
db = firebase.database()

robot = ThymioReal()  # create a robot object

no_movements = True
moves = None
while no_movements:
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the robot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.
    moves = db.child("move cmd").get().val()
    if moves == None:
        sleep(0.5)
    else:
        no_movements = False
    
    # Write your code here
    

# Write the code to control the robot here
for cmd in moves:
    if cmd == "up":
        robot.wheels(100, 100)
    elif cmd == "left":
        robot.wheels(-100, 100)
    elif cmd == "right":
        robot.wheels(100, -100)
    sleep(1)
# 'up' movement => robot.wheels(100, 100)
# 'left' movement => robot.wheels(-100, 100)
# 'right' movement => robot.wheels(100, -100)

