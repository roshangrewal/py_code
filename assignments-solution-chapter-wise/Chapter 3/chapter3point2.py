hrs = input("Enter Hours:")
rate = input("Enter rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error, Please enter numeric value')
    quit()


if h<=40:
    p1= float
    p1 = h*r
    print (p1)

elif h>40:
    h1=h-40
    p2=40*r
    p3=h1*r*1.5
    p4=p2+p3
    print(p4)
