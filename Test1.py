import pandas as pd
df = pd.read_csv('employees.dat', sep='\t',header=None)
df2=df[df[0].map(lambda x: not x.startswith("#"))]
df2.reset_index(drop=True,inplace=True)
df2_dict=dict(map(lambda x:x.split(","),list(df2[0])))
Ids=df2_dict.items()
Ids=sorted(Ids)
Ids=list(map(lambda x:[x[0],x[1].split()],Ids ))
last_names=sorted(Ids,key=lambda inlis:inlis[1][1])
def Sortedby_id():
    f = open('Sortedby_id.txt', 'w')
    print("Processing by employee number...")
    for id in Ids:
        toWrite =id[0]+","+id[1][0]+" "+id[1][1]+"\n"
        # write to the file
        f.write(toWrite)
        print(id[0]+","+id[1][0]+" "+id[1][1],flush=True)
    f.close()
def Sortedby_last_name():
    f = open('Sortedby_last_name.txt', 'w')
    print("Processing by last (family) Name...")
    for id in last_names:
        toWrite =id[0]+","+id[1][0]+" "+id[1][1]+"\n"
        # write to the file
        f.write(toWrite)
        print(id[0] + "," + id[1][0] + " " + id[1][1],flush=True)
    f.close()

Sortedby_id()
Sortedby_last_name()