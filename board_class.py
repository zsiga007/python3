    class Board:
    RED = 0
    BLACK = 1
    NO_COLOUR = -1
    RED_HOME = 0
    BAR = -1
    OUT = 24

    def __init__(self, points_number, points_colour, bar, out):
        self.points_number = points_number
        self.points_colour = points_colour
        self.bar = bar
        self.out = out

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

    def move(board, player, fromPoint, toPoint):  # assume that the labels of points run from 0 to 23
        """
        Assuming that the move is legitimate, actually carry it out.
        The board gets modified!
        """
        if board.points_number[fromPoint] == 1:  ## I later realised we had a function for colour...
            board.points_colour[fromPoint] = 'NO_COLOUR'
        if board.points_number[toPoint] <= 1:
            board.points_colour[toPoint] = player
        board.points_number[fromPoint] = board.points_number[fromPoint] - 1
        board.points_number[toPoint] = board.points_number[toPoint] + 1

    
    
