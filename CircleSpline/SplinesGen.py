#C format
import math as m
import numpy as np

#h, k, r, file = 1, 0, 1, "OD_Spline.txt"
#h, k, r, file = 1, 0, 0.5, "ID_Spline.txt"

def circlePointGen(h,k,r,file):
    f = open(file,"w")
    x = np.linspace(h-r,h+r,num=20)
    z = [-0.05,0.05]

    for j in z:
        for i in x:
            y = k - m.sqrt(r**2-(i-h)**2)
            point = '('+str(round(i,5))+' '+str(round(y,5))+' '+str(round(j,5))+')\n'
            f.write(point)

    f.close()

OD = circlePointGen(1, 0, 1, "OD_Spline.txt")
ID = circlePointGen(1, 0, 0.5, "ID_Spline.txt")

