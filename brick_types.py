from brick_class import Brick
from position_class import Position

class LBrick(Brick):
    def __init__(self):
        super().__init__(id = 1)
        #rotation state
        self.cells = {
            0: [Position(0,2), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(1,1), Position(2,1), Position(2,2)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,0)],
            3: [Position(0,0), Position(0,1), Position(1,1), Position(2,1)]
        }
        self.move(0,3) 

class JBrick(Brick):
    def __init__(self):
        super().__init__(id = 2)
        #rotation state
        self.cells = {
            0: [Position(0,0), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(0,2), Position(1,1), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,2)],
            3: [Position(0,1), Position(1,1), Position(2,0), Position(2,1)]
        }
        self.move(0,3)

class IBrick(Brick):
    def __init__(self):
        super().__init__(id = 3)
        #rotation state
        self.cells = {
            0: [Position(1,0), Position(1,1), Position(1,2), Position(1,3)],
            1: [Position(0,2), Position(1,2), Position(2,2), Position(3,2)],
            2: [Position(2,0), Position(2,1), Position(2,2), Position(2,3)],
            3: [Position(0,1), Position(1,1), Position(2,1), Position(3,1)]
        }
        self.move(-1,3)

class OBrick(Brick):
    def __init__(self):
        super().__init__(id = 4)
        #rotation state
        self.cells = {
            0: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            1: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            2: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            3: [Position(0,0), Position(0,1), Position(1,0), Position(1,1)]
        }
        self.move(0,4)

class SBrick(Brick):
    def __init__(self):
        super().__init__(id = 5)
        #rotation state
        self.cells = {
            0: [Position(0,1), Position(0,2), Position(1,0), Position(1,1)],
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,2)],
            2: [Position(1,1), Position(1,2), Position(2,0), Position(2,1)],
            3: [Position(0,0), Position(1,0), Position(1,1), Position(2,1)]
        }
        self.move(0,3)

class TBrick(Brick):
    def __init__(self):
        super().__init__(id = 6)
        #rotation state
        self.cells = {
            0: [Position(0,1), Position(1,0), Position(1,1), Position(1,2)],
            1: [Position(0,1), Position(1,1), Position(1,2), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(1,2), Position(2,1)],
            3: [Position(0,1), Position(1,0), Position(1,1), Position(2,1)]
        }
        self.move(0,3)

class ZBrick(Brick):
    def __init__(self):
        super().__init__(id = 7)
        #rotation state
        self.cells = {
            0: [Position(0,0), Position(0,1), Position(1,1), Position(1,2)],
            1: [Position(0,2), Position(1,1), Position(1,2), Position(2,1)],
            2: [Position(1,0), Position(1,1), Position(2,1), Position(2,2)],
            3: [Position(0,1), Position(1,0), Position(1,1), Position(2,0)]
        }
        self.move(0,3)