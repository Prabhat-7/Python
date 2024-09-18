import math as m
def fact(x):
    if x>1:
        return x*fact(x-1)
    if (x==1 or x==0):
        return 1


def sin(x):
    sin_x=0
    for i in range(50):
       sin_x+= ((-1)**i)*((x)**(2*i+1))/fact(2*i+1)
    return sin_x
print(sin(m.radians(float(input("Enter the angle (in degrees):")))))