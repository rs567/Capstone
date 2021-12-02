## Searches for best resistor combination w/ loss function to match targeted output
## Broken

import math
from random import seed
from random import random
def MSE(x,y): #Mean Sqaure Error
    if(x==y):
        return 0
    x=(x**2)
    y=y**2
    output=abs(x-y)**2
    output=(math.sqrt(output))
    return(output)
class SOl:
    R1=0
    R2=0
    R3=0 
    R4=0
    cost=9999999999999999999
    ex_voltage=24 # want v
    ex_curre=.25 # want current
    pred_volatage=0
    pred_curre=0
    voltage = 1200 # battery

    def __init__(self,a,b,c,d):
        self.R1=a
        self.R2=b
        self.R3=c
        self.R4=d
        total_current=self.voltage/(self.R1+((1/(self.R4+self.R3))+(1/self.R2))**-(1))
        V_accross_R1=total_current*self.R1
        current=total_current*(self.R2/(self.R3+self.R4+self.R2))
        #if(self.R2==110):
        voltage_drop2=current*self.R3
        T_voltage=self.voltage-V_accross_R1-voltage_drop2
        self.pred_volatage=T_voltage
        self.pred_curre=current

    def compute_cost(self):
        self.cost=MSE(self.pred_volatage,self.ex_voltage)+MSE(self.ex_curre,self.pred_curre)*100
    def compare(self,Compare):
        if(self.cost>Compare.cost):
            print("NEW BEST FOUND:: with a cost of (",self.cost,") With voltage (",self.pred_volatage,") and current (",self.pred_curre,")")
            return(Compare)
        else:
            return(self)
    def __str__(self):
        out="BEST ANSWER"
        out=out+'R1 : '
        out=out+str(self.R1)
        out=out+' R2 : '
        out=out+str(self.R2)
        out=out+' R3 : '
        out=out+str(self.R3)
        out=out+' R4 : '
        out=out+str(self.R4)
        out=out+" WITH A COST OF : "
        out=out+str(self.cost)
        return(out)

seed(1)

R=[]

for i in range(10000):
    R.append((i+1)*100)


R4=10
BEST=SOl(R[0],R[0],R[0],R[0])
for R1 in (R):
    for R2 in (R):
        for R3 in (R):
                tmp=SOl(2800,R2,R3,R4)
                tmp.compute_cost()
                BEST=BEST.compare(tmp)
print(BEST)
