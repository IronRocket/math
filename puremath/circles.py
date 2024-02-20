from constants import PI

class Snapshot:
    def __init__(self,radius:float, rotations:float, duration:float):
        self.radius = radius
        self.rotations = rotations
        self.duration = duration

    def radians(self) ->None:
        return (self.rotations*2*PI)/self.duration; 

    def linearSpeedToRPM(self,distance:float)->float:
        c = 2*PI*self.radius
        return c*distance
    
    def linearSpeed(self)->float:
        c = 2*PI*self.radius
        return (c*self.rotations)/self.duration