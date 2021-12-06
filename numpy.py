import numpy as np;
import matplotlib.pyplot as plt;
"""arr=np.array([[1,2,3],[5,6,7]])
brr=np.array([(1,2,3),(4,5,6)])
crr=np.array([[1,2,3],[5,6,7],[8,9,4]])
err=np.array([[[2,3,4],[5,6,7]],[[1,2,3],[4,5,6]]])
print(arr)
print(brr)
s=np.arange(1000)
e=np.arange(1000)
print(s+e)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.reshape(3,2))
print(arr[0][1])
print(arr[0,2])
print(arr[0:,2])
print(crr[0:,2])
print(crr[0:2,2])
drr=np.linspace(1,3,5)
print(drr)
print(err)
print(err.ndim)
print(err.shape)
print(err[0][1][1])"""

"""arr=np.array([[1,2,3],[4,5,6]])
brr=np.array([[1,2,3],[4,5,6]])
print(arr.max())
print(arr.min())
print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))
print(np.sqrt(arr))
print(np.std(arr))
print(np.mean(arr))
print(np.median(arr[0]))
print(arr+brr)
print(arr-brr)
print(arr*brr)
print(arr/brr)
print(np.vstack((arr,brr)))
print(np.hstack((arr,brr)))
print(np.max(arr))
print(arr.ravel())"""

"""x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
p=np.tan(x)
plt.plot(x,y)
plt.plot(x,z)
plt.show()

arr=np.array([[1,2,3],[4,5,6]])
print(np.exp(arr))
print(np.log(arr))
print(np.log10(arr))
print(np.log2(arr))"""

"""arr1=np.array([4,5,6,7])
#arr2=arr1
#arr2=arr1.view()
arr2=arr1.copy()
print(arr2)
print(id(arr1))
print(id(arr2))"""

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.array([[1,2,3],[4,8,6],[6,8,9]])
arr3=arr1*arr2
#m=np.matrix(arr)
m1=np.matrix('1 2 3;4 5 6;7 8 9')
m2=np.matrix('1 2 3;4 8 6;6 8 9')               #see the difference between matrix n array multiplication
m3=m1*m2
y=np.diagonal(m1)
print(m1)
print(y)
print(m3)
print(arr3)



