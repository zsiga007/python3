import board_util
import random

def game_loop():
    board = board_util.new_board()
    next_player = random.choice( [board_util.BLACK, board_util.RED] )
    board_util.draw_board( board )
    game_over = False
    while not game_over:
        die1 = random.randrange( 1, 7 )
        die2 = random.randrange( 1, 7 )
        board_util.ask_player_and_move( board, next_player, die1, die2 )
        next_player = board_util.opponent( next_player )
        if board_util.game_over( board ):
            game_over = True

def ask_player_and_move( board, next_player, die1, die2 ):
    """
    function for asking the player and converting their answer to moves
    """
    
