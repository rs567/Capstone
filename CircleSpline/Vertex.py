import math as m
import numpy as np
x = [0,0.33,0.67,1]
y = [0,1]
z = [-0.05,0.05]
j = 0

f = open("CircleSpline/vertex.txt","w")

for i3 in z:
    for i1 in x:
        for i2 in y:
            point = '('+str(i1)+' '+str(i2)+' '+str(i3)+')\n'#//'+str(j)+'\n'
            j = j +1
            f.write(point)
