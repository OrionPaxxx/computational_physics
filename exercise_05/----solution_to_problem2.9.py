import math
import pylab as pl
class canon_trajectory:
    def __init__(self,initial_velocity=700,angle_of_depature=45,altitude=0,
                 step_time=0.001,mass=10):
        self.i=0
        self.v=[initial_velocity]
        self.angle=angle_of_depature/180*math.pi
        self.vx=[initial_velocity*math.cos(angle_of_depature/180*math.pi)]
        self.vy=[initial_velocity*math.sin(angle_of_depature/180*math.pi)]
        self.x=[0]
        self.y=[altitude]
        self.t=[0]
        self.dt=step_time
        self.m=mass
    def trajectory(self):
        while(self.y[-1]>=0):
            temp_vx=self.vx[self.i]-0.06465*math.exp(-self.y[self.i]/10000)*(self.v[self.i]**2)/self.m*self.vx[self.i]/self.v[self.i]*self.dt
            temp_vy=self.vy[self.i]-0.06465*math.exp(-self.y[self.i]/10000)*(self.v[self.i]**2)/self.m*self.vy[self.i]/self.v[self.i]*self.dt-9.8*self.dt
            temp_v=math.sqrt(temp_vx**2+temp_vy**2)
            self.vx.append(temp_vx)
            self.vy.append(temp_vy)
            self.v.append(temp_v)
            temp_x=self.x[self.i]+temp_vx*self.dt
            temp_y=self.y[self.i]+temp_vy*self.dt
            self.x.append(temp_x)
            self.y.append(temp_y)
            temp_t=self.t[self.i]+self.dt
            self.t.append(temp_t)
            self.i=self.i+1
    def show_result(self):
        pl.plot(self.x,self.y)
        pl.xlabel("x(m)")
        pl.ylabel("y(m)")
        pl.title("trajectory of the canon")
        pl.ylim(0,500)
    def print_initial_value_and_land_coordinate(self):
        land_point=self.x[-2]-self.y[-2]*(self.x[-1]-self.x[-2])/(self.y[-1]-self.y[-2])
        print("mass---------------->",self.m)
        print("initial_velocity---->",self.v[0])
        print("angle_of_depature--->",self.angle/math.pi*180)
        print("altitude------------>",self.y[0])
        print("the canon land at------->   x=",land_point,"y=0")
    def store_result(self):
        datafile=open("cannon_data.txt","w")
        for j in range(len(self.t)):
            print(self.t[j],self.x[j],self.y[j],file=datafile)
        datafile.close()  
        
#the next code is programmed to show the trajectory of canon when angle of depature is 45degree.
class test_result_NO1(canon_trajectory):
    def draw_a_line(self):
        a=canon_trajectory()
        a.trajectory()
        a.show_result()
        a.print_initial_value_and_land_coordinate()
a=test_result_NO1()
a.draw_a_line()  


#the next code is programmed to find the angle of depature that maximize the range.
class test_result_NO2(canon_trajectory):
    def draw_90_lines(self):
        angle=1
        for i in range(88):
            b=canon_trajectory(angle_of_depature=angle)
            b.trajectory()
            b.show_result()
            angle=angle+1
b=test_result_NO2()
b.draw_90_lines()
        
        

#the next code is programmed to show how the range varies with the angle of departure
class test_result_NO3(canon_trajectory):
    def find_maximum_range(self):
        angle=1
        angles=[]
        ranges=[]
        for i in range(88):
            b=canon_trajectory(angle_of_depature=angle)
            b.trajectory()
            land_point=b.x[-2]-b.y[-2]*(b.x[-1]-b.x[-2])/(b.y[-1]-b.y[-2])
            angles.append(angle)
            ranges.append(land_point)
            angle=angle+1
        pl.plot(angles,ranges)
        pl.xlabel("angle_of_depature(degree)")
        pl.ylabel("range")
        pl.title("ranges versus angle of departure")
        max_range=max(ranges)
        for k in range(len(ranges)):
            if ranges[k-1]==max_range:
                best_angle=angles[k-1]
        print("best_angle=",best_angle)
        print("max_range=",max_range)
c=test_result_NO3()
c.find_maximum_range()









    

            
        
        
        
