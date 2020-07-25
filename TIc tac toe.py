"""
Written by Gavin Kroeger for FIT9136
Started 1/04/2020
Last Editted 1/04/2020

An implementation of tic-tac-toe
"""


# this is an algorithm I always use for printing grids.
# it has taken me a lot of iterations to get this right, so if you use it
# in your work, please cite me.
def pretty_print(matrix):
    # string topper, can be left blank if no header is needed
    new_string = "\t0\t1\t2\n"

    # count for side axis
    count = 0

    # for each line, for each item, tab separate the items and attach to new string
    for line in matrix:
        new_line = str(count) + "\t"
        for item in line:
            new_line += str(item) + "\t"
        count += 1
        new_line = new_line.strip()

        new_string += new_line + "\n"

    new_string = new_string[:len(new_string)]
    return new_string


# maybe not needed for a game this size, but this prints the game area
# you could extend it to print the entire game state including whose turn it is
def print_menu(game_state):
    print(pretty_print(game_state))

    print("Where would you like to place your piece (enter your choice space separated e.g. 0 0)")


# checks for a winner on the grid. True if there is, False otherwise
def is_winner(game_state):
    # check each row for a winner
    for row in game_state:
        if row[0] != "-" and row[0] == row[1] == row[2]:
            return True

    # check each column for a winner
    for x in range(3):
        if game_state[0][x] != "-" and game_state[0][x] == game_state[1][x] == game_state[2][x]:
            return True

    # check both diagonals for a winner
    if game_state[0][0] != "-" and game_state[0][0] == game_state[1][1] == game_state[2][2]:
        return True
    if game_state[0][2] != "-" and game_state[0][2] == game_state[1][1] == game_state[2][0]:
        return True

    return False


# this is quite a naive validate function. You should extend this to check
# that enough numbers have been entered, and that the entered text is actually
# numbers. Further, those numbers should be within the grid.
def validate_input(choice, game_grid):
    if game_grid[int(choice[0])][int(choice[1])] != "-":
        return False

    return True


# checking that every location hasn't been taken by a piece.
def is_draw(game_state):
    draw = True

    for row in game_state:
        for char in row:
            if char == "-":
                draw = False

    return draw


# game grid. Uses "-" to represent an empty value.
# a lot of code would need to change if we didn't use "-" here.
game_grid = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

# to keep track of who is placing a piece
turn = 0

# main driver of the code. Keep playing until either a winner, or a draw
while (not is_winner(game_grid) and not is_draw(game_grid)):

    # player 1 plays on even turns, player 2 plays on odd turns
    if turn % 2 == 0:
        player = 1
    else:
        player = 2

    print("Its your turn player", player)

    print_menu(game_grid)

    # basic check of valid input. For this to be useful it should indicate
    # what was wrong with the input in the first place with a unique message
    # this would require our function to return why it was wrong.
    choice = input().split(" ")

    while (not validate_input(choice, game_grid)):
        choice = input("Invalid choice, please enter another:").split()

    # these can be whatever you want except for "-"
    if player == 1:
        char = "O"
    else:
        char = "X"

    # always ensure your input is turned to the correct types to be used in
    # grids or other arthmetic actions.
    game_grid[int(choice[0])][int(choice[1])] = char

    # without this player 1 plays all the time
    turn += 1

# when we exit the loop we need to check to see why the game ended
# before presenting a message
if (is_winner(game_grid)):
    print("Player", player, "is the winner!")
else:
    print("It is a draw!")