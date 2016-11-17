import matplotlib.pyplot as plt  
import pylab as pl
class lorenz_model:
    def __init__(self,initial_x=1,initial_y=0,initial_z=0,r=24,b=8/3,delta=10,time_step=0.0001,total_time=50):
        self.x=[initial_x]
        self.y=[initial_y]
        self.z=[initial_z]
        self.t=[0]
        self.dt=time_step
        self.b=b
        self.r=r
        self.delta=delta
        self.time=total_time
    def run(self):
        while self.t[-1]<self.time:
            self.x.append(self.x[-1]+self.delta*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-1]*self.z[-1]+self.r*self.x[-1]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-1]*self.y[-1]-self.b*self.z[-1])*self.dt)
            self.t.append(self.t[-1]+self.dt)



class plots(lorenz_model):
    def show(self):
        a=lorenz_model(r=24.1,total_time=120)
        a.run()
        pl.plot(a.t,a.z,label="r=%.2f"%a.r)
        pl.xlabel("time($s$)")
        pl.ylabel("z")
        pl.legend(loc='upper center',frameon = True)
        pl.grid(True)
        pl.show()
    def plot_t_z(self):
        rs=[5,10,25,24.1]
        for i in rs:
            a=lorenz_model(r=i)
            a.run()
            if a.r==rs[0]:
                z1=a.z
                pl.plot(a.t,z1,label="r=%f"%a.r)
            elif a.r==rs[1]:
                z2=a.z
                pl.plot(a.t,z2,label="r=%f"%a.r)
            elif a.r==rs[2]:
                z3=a.z
                pl.plot(a.t,z3,label="r=%f"%a.r)
            elif a.r==rs[3]:
                z4=a.z
                pl.plot(a.t,z4,label="r=%f"%a.r)
        pl.title("lorenz model z versus time")
        pl.xlabel("time")
        pl.ylabel("z")
        pl.legend(loc="upper right",frameon=True)
        pl.grid(True)
    def plot_phase(self):
        a=lorenz_model(r=23)
        a.run()
        plot5,=pl.plot(a.x,a.z,label="r=%.2f"%a.r)
        pl.title("phase space z versus x")
        pl.xlabel("x")
        pl.ylabel("z")
        pl.legend(loc='upper center',frameon = True)
        pl.grid(True)
    def td_plot(self):
        fig = plt.figure()  
        ax = fig.add_subplot(111, projection='3d')  
        a=lorenz_model(r=25)
        a.run()
        X=a.x
        Y=a.y
        Z=a.z 
        plt.title("phase space:x,y,z")
        plt.xlabel("x")
        plt.ylabel("y")
        ax.plot(X, Y, Z,label="r=%.2f"%a.r)  
        plt.legend()
        plt.show()  
f=plots()
f.td_plot()

        
