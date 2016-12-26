#author：秦大粤
import random
import numpy as np
import matplotlib.pyplot as plt
class clusters:
    def __init__(self,size=100,number=10):
        self.l=size
        self.n=number
        self._fig=[[0]*self.l for i in range(self.l)]
    def growth(self):
        #initialization
        self._fig[int(self.l/2)][int(self.l/2)]=1
        counter=0
        while counter<self.n:
            #随机产生粒子
            tempx=random.randint(0,self.l-1)
            tempy=random.randint(0,self.l-1)
            if tempx==0:
                continue
            elif tempx==self.l-1:
                continue
            elif tempy==0:
                continue
            elif tempy==self.l-1:
                continue
            self._fig[tempx][tempy]=1
            if self._fig[tempx-1][tempy]==1:
                continue
            elif self._fig[tempx+1][tempy]==1:
                continue
            elif self._fig[tempx][tempy-1]==1:
                continue
            elif self._fig[tempx][tempy+1]==1:
                continue
            #walk
            while(1):
                self._fig[tempx][tempy]=0
                temp=random.random()
                if temp<0.25:
                    tempx-=1
                elif 0.25<temp<0.5:
                    tempy-=1
                elif 0.5<temp<0.75:
                    tempx+=1
                elif temp>0.75:
                    tempy+=1
                self._fig[tempx][tempy]=1
                
                if tempx==0:
                    self._fig[tempx][tempy]=0
                    break
                elif tempx==self.l-1:
                    self._fig[tempx][tempy]=0
                    break
                elif tempy==0:
                    self._fig[tempx][tempy]=0
                    break
                elif tempy==self.l-1:
                    self._fig[tempx][tempy]=0
                    break
                
                if self._fig[tempx-1][tempy]==1:
                    counter+=1
                    break
                elif self._fig[tempx+1][tempy]==1:
                    counter+=1
                    break
                elif self._fig[tempx][tempy-1]==1:
                    counter+=1
                    break
                elif self._fig[tempx][tempy+1]==1:
                    counter+=1
                    break
    def show(self):
        for i in range(self.l):
            for j in range(self.l):
                if self._fig[i][j]==1:
                    plt.plot(i,j,'g.')
                    plt.xlim(0,self.l)
                    plt.ylim(0,self.l)
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('DLA cluster,number of particles=%.f'%self.n)
                
a=clusters()
a.growth()
a.show()
