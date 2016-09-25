import os
import time
my_name=["######       ####       #    #","#    #       #   #       #   #","#    #       #    #       ##","#   ##       #   #         #","#######      ####          #"]
x=0
space=" "
while x<80:   
    print(space*x+my_name[0])
    print(space*x+my_name[1])
    print(space*x+my_name[2])
    print(space*x+my_name[3])
    print(space*x+my_name[4])
    x=x+1
    time.sleep(0.1)
    i = os.system('cls')