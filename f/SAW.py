import matplotlib.pyplot as plt
import random
class SAW:
    def __init__(self,l=1000,n=1000):
        self.l=l
        self.n=n
        self.r2=[0]
        self.t=[0]
        self._fig=[[0]*self.l for i in range(self.l)]
        self.loc=[[int(self.l/2),int(self.l/2)]]
    def walk1(self):
        self._fig[self.loc[-1][0]][self.loc[-1][1]]=1
        while(1):
            temp=random.random()
            if temp<0.25:
                temp1=self.loc[-1][0]-1
                temp2=self.loc[-1][1]
            elif 0.25<temp<0.5:
                temp1=self.loc[-1][0]
                temp2=self.loc[-1][1]-1
            elif 0.5<temp<0.75:
                temp1=self.loc[-1][0]+1
                temp2=self.loc[-1][1]
            elif 0.75<temp<1:
                temp1=self.loc[-1][0]
                temp2=self.loc[-1][1]+1
            self.loc.append([temp1,temp2])
            self._fig[self.loc[-1][0]][self.loc[-1][1]]=1
            self.r2.append((self.loc[-1][0]-self.loc[0][0])**2+(self.loc[-1][1]-self.loc[0][1])**2)
            self.t.append(self.t[-1]+1)
            if self.t[-1]>=self.n:
                break
    def walk2(self):
        self._fig[self.loc[-1][0]][self.loc[-1][1]]=1
        temp=random.random()
        if temp<0.25:
            temp1=self.loc[-1][0]-1
            temp2=self.loc[-1][1]
            self.loc.append([temp1,temp2])
        elif 0.25<temp<0.5:
            temp1=self.loc[-1][0]
            temp2=self.loc[-1][1]-1
            self.loc.append([temp1,temp2])
        elif 0.5<temp<0.75:
            temp1=self.loc[-1][0]+1
            temp2=self.loc[-1][1]
            self.loc.append([temp1,temp2])
        elif 0.75<temp<1:
            temp1=self.loc[-1][0]
            temp2=self.loc[-1][1]+1
            self.loc.append([temp1,temp2])
        self._fig[self.loc[-1][0]][self.loc[-1][1]]=1
        self.r2.append((self.loc[-1][0]-self.loc[0][0])**2+(self.loc[-1][1]-self.loc[0][1])**2)
        self.t.append(self.t[-1]+1)
        while(1):
            if self.loc[-2][0]==self.loc[-1][0]+1:
                temp=random.random()
                if temp<1/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]-1
                elif 1/3<temp<2/3:
                    temp1=self.loc[-1][0]+1
                    temp2=self.loc[-1][1]
                elif temp>2/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]+1
            elif self.loc[-2][1]==self.loc[-1][1]+1:
                temp=random.random()
                if temp<1/3:
                    temp1=self.loc[-1][0]-1
                    temp2=self.loc[-1][1]
                elif 1/3<temp<2/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]-1
                elif temp>2/3:
                    temp1=self.loc[-1][0]+1
                    temp2=self.loc[-1][1]
            elif self.loc[-2][0]==self.loc[-1][0]-1:
                temp=random.random()
                if temp<1/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]-1

                elif 1/3<temp<2/3:
                    temp1=self.loc[-1][0]+1
                    temp2=self.loc[-1][1]

                elif temp>2/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]+1
            elif self.loc[-2][1]==self.loc[-1][1]-1:
                temp=random.random()
                if temp<1/3:
                    temp1=self.loc[-1][0]+1
                    temp2=self.loc[-1][1]

                elif 1/3<temp<2/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]+1
                elif temp>2/3:
                    temp1=self.loc[-1][0]-1
                    temp2=self.loc[-1][1]
            self.loc.append([temp1,temp2])
            self._fig[self.loc[-1][0]][self.loc[-1][1]]=1
            self.r2.append((self.loc[-1][0]-self.loc[0][0])**2+(self.loc[-1][1]-self.loc[0][1])**2)
            self.t.append(self.t[-1]+1)
            if self.t[-1]>=self.n:
                break
    def show1(self):
        plt.grid(True)
        plt.plot(self.t,self.r2,'.',label='usual random walk')
        plt.xlabel('time')
        plt.ylabel('$<r^2>$')
        plt.legend(frameon=True)
    def show2(self):
        plt.grid(True)
        plt.plot(self.t,self.r2,'.',label='self-avoiding random walk')
        plt.xlabel('time')
        plt.ylabel('$<r^2>$')
        plt.legend(frameon=True)
a=SAW()
a.walk1()
a.show1()
b=SAW()
b.walk2()
b.show2()




