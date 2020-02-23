## tasks remaining for `ask_player_and_move()`

from dict_repr import *

    ## function for asking the player and converting their answer to moves I complete the move function in dict_repr;
    l=[die1,die2,die1+die2]
    if die1!=die2: ##this is just a hand-crafted method for the simpler method used below at die1==die2, but this may be used in another function...
        for i in range(1):
            fromPoint=int(input('Which checker to move? '))
            toPoint=int(input('Where to move? '))
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
            for j in range(3): ## this will execute the 4 moves included in the sub-list
                move( board, next_player, legitimate_moves( board, next_player, die1, die2 )[i][j][0], legitimate_moves( board, next_player, die1, die2 )[i][j][1] )##we assume that legitimate_moves is a list including lists of two long lists which represent the start and endpoints of a step

def is_move_possible( board, player, fromPoint, toPoint ):##we have done this in board util
    """
    Checks if a given move is legitimate
    (only makes sure that there is no checker waiting on the bar
    (unless the move is from the bar), and that the target point 
    contains `player`'s checkers, no checker or exactly one of
    opponent's checkers.
    """
    ## temporary
    return True

def possible_moves( board, player, die ):
    """
    Return a list of alternative moves that this player can make
    on this board with this die rolled.
    """
    ##as I see in dict_repr according to the rules black will go positive numbers along the list and red will go in the opposite negative direction
    ##as the list starts at the bottom right corner and goes up to the top right
    posslist=[]
    if has_checkers_on_bar(player, board)!=False:
        if playercolor(player)==True:
            if colour(board,24-die)==player or number_of_pieces( board, 24-die )<=1:
                posslist.append('bar',24-die)
        elif colour(board,die)==player or number_of_pieces( board, die )<=1:
            posslist.append('bar',die)
            
    else:
        if playercolor(player)==True:
            directionfactor=-1
        else:
            directionfactor=1
        for i in range(23):
            if colour(board,i)==player: ##checks if player has piece on point and if they can move with it
                if board["pointscolour"][i+directionfactor*die]==player or number_of_pieces( board, i+directionfactor*die )<=1:
                    posslist.append(i,i+directionfactor*die)
    return posslist

## Observe that after a move the allowed places where player can jump are 'almost' invariant (because if it jumps from a point where only 
## one of his pieces were, than that option vanishes...) as the other does not move until then, hence the die1!=die2 should not be too hard
def legitimate_moves( board, player, die1, die2 ):
    flist=[]
    if die1!=die2:
        posslist1=possible_moves( board, player, die1 )
        posslist2=possible_moves( board, player, die2 )
        for j in range(len(posslist1)):
            for i in range(len(posslist2)):
                if posslist1[j][0]!=posslist2[i][0]:
                    flist.append([posslist1[j],posslist2[i]]) ##this is definitely a valid sequence finally!!!
                elif number_of_pieces( board,posslist1[j][0])!=1: ##checking the mentioned only tricky case
                    flist.append([posslist1[j],posslist2[i]]) ##else we moved from the point (where only one was), so the sequence cannot be continued from there
                    ## note this flist is not yet complete even in this case as we could move from a point where we moved thanks to the throw with the other die,
                    ## which hence generated a new fromPoint, so I am thinking, maybe we should do a copy of the board where we try these changes which are not permanent
                    ## just a way to check the new possible sequences, from now on I am not quite sure how to continue this part

    """
    Return a list of move sequences that are legitimate.
    Unfortunately, in some cases we have to calculate all
    legitimate move sequences in order to decide if a given 
    move sequence is feasible, because of the maximality
    criterion (the maximum possible distance must be made).
    """
    ## Algorithm: We will set up an empty list of move
    ## sequences in which we will collect the legitimate
    ## sequences.
    
    ## We will also set up a ``todo list'' containing
    ## triples of the form `[move-sequence, board, remaining-roll]`,
    ## where `move-sequence` is a sequence of planned moves,
    ## and `remaining-roll` is what numbers we still have
    ## based on the roll.  Initially, the todo list will
    ## contain one or two elements, with the `move-sequence`
    ## being empty (no planned moves so far);  if `die1` and
    ## `die2` are different numbers, we will have two triples,
    ## with `remaining-roll` being different depending on the
    ## order of dice;  if the roll is doubles, we have only
    ## one triple, `remaining-roll` containing four times the
    ## number rolled.

    ## Then we will go through the todo list, and try to
    ## produce a new sequence from each element; if we have
    ## finished a sequence (because there are no remaining
    ## rolls or because no further move is possible), we append
    ## the result to our list of finished sequences;  otherwise,
    ## we update the current todo element, and append the result
    ## to the end of our todo list: we will get there later on.
    
    ## Finally, we could just return the list of finished move
    ## sequences, but we don't: we first have to keep only the
    ## maximal ones, because that's the rule in backgammon.

    finished = []
    if die1 == die2:
        todo = \
            [                   # list of todo elements
                [               # first and only triple
                    [],         # move-sequence of first triple
                    board,
                    [die1, die1, die1, die1] # remaining-roll
                ]                            # end of triple
            ]                                # end of todo list
    else:
        todo = \
            [                   # list of todo elements
                [               # first triple
                    [],         # move-sequence of first triple
                    board,
                    [die1, die2] # remaining-roll
                ],               # end of first triple

                [               # second triple
                    [],         # move-sequence of second triple
                    board,
                    [die2, die1] # remaining-roll
                ]                # end of second triple
            ]                    # end of todo list
    next_todo_index = 0          # our position in the todo list
    while True:                  # only stop if nothing more to do
        if next_todo_index == len( todo ) - 1: # nothing more to do
            break
        else:
            ## missing:
            ## Try to continue `move-sequence` with first element
            ## of `remaining-roll`.
            ## Append result to `finished` if failure or no more
            ## elements in `remaining-roll`;  append result to
            ## `todo` if successful.

            ## Prepare for next todo element:
            next_todo_index += 1
    ## We will choose the maximal ones in a separate function:
    return maximalMoveSequences( finished )

def maximalMoveSequences( moveSequences ):
    ## temporary:
    return moveSequences


