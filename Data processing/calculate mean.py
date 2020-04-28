import pandas as pd
import os
import numpy as np

data=pd.read_csv("C:/Users/hebin/OneDrive/merge/realtime.csv")

list1=data.values.tolist()
n=0
sumlist=np.zeros((len(list1),24,15),dtype=float)
meanlist=np.zeros((len(list1),24,15),dtype=float)
z=0
for i in range(0,len(list1)):
    # days
    for j in range(0,24):
        #24 hours0
        for p in range(0, 15):
            for k in range(0, 12):
                n=p+(k*15)+(j*15*12)+(i*24*15*12)
                sumlist[i][j][p] += float(list1[n][3])
                print("n={}".format(n))
                print(list1[n][3])
            print("sum={}".format(sumlist[i][j][p]))
            meanlist[i][j][p]=sumlist[i][j][p]/12
            z=z+1
            print("mean={}".format(meanlist[i][j][p]))

print(z)
save_path = "C:/Users/hebin/OneDrive/merge"
save_name = "merge_realtime.csv"
b=[]
for i in range(0,len(list1)):
    #92 days
    for j in range(0,24):
        #24 hours
        for p in range(0, 15):
            b.append(meanlist[i][j][p])

df = pd.DataFrame(b)
df.to_csv(save_path + '\\' + save_name ,encoding="utf_8",index=False, header=False, mode='a+')




