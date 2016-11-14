import pylab as pl
import math
import vpython as vpy
claf.dt=step_time
        self.l=length
        self.q=q
        self.total_time=total_time
        self.fd=F_d
        self.omegad=Omega_d
        self.t=[0]
        self.n=int(total_time/step_time)
    def pendulum(self):
        while self.t[-1]<=self.total_time:
            temp_omega=self.omega[-1]+(-9.8/self.l*math.sin(self.theta[-1])-self.q*self.omega[-1]+self.fd*math.sin(self.omegad*self.t[-1]))*self.dt
            self.omega.append(temp_omega)
            temp_theta=self.theta[-1]+temp_omega*self.dt
            if temp_theta>math.pi:
                temp_theta=temp_theta-2*math.pi
            elif temp_theta<-math.pi:
                temp_theta=temp_theta+2*math.pi
            self.theta.append(temp_theta)
            temp_t=self.t[-1]+self.dt
            self.t.append(temp_t)
    def visual(self):
        ball=vpy.sphere()
        for i in range(len(self.theta)):
            vpy.rate(100)
            ball.pos.x+=self.t[i]
            ball.pos.y+=self.theta[i]
    def show_result(self):
        pl.plot(self.t,self.theta)
        pl.xlabel("time($s$)")
        pl.ylabel("angle($radians$)")

        
        
a=chaotic_pendulums()
a.pendulum()
a.visual()ss chaotic_pendulums:
    def __init__(self,length=9.8,q=0.5,initial_theta=0.2,initial_theta1=(0.2-0.001),initial_omega=0,initial_omega1=0,F_d=1.35,Omega_d=2/3,step_time=0.04,total_time=120):
        self.theta=[initial_theta]
        self.omega=[initial_omega]
        self.theta1=[initial_theta1]
        self.omega1=[initial_omega1]
        self.d_theta=[math.log(0.001)]
        sel
