import os
import time
my_name=[" ","######       ####       #    #"," ","#    #       #   #       #   #"," ","#    #       #    #       ##"," ","#   ##       #   #         #"," ","#######      ####          #"]
x=1
while x<20:
    print(my_name[0:x+1])
    print(my_name[x+1:2*x+2])
    print(my_name[2*x+2:3*x+3])
    print(my_name[3*x+3:4*x+4])
    print(my_name[4*x+4:5*x+5])
    my_name.insert(0," ")
    my_name.insert(x+2," ")
    my_name.insert(2*x+4," ")
    my_name.insert(3*x+6," ")
    my_name.insert(4*x+8," ")
    x=x+1
    time.sleep(0.1)
    i = os.system('cls')













































