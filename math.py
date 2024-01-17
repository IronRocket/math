import math,pygame,sys


class Trig:
    def __init__(self,width:int,height:int,fps=30,scale=100) -> None:
        self.x = 0
        self.radians = 0
        self.sin = []
        self.cos = []
        self.tan = []

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.screen_color = (49, 150, 100)
        self.line_color = (255, 0, 0)
        self.lineSize = 1
        self.yOffset = 100
        self.scale = scale

    def drawSin(self):
        self.sin.append((self.x,math.sin(self.radians)*self.scale))
        for point in self.sin:
            point = (point[0],point[1]+self.yOffset)
            pygame.draw.line(self.screen, self.line_color, point, point, self.lineSize)
    
    def drawCos(self):
        self.cos.append((self.x,math.cos(self.radians)*self.scale))
        for point in self.cos:
            point = (point[0],point[1]+self.yOffset)
            pygame.draw.line(self.screen, self.line_color, point, point, self.lineSize)
    
    def drawTan(self):
        self.tan.append((self.x,math.tan(self.radians)*self.scale))
        for point in self.tan:
            point = (point[0],point[1]+self.yOffset)
            pygame.draw.line(self.screen, self.line_color, point, point, self.lineSize)

    def restartXPosition(self):
        self.x = 0
        self.sin = []
        self.cos = []
        self.tan = []
    
    def clear(self):
        self.x += 1
        self.radians = (math.pi/180)*self.x
        self.clock.tick(self.fps)
        self.screen.fill(self.screen_color)



t = Trig(800,800)


while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit(0)

    if t.x > t.width:
        t.restartXPosition()

    t.clear()

    t.drawSin()
    t.drawCos()
    t.drawTan()
    
    pygame.display.update()
