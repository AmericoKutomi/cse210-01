##
## W01 Prove: Tic-Tac-Toe game
## Author: AMERICO SADAO KUTOMI
## CSE 210 Section 20
##

# defines the global variable to be used as an internal board where zeroes show empty places
# the item array value will be 1 or 2 according to the player that has chosen that square
tic_tac_toe_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# main function
def main():
    # display the game title
    print('\nTic-Tac-Toe\n')

    # start with an empty board and show it
    show_empty_board()

    # start the option variable that will be used in loop control
    option = ''

    # start the order with the player 1
    player = 1

    # the main loop for one game
    while option != 0:
        # select the marking symbol for the player
        if player == 1:
            player_marking = 'x'
        else:
            player_marking = 'o'

        # gets the option from the player; it will break if zero is typed
        option = int(input(f"{player_marking}'s turn to choose a square (1-9, or zero to end): "))
        if option == 0:
            print(f'Game was interrupted.')
            break

        # the selected square will be marked for the player; if the square had been chosen before, the player needs to select other
        if not change_square(option, player):
            print(f'The square {option} is not empty. Try other.\n')
            continue

        # after selecting the square the order will pass to other player 
        if player == 1:
            player = 2
        else:
            player = 1

        # the board is shown again
        display_board()

        # the program checks if the game needs to be ended
        # the game_result function returns the winner player number or 9 if all squares are filled
        check_result = game_result()
        if check_result == 1:
            print(f'Player 1 won the game. Congratulations!')
            option = 0
        elif check_result == 2:
            print(f'Player 2 won the game. Congratulations!')
            option = 0
        elif check_result == 9:
            print(f'It is a draw. Thanks for playing!')
            option = 0

    # at this point the program will end the execution
    pass

def game_result():
    # this function verify if the game is over
    # return value:
    #   0: the game will go on
    #   1: player 1 has won
    #   2: player 2 has won
    #   9: all 9 squares are filled and the game needs to end

    # this is an internal function to check if a row, a column or a diagonal are completed by the same player
    def completed(index1, index2, index3):
        # return value:
        #   True: the row, column or diagonal is complete by the same player
        #   False: the three squares are not of the same player
        if (tic_tac_toe_board[index1] == 1 and tic_tac_toe_board[index2] == 1 and tic_tac_toe_board[index3] == 1) or \
            (tic_tac_toe_board[index1] == 2 and tic_tac_toe_board[index2] == 2 and tic_tac_toe_board[index3] == 2):
            return True
        else:
            return False
        pass

    # check the first row
    if completed(0,1,2):     
        # if the three squares are completed, the function will return the player number
        # the content of any of the three squares contains the winner player number
        return tic_tac_toe_board[0]  

    # the next lines follow the same logic of the above lines

    # check the second row
    if completed(3,4,5):
        return tic_tac_toe_board[3]
    # check the third row
    if completed(6,7,8):
        return tic_tac_toe_board[6]

    # check the first column
    if completed(0,3,6):     
        return tic_tac_toe_board[0]
    # check the second column
    if completed(1,4,7):
        return tic_tac_toe_board[1]
    # check the third column
    if completed(2,5,8):
        return tic_tac_toe_board[2]

    # check the diagonal from left to right
    if completed(0,4,8):
        return tic_tac_toe_board[0]
    # check the diagonal from right to left
    if completed(2,4,6):
        return tic_tac_toe_board[6]

    # if the function reaches this point is because there is no winner yet
    # the function will check if all the squares have been used
    squares_marked = 0
    for square in tic_tac_toe_board:
        # in a for statement, the used squares (value different from zero) are counted
        if square != 0:
            squares_marked += 1
    # if all squares are used, the counter will be 9
    if squares_marked == 9:
        return 9
    else:
        # at this point, there is no winner and there are squares to be chosen yet
        return 0

    pass

def show_empty_board ():
    # function that start a new board and show it
    # no return value

    # empty the board
    tic_tac_toe_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # display the board
    display_board()

    pass

def display_board ():
    # function that displays the board in three lines with more two separators lines
    # no return value

    # internal function that returns the content to be used in each square, preceded by a color sequence
    def square_content(index):
        # return value
        #   'x' for player 1, colored in cyan
        #   'o' for player 2, colored in yellow
        #   the number of the square, for empty square, with neutral color

        # verify the value of the array item in the global variable tic_tac_toe_board 
        if tic_tac_toe_board[index] == 1:
            return '\033[96mx'
        elif tic_tac_toe_board[index] == 2:
            return '\033[93mo'
        else:
            # as index is zero-based, the number of the square is added by 1
            return '\033[0m' + str(index + 1)
        pass

    print(f'{square_content(0)}|{square_content(1)}|{square_content(2)}\033[0m')
    print('-+-+-')
    print(f'{square_content(3)}|{square_content(4)}|{square_content(5)}\033[0m')
    print('-+-+-')
    print(f'{square_content(6)}|{square_content(7)}|{square_content(8)}\033[0m\n')
    pass

def change_square(option, player):
    # function that changes the value of the corresponding square
    # return value:
    #   True: the change has been made
    #   False: the change was not made because the square was already been chosen

    # the index is zero-based, so it is the square number minus 1
    index = option - 1

    # if the square is empty, its number is equal to zero
    if tic_tac_toe_board[index] == 0:
        # the square is attributed to the player
        tic_tac_toe_board[index] = player
        return True
    else:
        return False
    pass

# If this file is executed like this:
# > python tic_tac_toe.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
