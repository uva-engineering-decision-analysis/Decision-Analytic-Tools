import pandas as pd
import os
read_path =  "C:/Users/hebin/OneDrive/predicted"
save_path =  "C:/Users/hebin/OneDrive/merge"
save_name = "predicted.csv"

os.chdir(read_path)
csv_name_list = os.listdir()

for i in range(0,len(csv_name_list)):
    df = pd.read_csv(csv_name_list[i])
    list=df.values.tolist()
    df = pd.DataFrame(list)
    df.to_csv(save_path + '\\' + save_name, encoding="utf_8", index=False, header=False, mode='a+')
