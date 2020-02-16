## tasks remaining for `ask_player_and_move()`

def get_player_moves( die1, die2 ):
    """
    Return a list of moves the given player wants to make
    """
    ## temporary:
    return []

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
    ## temporary:
    return []

## This is the hardest one:
def legitimate_moves( board, player, die1, die2 ):
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


