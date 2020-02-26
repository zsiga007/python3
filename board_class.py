RED = 0
    BLACK = 1
    NO_COLOUR = -1
    RED_HOME = 0
    BAR = -1
    OUT = 24
class Board:
    #static members or methods
    RED = 0
    BLACK = 1
    NO_COLOUR = -1
    RED_HOME = 0
    BAR = -1
    OUT = 24
##member
    def __init__(self, points_number, points_colour, bar, out):
        self.points_number = points_number
        self.points_colour = points_colour
        self.bar = bar
        self.out = out
        ##fields
        ##subclasses, default inheritance, overwriting
def new_board():
    return \
        Board ([2, 0, 0, 0, 0, 5,
               0, 3, 0, 0, 0, 5,
               5, 0, 0, 0, 3, 0,
               5, 0, 0, 0, 0, 2],
                [BLACK, NO_COLOUR, NO_COLOUR, NO_COLOUR, NO_COLOUR, RED,
                NO_COLOUR, RED, NO_COLOUR, NO_COLOUR, NO_COLOUR, BLACK,
                RED, NO_COLOUR, NO_COLOUR, NO_COLOUR, BLACK, NO_COLOUR,
                BLACK, NO_COLOUR, NO_COLOUR, NO_COLOUR, NO_COLOUR, RED],
                [0, 0],
                [0, 0])
    @staticmethod 
    def opponent(self, player):
        return (player + 1) % 2

    def number_of_pieces(board, point):
        return board.points_number[point]

    def colour(board, point):
        return board.points_colour[point]

    def game_over(board):
        return ((board.out[0] == 15) or (board.out[1] == 15))

    def has_checker(board, player, fromPoint):
        return (board.points_colour[fromPoint] == player)

    def has_checkers_on_bar(board, player):
        return (board.bar[player] != 0)

    def move(board, player, fromPoint, toPoint):
        if fromPoint==BAR:
            board.bar[player]-=1
        else:
            if board.points_number[fromPoint] == 1:
                board.points_colour[fromPoint] = 'NO_COLOUR'
            if board.points_number[toPoint] <= 1:
                board.points_colour[toPoint] = player
            board.points_number[fromPoint] = board.points_number[fromPoint] - 1
            if not board.points_colour[toPoint]==opponent(player):
                board.points_number[toPoint] = board.points_number[toPoint] + 1
            else:
                board.bar[opponent(player)]+=1
            if toPoint==OUT:
                board.out[player]+=1
class InitialBoard(Board):
    def __init__(self):
        self=new_board()
    
