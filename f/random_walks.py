import random
import matplotlib.pyplot as plt
class random_walks:
    def __init__(self,n=100,step_length=0.1):
        self.x=[0]
        self.y=[0]
        self.x2=[0]
        self.n=n
        self.l=step_length
    def walk1(self):#random walk with step_length=1
        for i in range(1,self.n):
            self.x.append(i)
            temp=random.random()
            if temp < 0.5:
                self.y.append(self.y[-1]-self.l)
            elif temp > 0.5:
                self.y.append(self.y[-1]+self.l)
            self.x2.append(self.x2[-1]+self.l**2)
    def walk2(self):#random walk with random step-length
        for i in range(1,self.n):
            self.x.append(i)
            temp=random.random()
            self.l=random.random()
            if temp < 0.5:
                self.y.append(self.y[-1]-self.l)
            elif temp > 0.5:
                self.y.append(self.y[-1]+self.l)
            self.x2.append(self.x2[-1]+self.l**2)
    def show1(self):
        plt.plot(self.x,self.y,'o')
        plt.title('random walk in one dimension')
        plt.xlabel('step number')
        plt.ylabel('x')
        plt.grid(True)
    def show2(self):
        plt.plot(self.x,self.x2,'.',label='$<x^2>$ versus time')
        plt.title('random walk in one dimension')
        plt.xlabel('step number')
        plt.ylabel('$<x^2>$')
        plt.legend(frameon=True)
        plt.grid(True)
a=random_walks()
a.walk2()
a.show1()
b=random_walks()
b.walk2()
b.show1()

