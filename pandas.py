import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

from scipy import cluster

#style.use("fivethirtyeight")
'''data1={'x':[3,4,5,6],'y':[5,6,7,8],'z':[7,6,8,5]}
data2={'x':[3,4,5,6],'y':[5,6,7,8],'z':[7,6,8,5]}
df1=pd.DataFrame(data1, index=["a","b","c",'d'])
df2=pd.DataFrame(data2, index=["a","b","c",'d'])
merge=pd.merge(df1,df2, on='x')
print(merge)


df1=pd.DataFrame({'x':[3,4,5,6],'y':[5,6,7,8],'z':[7,6,8,5]}, index=[2000,2001,2002,2003])
df2=pd.DataFrame({'x':[3,4,5,6],'y':[5,6,7,8],'z':[7,6,8,5]}, index=[2004,2005,2006,2007])
merge=pd.merge(df1,df2, on='x')
print(merge)

df1=pd.DataFrame({'x':[3,4,5,6],'y':[5,6,7,8],'z':[7,6,8,5]}, index=[2000,2001,2002,2003])
df2=pd.DataFrame({'a':[3,4,5,6],'b':[6,4,3,2],'c':[7,6,8,5]}, index=[2000,2001,2002,2003])
joined=df1.join(df2)
print(joined)

data1={'x':[3,4,5,6],'y':[5,6,7,8],'z':[7,6,8,5]}
data2={'x':[3,4,5,6],'y':[5,6,7,8],'z':[7,6,8,5]}
df1=pd.DataFrame(data1, index=["a","b","c",'d'])
df2=pd.DataFrame(data2, index=["a","b","c",'d'])
concat=pd.concat([df1,df2])
print(concat)
df1.set_index("x", inplace=True)
df1=df1.rename(columns={'y':'second'})
print(df1)'''

'''x=pd.read_csv("F:\Python\data.csv")
df=pd.DataFrame(x)
df=df.head(5)
#df.to_html('jus.html')
df.set_index("Duration", inplace=True)
df=df.reindex(columns={'Pulse','Maxpulse'})
print(df.to_string())
df.diff(axis=1)
df.plot(kind='bar')
plt.show()
print(df.to_string())'''

'''
from statistics import mean, median, mode, variance
print(mean([1,2,3,4]))
print(mode([1,2,3,3,4]))
print(median([1,2,6,3,4]))
print(variance([1,2,6,3,4]))'''

'''from scipy import special
##help(cluster)
a=special.exp10(2)
b=special.exp2(3)
print(a,b, sep= '\n')
c=special.sindg(90)
d=special.cosdg(90)
print(c,d, sep='\n')'''

'''from scipy import integrate
from scipy import special
i=integrate.quad(lambda x:special.exp10(x),0,1) #integration of single variable
print(i)

e=lambda x,y:x*y**2
f=lambda x:1
g=lambda x:-1
i=integrate.dblquad(e,0,1,f,g)
print(i)'''

'''from scipy.fftpack import fft,ifft
import numpy as np
x=np.array([1,2,3,4])
y=fft(x)
z=ifft(x)
print(y)
print(z)'''
from scipy import linalg
import numpy as np
a=np.array([[1,2],[3,4]])
b=linalg.inv(a)
print(b)
print(b*a)
