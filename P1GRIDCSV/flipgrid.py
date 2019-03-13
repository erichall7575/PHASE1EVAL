import csv
import os
with open("grid.csv",'r') as myfile:
    rc=csv.reader(myfile)    
    for i in rc:
        newlist=i[::-1]
        with open("normgrid.csv","a") as newfile:
            wc=csv.writer(newfile)
            wc.writerow(newlist)
          
with open('normgrid.csv', 'r') as textfile:
    for row in reversed(list(csv.reader(textfile))):
        
        n=', '.join(row)
        n=n+"\n"
        with open('flipgrid.csv','a') as flipfile:
            
            flipfile.write(n)

