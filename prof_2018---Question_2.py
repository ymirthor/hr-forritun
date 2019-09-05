# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
POSITION_NUM=0
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid
def print_grid():
     line1=initialize_grid()[0]
     line2=initialize_grid()[1]
     line3=initialize_grid()[2]
     line4=initialize_grid()[3]
     line5=initialize_grid()[4]
     print(' '.join(map(str, line1)))
     print(' '.join(map(str, line2)))
     print(' '.join(map(str, line3)))
     print(' '.join(map(str, line4)))
     print(' '.join(map(str, line5)))
def new_position():
     if new_position(LEFT):
          print("LEFT")
# Main program starts here
# In your implementation, you have to use the functions and the constants given

print_grid()
get_move()
if get_move==LEFT:
     new_position(LEFT)
