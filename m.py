import math,pygame,sys,time,random,keyboard

PI = 3.1415926535897932384626433832795028841971693993751

pygame.init()
font = pygame.font.SysFont('Comic Sans MS', 14)


def convertToRadians(x:int):
    return x*(math.pi/180)

class Vector:
    def __init__(self, x:float, y:float):
        '''
        A vector represents both a magnitude and direction.
        '''
        self.x =x
        self.y =y
        
class Engine:
    def __init__(self,width:int,height:int,fps=30) -> None:
        self.width =width
        self.height =height
        self.background = (0,155,0)
        self.screen =pygame.display.set_mode((width,height))
        self.fps = fps
        self.clock =pygame.time.Clock()
    def clear(self):
        self.clock.tick(self.fps)
        self.screen.fill(self.background)

class TrigFunctions():
    def __init__(self,screen:pygame.Surface,scale:int=10) -> None:
        self.screen = screen
        self.scale = scale
        self.x =0
        self.radians =0
        self.sin =[]
        self.cos =[]
        self.tan =[]

        self.screen_color =(49, 150, 100)
        self.line_color =(255, 0, 0)
        self.lineSize =1
        self.yOffset =100

    def renderSin(self):
        self.sin.append((self.x,math.sin(self.radians)*self.scale))
        for point in self.sin:
            point = (point[0],point[1]+self.yOffset)
            pygame.draw.line(self.screen, self.line_color, point, point, self.lineSize)
    
    def renderCos(self):
        self.cos.append((self.x,math.cos(self.radians)*self.scale))
        for point in self.cos:
            point = (point[0],point[1]+self.yOffset)
            pygame.draw.line(self.screen, self.line_color, point, point, self.lineSize)
    
    def renderTan(self):
        self.tan.append((self.x,math.tan(self.radians)*self.scale))
        for point in self.tan:
            point = (point[0],point[1]+self.yOffset)
            pygame.draw.line(self.screen, self.line_color, point, point, self.lineSize)

    def restartXPosition(self):
        self.x =0
        self.sin =[]
        self.cos =[]
        self.tan =[]


class Ellipse:
    def __init__(
            self,screen:pygame.Surface,
            minorAxis:float=25,majorAxis:float=50,
            angleRange:tuple=(0,360),offset=Vector(200,200),
            step:float=0.1,
            curserColor=(0,0,0),
            curserRadius:int=5,
            curserWidth:int=0,
            points:bool=False):
        self.screen = screen
        self.ellipsePoints =[]
        self.ellipseAngle =0

        self.currentVector = offset

        self.minorAxis:float =minorAxis
        self.majorAxis:float =majorAxis
        self.angleRange:tuple =angleRange
        self.offset:Vector =offset
        self.step:float = step 
        self.curserColor:tuple =curserColor
        self.curserRadius:int =curserRadius
        self.curserWidth:int =curserWidth
        self.points:bool = points
        self.pointColor:tuple =(0,0,0)
    
    def iNeedATriangle(self):
        pygame.draw.line(self.screen,self.curserColor,
                         (self.offset.x,self.offset.y),
                         (self.currentVector.x,self.currentVector.y))
        pygame.draw.line(self.screen,self.curserColor,
                         (self.currentVector.x,self.currentVector.y),
                         (self.currentVector.x,self.offset.y))
        pygame.draw.line(self.screen,self.curserColor,
                         (self.offset.x,self.offset.y),
                         (self.currentVector.x,self.offset.y))

    def details(self):
        pygame.draw.line(
                self.screen,self.curserColor,
                (self.offset.x,self.offset.y+self.minorAxis),
                (self.offset.x,self.offset.y-self.minorAxis),
        )
        pygame.draw.line(
                self.screen,self.curserColor,
                (self.offset.x-self.majorAxis,self.offset.y),
                (self.offset.x+self.majorAxis,self.offset.y),
        )
        foci = math.sqrt(self.minorAxis*self.majorAxis)
        foci1 = (self.offset.x+foci,self.offset.y)
        foci2 = (self.offset.x-foci,self.offset.y)
        pygame.draw.line(self.screen,(255,255,255),
                foci1,
                foci2,
        )

        textOffsetX = self.offset.x
        textOffsetY = self.offset.y-self.minorAxis-100
        text = font.render(f'F\u2081={int(foci1[0]),int(foci1[1])}',True, (255,255,255))
        self.screen.blit(text,(textOffsetX-text.get_width()/2,textOffsetY)
        )

        text = font.render(f'F\u2082={int(foci2[0]),int(foci2[1])}',True, (255,255,255) )
        self.screen.blit(text,(textOffsetX-text.get_width()/2,textOffsetY+20))

        text = font.render(f'Focus={int(foci)}', True, (255,255,255))
        self.screen.blit(text,(textOffsetX-text.get_width()/2,textOffsetY+40))


    def render(self):
        s =self
        self.currentVector =Vector(
            s.majorAxis*math.cos(convertToRadians(s.ellipseAngle))+s.offset.x,
            s.minorAxis*math.sin(convertToRadians(s.ellipseAngle))+s.offset.y
        )
        pygame.draw.circle(
            self.screen,
            s.curserColor,
            (self.currentVector.x,self.currentVector.y),
            s.curserRadius,
            width=s.curserWidth
        )
        s.ellipseAngle += s.step
        if s.ellipseAngle > s.angleRange[1]:
            s.ellipseAngle = s.angleRange[0]
        if s.points:
            adjust = int(s.angleRange[1]/s.step)-len(self.ellipsePoints)
            if adjust>>31 == -1:
                for i in range(-1,adjust,-1):
                    self.ellipsePoints.remove(self.ellipsePoints[i])
            else:
                for _ in range(adjust):
                    self.ellipsePoints.append(None)
            self.ellipsePoints[int(s.ellipseAngle/s.step)-1] = self.currentVector
            for point in self.ellipsePoints:
                if point != None:
                    pygame.draw.circle(self.screen,s.pointColor,(point.x,point.y),1)

class Snapshot:
    def __init__(self,radius,rotations,duration,engine:Engine):
        self.radius = radius
        self.rotations = rotations
        self.duration = duration*engine.fps
        self.r = pygame.Rect(engine.width/2,engine.height/2,10,10)
        self.angle = 0
        self.previous = time.perf_counter()
    def radians(self)->float:
        return (self.rotations*2*PI)/self.duration

    def linearSpeed(self) ->float:
        c = 2*PI*self.radius
        return (c*self.rotations)/self.duration
    
    def animate(self):
        pygame.draw.rect(engine.screen, (0,0,0), (0, 0, self.r.width, self.r.height), 2)
        self.angle += self.radians()*(180/PI)
        if self.angle > 360:
            self.angle = 0
        rotated_surface = pygame.transform.rotate(engine.screen, self.angle)
        rotated_rect = rotated_surface.get_rect(center=self.r.center)
        engine.screen.blit(rotated_surface, rotated_rect)
    
engine = Engine(800,800)
t = TrigFunctions(engine.screen)
e =Ellipse(
    engine.screen,minorAxis=50,majorAxis=100,
    angleRange=(0,360),offset=Vector(300,300),
    points=True,
    curserColor=(255,0,0),
    step=0.5
)

y = Snapshot(10,1,60,engine)

while True:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit(0)

    if keyboard.is_pressed('q') and y.rotations > 1:
        y.rotations -= 1
    if keyboard.is_pressed('e'):
        y.rotations += 1
    if t.x > engine.width:
        t.restartXPosition()
    engine.clear()
    y.animate()
    t.renderSin()
    t.renderTan()
    e.render()
    e.details()

    pygame.display.update()
