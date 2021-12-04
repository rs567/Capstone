#C format
import math as m
import numpy as np

#h, k, r, file = 1, 0, 1, "OD_Spline.txt"
#h, k, r, file = 1, 0, 0.5, "ID_Spline.txt"

def circlePointGen(h,k,r,z1,file):
    f = open(file,"w")
    x = np.linspace(h-r,h+r,num=20)
    z = [-z1,z1]
    i1 = 1

    print(file)
    w = 1
    for j in z:
        for i in x:
            i=round(i,5)
            h=round(h,5)

            c=(i-h)**2
            b=r**2
            
            c=round(c,5)
            b=round(b,5)

            print(r, i, h, c,b)
            print(w)
            w = w+1
            y = k - m.sqrt(b-c)
            point = '('+str(round(i,5))+' '+str(round(y,5))+' '+str(round(j,5))+')\n'
            f.write(point)

            i = i + 1

    print(file)
    f.close()

OD = circlePointGen(0.5, 0, 0.5, 0.05, "CircleSpline/OD_Spline.txt")
ID = circlePointGen(0.5, 0, 0.17, 0.05, "CircleSpline/ID_Spline.txt")

