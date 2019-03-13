import csv
import os
with open("grid.csv",'r') as myfile:
    rc=csv.reader(myfile)    
    for i in rc:
        x=-1
        for j in i:
            if x==-1:
                x=int(j)
            elif x>=0:
                x=x+int(j)

        b=x
        print(b)

    
            


        



