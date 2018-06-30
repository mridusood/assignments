import pandas as pd
import numpy as np
#Q1

data={'name':['richa'],'age':[20],'mail id':['richasood120@gmail.com'],'phone no.':[558192044]}
df=pd.DataFrame(data)
print(df)
print("\n \n after adding information of my friend ")
df.loc[1]=['abc',22,'abc98@gmail.com',7647864782]
print(df)


#Q2
data=pd.read_csv("data.csv")
df=pd.DataFrame(data)
print("first five rows of data frame are")
print(df.head(5))
print("first ten rows of data frame are")
print(df.head(10))
print("basic statics are")
print("axes\n"+str(df.axes))
print("datatypes\n"+str(df.dtypes))
print("dimension\n"+str(df.ndim))
print("shape\n"+str(df.shape))
print("size\n"+str(df.size))
print("last 5 rows are")
print(df.tail(5))

x=df.loc[:,'Location']
print(x)
print("basic statics are")
print("axes\n"+str(x.axes))
print("datatypes\n"+str(x.dtypes))
print("dimension\n"+str(x.ndim))
print("shape\n"+str(x.shape))
print("size\n"+str(x.size))