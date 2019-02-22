import pandas as pd
import os
import time
import sys
file_path = os.getcwd() + "\employees.dat"
print(file_path)
df = pd.read_csv(file_path, sep='\t', header=None)
df2 = df[df[0].map(lambda x: not x.startswith("#"))]
df2.reset_index(drop=True, inplace=True)
df2_dict = dict(map(lambda x: x.split(","), list(df2[0])))
Ids = df2_dict.items()
Ids = sorted(Ids)
Ids = list(map(lambda x: [x[0], x[1].split()], Ids))
last_names = sorted(Ids, key=lambda inlis: inlis[1][1])


def Sortedby_id():
    print("Processing by employee number...")
    for id in Ids:
        print(id[0] + "," + id[1][0] + " " + id[1][1], flush=True)
    time.sleep(1)

def Sortedby_last_name():
    print("Processing by last (family) Name...")
    for id in last_names:
        print(id[0] + "," + id[1][0] + " " + id[1][1], flush=True)
    time.sleep(1)

while(True):
    sel=input("\nEnter 1 to see the sorted list by Employee number\n"+"Enter 2 to see the sorted list by last (family) Name\n"+"Enter 3 to exit\n")
    if sel=="1":
        Sortedby_id()
    elif sel=="2":
        Sortedby_last_name()
    elif sel=="3":
        sys.exit()
    else:
        print("Invalid Selection\n"+"Choose again")
        time.sleep(0.5)



