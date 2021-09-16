#excercise_05:chapter2_problem2.9
---------------------------------------------
***
##@.abstract
######this is programmed to reach a numerical solution to problem2.9 of Nicholas J.Giordano's computational physics。
**the eessential points of this problem is：    
      1.include both air drag and the reduced air density at high altitudes.    
      2.perform the calculation for different firing angles.    
      3.determine the value of the angle that gives the maximum range.**    
##@.background
###1.dynamic equations
![](https://github.com/OrionPaxxx/computational_physics_N2014301020039/blob/master/exercise_05/___1.png)
###2.drag force and some coefficient
![](https://github.com/OrionPaxxx/computational_physics_N2014301020039/blob/master/exercise_05/____2.png)
###3.Euler's method
![](https://github.com/OrionPaxxx/computational_physics_N2014301020039/blob/master/exercise_05/____3.png)
##@.main body:programs and results
######the py_document has been uploaded,click [here](https://github.com/OrionPaxxx/computational_physics_N2014301020039/blob/master/exercise_05/----solution_to_problem2.9.py) to check it
###1.the primary part of the program
![](https://github.com/OrionPaxxx/computational_physics_N2014301020039/blob/master/exercise_05/____pic_0.png)
###2.call the class and the result of it
![](https://github.com/OrionPaxxx/computational_physics_N2014301020039/blob/master/exercise_05/____pic_1.png) 
      
_____________________________________________
        this program can print the initial values,landing coordinate and output the cannon trajectory diagram.
![](https://github.com/OrionPaxxx/computational_physics_N2014301020039/blob/master/exercise_05/____test_result_NO1.png)
###3.perform the calculation for different firing angles.
![](https://github.com/OrionPaxxx/computational_physics_N2014301020039/blob/master/exercise_05/____pic_02.png)
     
______________________________________________
      
      there are 88 trajectories which firing angles are 1 degree,2 degrees,......,88degrees.
![](https://github.com/OrionPaxxx/computational_physics_N2014301020039/blob/master/exercise_05/____test_result_NO2.png)
###4.determine the value of the angle that gives the maximum range.
![](https://github.com/OrionPaxxx/computational_physics_N2014301020039/blob/master/exercise_05/____pic_03.png)
     
______________________________________________
      
     this program can print the maximum rang and its firing angle and output a diagram that shows how ranges varies with firing angles 
![](https://github.com/OrionPaxxx/computational_physics_N2014301020039/blob/master/exercise_05/____test_result_NO3.png)
##@.conclusions
#####1.the air resistance have a substantial effect on the trajectory，which is no longer a quadratic curve.    
#####2.since there is air resistance,the angle that gives the maximum range is usually less than 45degree.     
##@.acknowledgement
#####thank to Mr.cai's [teaching document](https://www.evernote.com/shard/s140/sh/26f85380-ee6c-4b4b-b33f-6871804d91ff/fb8cc702cb0e8ed7fafb50b2de4596ca)
