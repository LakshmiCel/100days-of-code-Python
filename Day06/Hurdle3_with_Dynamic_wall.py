def move_up():
    turn_left()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
at_goal()
def move_right():
    turn_right()
    move()
def move_down():
    turn_right()
    move()
    turn_left()

def one_move():
#    move()
    move_up()
    move_right()
    move_down()

#for time in range(0, 6):
#    one_move()
    
#using while loop for the moving 
step = 6 
#while (step>=1):
#   if(at_goal()):
#        break
#    else:
#        one_move()
#        step-=1
while not at_goal():
    print(front_is_clear(), wall_in_front())
    if(front_is_clear()):
        move()
    elif(wall_in_front()):
        one_move()
        
        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
