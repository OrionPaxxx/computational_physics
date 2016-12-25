import matplotlib.pyplot as plt
import numpy as np
import random
class cluster:
    def __init__(self,size=100,update_times=200,density=10):
        self.l=size
        self.n=update_times
        self.d=density
        self.color='b.'
        self._fig=[[0]*self.l for i in range(self.l)]
        self.total=0
        self.entropy=[]
    def diffu(self):
        #initial condition
        for i in range(int(self.l*2/5),int(self.l*3/5)):
            for j in range(int(self.l*2/5),int(self.l*3/5)):
                self._fig[i][j]=self.d
                self.total+=self.d
        #diffusion
        counter=1
        while(1):
            counter+=1
            temp_fig=[[0]*self.l for i in range(self.l)]
            for i in range(self.l):
                for j in range(self.l):
                    for k in range(self._fig[i][j]):
                        temp=random.random()
                        if temp<0.25:
                            temp_fig[i-1][j]+=1
                        elif 0.25<temp<0.5:
                            temp_fig[i][j-1]+=1
                        elif 0.5<temp<0.75:
                            temp_fig[i+1][j]+=1
                        elif temp>0.75:
                            temp_fig[i][j+1]+=1
            self._fig=temp_fig
            #calculate entropy
            temp_e=0
            for i in range(self.l):
                for j in range(self.l):
                    if self._fig[i][j]==0:
                        continue
                    else:
                        temp_e+=-self._fig[i][j]/self.total*np.log(self._fig[i][j]/self.total)
            self.entropy.append(temp_e)
            if counter>self.n:
                break
    def show(self):
        for i in range(self.l):
            for j in range(self.l):
                if self._fig[i][j]==0:
                    continue
                else:
                    if self._fig[i][j]>10:
                        self.color='r.'
                    elif 0.9*self.d<=self._fig[i][j]<=self.d:
                        self.color='y.'
                    elif 0.7*self.d<=self._fig[i][j]<=0.8*self.d:
                        self.color='g.'
                    elif 0.5*self.d<=self._fig[i][j]<=0.6*self.d:
                        self.color='c.'
                    elif 0.3*self.d<=self._fig[i][j]<=0.4*self.d:
                        self.color='b.'
                    elif 0.1*self.d<=self._fig[i][j]<=0.2*self.d:
                        self.color='m.'
                    plt.plot(i,j,self.color)
                    plt.xlim(0,self.l)
                    plt.ylim(0,self.l)
                    plt.xlabel('x')
                    plt.ylabel('y')
                    plt.grid(True)
                    plt.title('cream in coffee,time=%.f'%self.n)
    def plot_entropy(self):
        x=np.arange(0,self.n,1)
        plt.plot(x,self.entropy,'r.')
        plt.xlabel('time')
        plt.ylabel('entropy')
        plt.title('entropy versus time')
        plt.grid(True)
a=cluster()
a.diffu()
a.plot_entropy()