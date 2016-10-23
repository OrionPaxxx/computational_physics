import pylab as pl
import math
class cannon_strike:
    def __init__(self,mass=10,altitude=0,initial_velocity=700,angle_of_departure=45,step_time=0.01,target_location_x=7000,target_location_y=5000):
        self.v=[initial_velocity]
        self.angle=angle_of_departure/180*math.pi
        self.vx=[initial_velocity*math.cos(self.angle)]
        self.vy=[initial_velocity*math.sin(self.angle)]
        self.x=[0]
        self.y=[0]
        self.t=[0]
        self.dt=step_time
        self.m=mass
        self.target_x=target_location_x
        self.target_y=target_location_y
        self.strike_point_y=0
    def trajectory(self):
        while (self.y[-1]>=0):
            temp_vx=self.vx[-1]-0.003233*math.exp(-self.y[-1]/10000)*(self.v[-1]**2)/self.m*self.vx[-1]/self.v[-1]*self.dt
            temp_vy=self.vy[-1]-0.003233*math.exp(-self.y[-1]/10000)*(self.v[-1]**2)/self.m*self.vy[-1]/self.v[-1]*self.dt-9.8*self.dt
            temp_v=math.sqrt(temp_vx**2+temp_vy**2)
            self.vx.append(temp_vx)
            self.vy.append(temp_vy)
            self.v.append(temp_v)
            temp_x=self.x[-1]+temp_vx*self.dt
            temp_y=self.y[-1]+temp_vy*self.dt
            self.x.append(temp_x)
            self.y.append(temp_y)
            temp_t=self.t[-1]+self.dt
            self.t.append(temp_t)
            if self.x[-1]>self.target_x:
                self.strike_point_y=(self.y[-2]-self.y[-1])/(self.x[-2]-self.x[-1])*(self.target_x-self.x[-1])+self.y[-1]
                break
    def show_result(self):
        pl.plot(self.x,self.y)
        pl.xlabel("x(m)")
        pl.ylabel("y(m)")
        pl.title("trajectory of the canon")
class precise_strike(cannon_strike):
    def pre_stk(self):
        #input the target location
        _input=input("please input the strike location like this:'x,y'\n")
        target_location=_input.split(",")
        temp_target_x=float(target_location[0])
        temp_target_y=float(target_location[1])
        #find the best angle
        temp_angle=1
        temp_velocity=190
        a=cannon_strike(angle_of_departure=temp_angle,initial_velocity=temp_velocity,target_location_x=temp_target_x,target_location_y=temp_target_y)
        a.trajectory()
        while a.strike_point_y<temp_target_y:
            if temp_angle<89:
                temp_angle=temp_angle+1
                a=cannon_strike(angle_of_departure=temp_angle,initial_velocity=temp_velocity,target_location_x=temp_target_x,target_location_y=temp_target_y)
                a.trajectory()
            else:
                temp_angle=1
                temp_velocity=temp_velocity+0.1
                a=cannon_strike(angle_of_departure=temp_angle,initial_velocity=temp_velocity,target_location_x=temp_target_x,target_location_y=temp_target_y)
                a.trajectory()
        #output the result
        print("stike point:","x=",a.target_x,"y=",a.strike_point_y)
        print("velocity=",temp_velocity,"angle=",temp_angle)
        tra,=pl.plot(a.x,a.y)
        loc,=pl.plot([a.target_x],[a.target_y],"*")
        pl.xlabel("x(m)")
        pl.ylabel("y(m)")
        pl.title("trajectory of the canon")   
        pl.legend([tra,loc],["trajectory","target location"],loc="upper left")        
b=precise_strike()
b.pre_stk()   

       
     