#maximum and minimum element in the Given array
import numpy as np
#Creating 5*4 array
array=np.arange(20).reshape(5,4)
print(array)
print(np.argmax(array))
print(np.argmax(array,axis=1))
print(np.argmax(array,axis=0))
print(array[np.argmax(array,axis=1)])
print(array[np.argmax(array,axis=0)])

array1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array1)
print(np.sort(array1,axis=None))
print(np.sort(array1,axis=1))
print(np.sort(array1,axis=0))

list=[np.array([2,4,5,6]),np.array([4,6,8,9]),np.array([2,7,8,3]),np.array([4,8,2,5])]
result=[]
for i in range(len(list)):
  result.append(np.mean([list[i]]))
print(result)
newrow=np.array([10,11,12])
newarray=np.vstack((array1,newrow))
print(newarray)

