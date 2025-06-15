def move_up():
    turn_left()
    while wall_on_right():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_right():
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
        
def one_move():
    move_up()
    move_right()
    turn_left()

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
    if (wall_in_front()):
        one_move()
    else:
        move()
        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
