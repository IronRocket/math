import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self,fig,ax):
        self.fig = fig
        self.ax = ax
        self.x = np.linspace(0, 2 * np.pi, 200)

    def sinGraph(self,a=5,f=4,h=0,v=0,i=False):
        '''
        a=amplitude f=frequency
        h=horizontal v=vertical
        i=inverse
        '''
        if i:
            self.ax.plot(self.x,a*np.arcsin(f*self.x+h)+v)
        else:
            self.ax.plot(self.x,a*np.sin(f*self.x+h)+v)
    
    def cosGraph(self,a=5,f=4,h=0,v=0,i=False):
        '''
        a=amplitude f=frequency
        h=horizontal v=vertical
        i=inverse
        '''
        if i:
            self.ax.plot(self.x,a*np.arccos(f*self.x+h)+v)
        else:
            self.ax.plot(self.x,a*np.cos(f*self.x+h)+v)
    
    def tanGraph(self,a=1,f=1,h=0,v=0,i=False):
        '''
        a=amplitude f=frequency
        h=horizontal v=vertical
        i=inverse
        '''
        if i:
            self.ax.plot(self.x,a*np.arctan(f*self.x+h)+v)
        else:
            self.ax.plot(self.x,a*np.tan(f*self.x+h)+v)

fig, ax = plt.subplots()
g = Graph(fig,ax)

g.sinGraph(i=True)
g.cosGraph(i=True)
g.tanGraph(i=True)


plt.show()