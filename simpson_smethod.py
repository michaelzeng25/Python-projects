import math

#area=dx/3*{f(x0)+4**f(x1)+2*f(x2).....4*f(xn-1)+f(xn)}

def function(x): #enter the function here
	return eval(s)

def dx():
    return int((b-a)/n);#without the int it will return a string type

def fab():  #find the sum of the 2 f(x) that are not multiply by 2 or 4\
    return function(a) + function(b)

def fxs():
    total=0
    for x in range(a+dx(),b,2*dx()):  #for when x is odd=will be multiply by 4
        total=total+function(x)*4
    for y in range(a+2*dx(), b-dx(),2*dx()):
        total=total+function(y)*2
    return total

def answer():
	return (dx()/3)*(fab()+fxs())

while(True):
    s=input("Enter the function here")
    a=int(input("Enter a here "))
    b=int(input("Enter b here "))
    n=int(input("Enter n here "))

    print (answer())
	


