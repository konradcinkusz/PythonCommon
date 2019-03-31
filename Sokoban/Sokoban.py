# parcel
class Parcel :
    pass

# destination of the parcel
class Destination :
    pass

class BoardInitializationException(Exception) :
    pass

# board
# the game will take in the board
class Board :
    def __init__(self, *args, **kwargs):
        self.terrains = []
        if(len(args) >=2):
            self.width = args[0]
            self.height = args[1]
            if(len(args) > 2) :
                self.offset = args[2]
        else :
            raise BoardInitializationException()

    def addTerrain(terrain) :
        self.terrains.append(terrain)

class Terrain :
    
    @property
    def setBoard(board) :
        self.board = board

