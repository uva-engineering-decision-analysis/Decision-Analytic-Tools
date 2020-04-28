#%%
import pandas as pd
import os
read_path =  "C:/Users/hebin/OneDrive/realtime"
save_path =  "C:/Users/hebin/OneDrive/merge"
save_name = "merge_realtime.csv"
os.chdir(read_path)
csv_name_list = os.listdir()
for i in range(0,len(csv_name_list)):
    df = pd.read_csv(csv_name_list[i])
    list=df.values.tolist()
    j = 0
    while j < len(list):
        if (list[j][3] < 0):
            list[j][3] = abs(list[j][3])
        if (int(list[j][0][15:16]) % 5 != 0) | (int(list[j][0][17:18]) % 5 != 0) | (int(list[j][0][18:19]) % 5 != 0):
            del list[j]
        else:
            j += 1
    if (j!=4320):
        print(list[1][0])
        print(j)
    df = pd.DataFrame(list)
    df.to_csv(save_path + '\\' + save_name ,encoding="utf_8",index=False, header=False, mode='a+')
