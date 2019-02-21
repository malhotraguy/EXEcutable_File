import pandas as pd
import sys
df = pd.read_csv('employees.dat', sep='\t',header=None)
#print(df)
#df2=df[df[0].map(startswith("#"))]
df2=df[df[0].map(lambda x: not x.startswith("#"))]
#df2.remove_index()
df2.reset_index(drop=True,inplace=True)
#print(df2)
#print(list(df2[0]))
df2_list=list(map(lambda x:x.split(","),list(df2[0])))
#print(df2_list)
sortedby_Id=sorted(df2_list, key=lambda tup: tup[0])

#print(sortedby_Id)
for Id in sortedby_Id:
    #sys.stdout.write(str(Id).strip("[ ]"))  # same as print
    #sys.stdout.flush()
    print(str(Id).strip("[ ]"),"\n",flush=True)

#print(df2[0])
