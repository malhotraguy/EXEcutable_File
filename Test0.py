import pandas as pd
import os
import sys
df = pd.read_csv('employees.dat', sep='\t',header=None)
#print(df)
#df2=df[df[0].map(startswith("#"))]
df2=df[df[0].map(lambda x: not x.startswith("#"))]
#df2.remove_index()
df2.reset_index(drop=True,inplace=True)
#print(df2)
#print(list(df2[0]))
df2_dict=dict(map(lambda x:x.split(","),list(df2[0])))

#print(df2_dict)

Ids=df2_dict.items()
#print((Ids))
Ids=sorted(Ids)
Ids=list(map(lambda x:[x[0],x[1].split()],Ids ))
#print(Ids)
last_names=sorted(Ids,key=lambda inlis:inlis[1][1])
#print(last_name)
print("Processing by employee number...")
for id in Ids:
    print(id[0]+","+id[1][0]+" "+id[1][1])

print("Processing by last (family) Name...")
for id in last_names:
    print(id[0] + "," + id[1][0] + " " + id[1][1])

"""sortedby_Id=sorted(df2_dict, key=lambda lis: lis.key())

#print(sortedby_Id)
for Id in sortedby_Id:
    #sys.stdout.write(str(Id).strip("[ ]"))  # same as print
    #sys.stdout.flush()
    #print(str(Id).strip("[ ]"),"\n")
    #os.system("{command here}")
    print(Id[0]+","+Id[1].lstrip())

#print(df2[0])"""
