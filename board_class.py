class Board:
    def __init__(self,points_number,points_colour,bar,out):
        self.points_number=points_number
        self.points_colour=points_colour
        self.bar=bar
        self.out=out
    RED = 0
    BLACK = 1
    NO_COLOUR = -1
    RED_HOME = 0
    BAR = -1
    OUT = 24
    def opponent( player ):
        return ( player + 1 ) % 2
    def number_of_pieces( board, point ):
        return board.points_number[point]
    
    
