#author：秦大粤
import matplotlib.pyplot as plt
import numpy as np
import random
class diffusion:
    def __init__(self,constant=0.5,l=500,update_times=50):
        self.l=l
        self.c=constant
        self.ss=[[0]*self.l]
        self.n=update_times
    def diff(self):
        self.ss[-1][int(self.l/2)]=1#initial scatter
        temp=[0]*self.l
        counter=1
        while(1):
            for i in range(len(self.ss[-1])-2):
                temp[i+1]=self.ss[-1][i+1]+self.c*(self.ss[-1][i+2]+self.ss[-1][i]-2*self.ss[-1][i+1])
            self.ss.append(temp)
            counter+=1
            if counter>self.n:
                break
    def show(self):
        x=np.arange(0,self.l,1)
        plt.plot(x,self.ss[-1],'.',label='time=%.1f'%(len(self.ss)-1))

        plt.legend(frameon=True)
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('density')
        plt.title('diffusion in one dimension')  

a=diffusion(update_times=50)
a.diff()
a.show()
a=diffusion(update_times=100)
a.diff()
a.show()
a=diffusion(update_times=500)
a.diff()
a.show()
a=diffusion(update_times=1000)
a.diff()
a.show()

class rand_walks:
    def __init__(self,l=100,N=5000,time=1000):
        self.l=l
        self.N=N
        self.n=time
        self.loca=[[0]*self.l]
    def walk(self):
        self.loca[-1][int(self.l/2)]=self.N
        counter=0
        while(1):
            counter+=1
            temp=[0]*self.l
            for  i in range(self.l-2):
                for j in range(self.loca[-1][i+1]):
                    rand=random.random()
                    if rand>0.5:
                        temp[i+2]+=1
                    elif rand<0.5:
                        temp[i]+=1
            self.loca.append(temp)
            if counter>self.n:
                break
    def show(self):
        x=np.arange(0,100,1)
        plt.plot(x,self.loca[-1],'.')
        plt.plot(x,self.loca[-1],label='time=%.f'%self.n)
        plt.title('random walks of %.f particles'%self.N)
        plt.xlabel('x')
        plt.ylabel('number of particles')
        plt.grid(True)
        plt.legend(frameon=True)
'''
b=rand_walks(time=10)
b.walk()
b.show()
b=rand_walks(time=100)
b.walk()
b.show()
b=rand_walks(time=1000)
b.walk()
b.show()
'''       
        
            
            
            
            
            
            
            
            
            
            
            
