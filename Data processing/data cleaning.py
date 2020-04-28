import pandas as pd
import os
read_path =  "C:/Users/hebin/OneDrive/error"
save_path =  "C:/Users/hebin/OneDrive/merge"
save_name = "replace.csv"
os.chdir(read_path)
csv_name_list = os.listdir()

z=0
for k in range(0,len(csv_name_list)):
    df = pd.read_csv(csv_name_list[k])
    list = df.values.tolist()
    for i in range(0,24):
        for j in range (0,12):
            t=0
            point=0
            x=j*5
            while(t<len(list)):
                if (int(list[t][0][11]) * 10 + int(list[t][0][12]) == i) & (int(list[t][0][14]) * 10 + int(list[t][0][15]) == x):
                    t = len(list)
                    point = 1
                else:
                    t += 1
            else:
                if (point==0):
                    print(csv_name_list[k])
                    print(i)
                    print(x)




