import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pylab as pl
import math
class solar:
    def __init__(self,x0=1,y0=0,vx=0,vy=2*math.pi,dt=0.001,dbeta=0,total_time=100,alpha=0):
        self.x=[x0]
        self.y=[y0]
        self.r=[math.sqrt(x0**2+y0**2)]
        self.vx=[vx]
        self.vy=[vy]
        self.dt=dt
        self.t=[0]
        self.tt=total_time
        self.db=dbeta
        self.a=alpha
    def run(self):
        while self.t[-1]<self.tt:
            self.vx.append(self.vx[-1]-4*math.pi**2*self.x[-1]*(1+self.a/(self.r[-1]**2))/self.r[-1]**(3+self.db)*self.dt)
            self.vy.append(self.vy[-1]-4*math.pi**2*self.y[-1]*(1+self.a/(self.r[-1]**2))/self.r[-1]**(3+self.db)*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.r.append(math.sqrt(self.x[-1]**2+self.y[-1]**2))
            self.t.append(self.t[-1]+self.dt)
    def show(self):
        pl.title("simulation of elliptical orbit")
        pl.xlabel("x")
        pl.ylabel("y")
        pl.xlim(-1,1)
        pl.ylim(-1,1)
        pl.plot(self.x, self.y,label="$\\beta$ =%.3f"%(2+self.db))  
        pl.legend()
        pl.grid(True)
        pl.show()
    def show_(self):
        vs=[10.061,7.405,6.283,5.096,2.755,2.034,1.434,1.146]
        rs=[0.39,0.72,1.00,1.52,5.20,9.54,19.19,30.06]
        names=['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune']
        fig = plt.figure()  
        ax = fig.add_subplot(111, projection='3d') 
        plt.title("solar system")
        plt.xlabel("x")
        plt.ylabel("y")
        for i in range(len(vs)):
            a=solar(vy=vs[i],x0=rs[i])
            a.run()
            ax.plot(a.x, a.y,label=names[i]) 
        plt.legend()
        plt.show()

#show the whole solar system  
a=solar()
a.run()
a.show_()
#the inverse square law and the stabiliity of planetary orbits
b=solar(dbeta=0.1,vy=5)
b.run()
b.show()
#precession of the perihelon of mercury
class precession(solar):
    def m_run(self):
        _alphas=[0.0001,0.0004,0.003,0.0035,0.004,0.006,0.007]
        omegas=[]
        for i in _alphas:
            a=solar(x0=0.39,vy=10.061,total_time=100,alpha=i)
            a.run()
            _min=1
            _j=0
            for j in range(len(a.r)):
                if a.r[j]<_min:
                    _min=a.r[j]
                    _j=j
            min_r=a.r[_j]+(a.r[_j-1]-a.r[_j])/2
            temp_theta=[]
            temp_t=[]
            for k in range(len(a.r)):
                if a.r[k]<min_r:
                    temp_theta.append(math.asin(a.x[k]/a.r[k])*360/2/math.pi)
                    temp_t.append(a.t[k])
            omegas.append((temp_theta[3]-temp_theta[2])/(temp_t[3]-temp_t[2]))
        print(omegas)
test=precession()
test.m_run()

#线性拟合，列表_omegas中的数据为test的运行结果
_alphas=[0,0.0001,0.0004,0.003,0.0035,0.004,0.006,0.007]
_omegas=[0,2.1360957657207646,3.79859101235552, 31.586827548752012, 35.67506491602629,\
 39.82020809760321,64.21130592694833, 80.79924387065746]
pl.plot(_alphas,_omegas,'.')
z=np.polyfit(_alphas,_omegas,1)
p=np.poly1d(z)
print(z)
print(p)
linspx=np.linspace(0,0.007)
linspy=z[0]*linspx+z[1]
pl.title('precession rate versus $\\alpha$')
pl.xlabel("$\\alpha$")
pl.ylabel("$d\\theta /dt$(degree/yr)")
pl.plot(linspx,linspy)
pl.grid(True)
