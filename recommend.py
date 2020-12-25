import pandas as pd
import numpy as np
from datetime import time
from datetime import datetime
df=pd.read_csv("data.csv",usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16),dtype = {"key":"double","mode":"double"})
df.head()
cols = list(df)
cols[14], cols[0] = cols[0], cols[14]
df = df.ix[:,cols]
cols = list(df)
cols[15], cols[1] = cols[1], cols[15]
df = df.ix[:,cols]
df.head()
df.drop(columns = ['duration_ms'], inplace = True)
df.drop(columns = ['artist'], inplace = True)
df.drop(columns = ['target'], inplace = True)
df.drop(columns = ['time_signature'], inplace = True)
df.head()
mrow1=df["energy"].mean()
mrow2=df["instrumentalness"].mean()
mrow3=df["key"].mean()
mrow4=df["liveness"].mean()
mrow5=df["loudness"].mean()
mrow6=df["mode"].mean()
mrow7=df["speechiness"].mean()
mrow8=df["tempo"].mean()
mrow9=df["valence"].mean()
mrow10=df["acousticness"].mean()
mrow11=df["danceability"].mean()
Mrow1=df["energy"].max()
Mrow2=df["instrumentalness"].max()
Mrow3=df["key"].max()
Mrow4=df["liveness"].max()
Mrow5=df["loudness"].max()
Mrow6=df["mode"].max()
Mrow7=df["speechiness"].max()
Mrow8=df["tempo"].max()
Mrow9=df["valence"].max()
Mrow10=df["acousticness"].max()
Mrow11=df["danceability"].max()
arow1=df["energy"].min()
arow2=df["instrumentalness"].min()
arow3=df["key"].min()
arow4=df["liveness"].min()
arow5=df["loudness"].min()
arow6=df["mode"].min()
arow7=df["speechiness"].min()
arow8=df["tempo"].min()
arow9=df["valence"].min()
arow10=df["acousticness"].min()
arow11=df["danceability"].min()
for i in range(2014):
    df.at[i,"energy"] = (df.at[i,"energy"]-mrow1)/(Mrow1-arow1)
    df.at[i,"instrumentalness"] = (df.at[i,"instrumentalness"]-mrow2)/(Mrow2-arow2)

    x= df.at[i,"key"]
    x = (x-mrow2)/(Mrow2-arow2)
    df.at[i,"key"]=x
   
    
    
    df.at[i,"liveness"] = (df.at[i,"liveness"]-mrow4)/(Mrow4-arow4)
    df.at[i,"loudness"] = (df.at[i,"loudness"]-mrow5)/(Mrow5-arow5)
    df.at[i,"mode"] = (df.at[i,"mode"]-mrow6)/(Mrow6-arow6)
    df.at[i,"speechiness"] = (df.at[i,"speechiness"]-mrow7)/(Mrow7-arow7)
    df.at[i,"tempo"] = (df.at[i,"tempo"]-mrow8)/(Mrow8-arow8)
    df.at[i,"valence"] = (df.at[i,"valence"]-mrow9)/(Mrow9-arow9)
    df.at[i,"acousticness"] = (df.at[i,"acousticness"]-mrow10)/(Mrow10-arow10)
    df.at[i,"danceability"] = (df.at[i,"danceability"]-mrow11)/(Mrow11-arow11)

df.drop_duplicates(subset="song_title",keep=False,inplace=True)
df.head()
df8=df.transpose()

new_df=df8.reset_index(drop=True)
headers = new_df.iloc[0]
new_df4 = pd.DataFrame(new_df.values[1:], columns=headers)
new_df4.head()
sel=[]
tem=[]
def a(final,number,y1):
    f=open("selected.txt","rt")
    
    b=datetime.time(datetime.now())
    x=b.strftime("(%H:%M:%S.%F)")
    x=x[1:len(x)-1]

    y=x.split(":")
    
    for t in f:
        s=t
    sel=[]
    for j in new_df4[s]:
        sel.append(j)
    w1=[]
    if(number>0):
        for j in new_df4[ final[0] ]:
            w1.append(j)
        w1=np.asarray(w1)
        w=np.asarray(sel)
        similar=np.corrcoef(w1, w)
        if( (int(y[0])-int(y1[0]))>6 and similar[0][1]<0.3):
            number=0
        else:
            sel=b(final,sel)
    number=number+1
    tem=[]
    final=[]
    val=[]
    f=0
    for i in new_df4.columns:
        tem=[]
        for j in new_df4[i]:
            tem.append(j)
        tem=np.asarray(tem)
        co=np.corrcoef(tem, sel)
        x=co[0][1]
        if(f<5):
            final.append(i)
            val.append(x)
            f=f+1
        elif(val[4]<x):
            val[4]=x
            final[4]=i
        final,val=sort(final,val)
    
    return final,y 
    
def b(final,sel):
    sel1=[]
    for j in new_df4[ final[0] ]:
        sel1.append(j)
    sel=sel1+sel
    sel=sel/2
    sel1=np.asarray(tem)
    return sel1   
def sort(f,v):
    for i in range(len(f)):
        for j in range(len(f)-1):
            if(v[j]<v[j+1]):
                temp=v[j]
                temp1=f[j]
                
                v[j]=v[j+1]
                f[j]=f[j+1]
                
                v[j+1]=temp
                f[j+1]=temp1
    return f,v
def store(final,number):
    from xlwt import Workbook
    wb=Workbook()
    sheet1=wb.add_sheet('Sheet 1')
    sheet1.write(1,0,final[0])
    sheet1.write(2,0,final[1])
    sheet1.write(3,0,final[2])
    sheet1.write(4,0,final[3])
    sheet1.write(5,0,final[4])
    wb.save('rec12.xls')
number=0
final=[]
y1=[]

final,y1=a(final,number,y1)
store(final,number)
b=datetime.time(datetime.now())
x=b.strftime("(%H:%M:%S.%F)")
x=x[1:len(x)-1]

y=x.split(":")
file = open(r"output.txt", "w+")
file.write(final[0] + '\n'+final[1] + '\n'+final[2] + '\n'+final[3] + '\n'+final[4] )
file.close