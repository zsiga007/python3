## Strings for drawing the board:
colours = ["", ""]
colours[RED] = "R"
colours[BLACK] = "B"

################
## Board printing
################
## The printed representation of each point will occupy
## three characters.  The first and the last character
## will be a space (" ") if the point contains no checker
## at all.  Otherwise, the third character will be the
## character representing the colour of the checkers at
## the point.  The first character will be non-space only
## if the point contains more than 9 checkers.

def print_point( checkers, colour ):
    colour_string = colours[colour]
    if checkers == 0:
        print( " 0 ", end="" )
    elif checkers < 10:         # one-digit number
        ## add extra space before:
        print( " ", checkers, colour_string, sep="", end="" )
    else:                       # two-digit number
        print( checkers, colour_string, sep="", end="" )

## This procedure prints the board
## (missing: the bar is not printed).
## The board is represented by twelve consecutive
## lines, containing two points each (so we
## rotate the usual view of the board by 90 degrees).

def draw_board( board ):
    ## Number of spaces between the two columns
    ## ("column separator"):
    column_sep = "        "
    ## We will print 12 lines, with two points each:
    for i in range( 12 ):
        ## Number of checkers at the two points
        ## in this row:
        checkers1 = board_repr.number_of_pieces( board, 11 - i )
        checkers2 = board_repr.number_of_pieces( board, 12 + i )
        print_point( checkers1, board_repr.colour( board, 11 - i ) )
        print( column_sep, end="" )
        print_point( checkers2, board_repr.colour( board, 12 + i ) )
        ## Don't forget the newline at the end of each line:
        print()

