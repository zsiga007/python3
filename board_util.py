import dict_repr as board_repr
## maybe we could use: 'from dict_repr import *' as it imports everything as I know and we do not have to refer to it always by name
## link to source: https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3
import vertical_draw as draw

## Represent the opponents (and their checkers etc.) with
## numbers, because we represent everything with numbers.
RED = board_repr.RED
BLACK = board_repr.BLACK

## We have to decide in which direction each opponent will proceed.
RED_HOME = board_repr.RED_HOME

def new_board():
    return board_repr.new_board()

def ask_player_and_move( board, next_player, die1, die2 ):
    ## I later realised that at tasks.py there is get player moves and what I did is quite similar...
    ## function for asking the player and converting their answer to moves I complete the move function in dict_repr;
    l=[die1,die2,die1+die2]
    if die1!=die2: ##this is just a hand-crafted method for the simpler method used below at die1==die2, but this may be used in another function...
        for i in range(1):
            c=False
            while c==False:
              try:
                  fromPoint = int(input("Enter a positive integer: ")) ##error handling added
                  toPoint = int(input("Enter a positive integer: "))
                  c = True
                  if fromPoint < 0 or toPoint < 0:
                    c=False
              except ValueError:
                c=False
                
            a=abs(fromPoint-toPoint) ## checking length of move
            while a in l and len(l)>1:
                if a==die1:
                    del l[-3] ##deleting possible moves if played
                if a==die2:
                    del l[-2]
                if a==die1+die2:
                    l=[] ##because max number of steps is reached
                if is_move_possible( board, next_player, fromPoint, toPoint )==True:
                    move( board, next_player, fromPoint, toPoint )
    if die1==die2:
        i=int(input())
        if len(legitimate_moves( board, next_player, die1, die2 )[i])==4: ##assuring that they select a sequence which is 4 long, so double moves are not distincted
            for j in range(3): ## this will execute the 4 (it goes until 3 because range starts at 0) moves included in the sub-list
                move( board, next_player, legitimate_moves( board, next_player, die1, die2 )[i][j][0], legitimate_moves( board, next_player, die1, die2 )[i][j][1] )##we assume that legitimate_moves is a list including lists of two long lists which represent the start and endpoints of a step        
    pass

def opponent( player ):
    return board_repr.opponent( player )

def game_over( board ):
    return board_repr.game_over( board )

def draw_board( board ):
    draw.draw_board( board )

def is_move_possible( board, player, fromPoint, toPoint ):
    """
    Checks if a given move is legitimate
    (only makes sure that there is no checker waiting on the bar
    (unless the move is from the bar), and that the target point 
    contains `player`'s checkers, no checker or exactly one of
    opponent's checkers.
    """
    if not board_repr.has_checker( player, board, fromPoint ):
        return False
    if board_repr.has_checkers_on_bar( player, board ):
        if not fromPoint == board_repr.BAR:
            return False
    
    ## temporary:
    return True

