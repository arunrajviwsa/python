#numpy -Numerical Python library


#advantages of Numpy
#More speed,fewer loops,clearer code,better quality,
"""import numpy as np
digits =np.array([[1,2,3],[4,5,6],[7,8,9]])
print(digits)
print(digits.shape)
row_vector=digits[:,np.newaxis]
print(row_vector,"Row vector")
row_vector1=digits[np.newaxis:]
print(row_vector1,"Row vector1")
row_vector2=digits[np.newaxis]
print(row_vector2,"Row vector2")"""

import numpy as np
curve_center=80
grades =np.array([72,35,64,98,35,17,65])
def curve(grades):
    average= grades.mean();
    print("average",average)
    change = curve_center -average
    print("change", change)
    new_grade =grades +change
    print("new grades ", new_grade)
    print("grades ", grades)
    return np.clip(new_grade,grades,100)
print(curve(grades))

"""temp =np.array([29.3,45.5,23,45,18,23.9,67,78,56,34]).reshape(2,2,3)
print(temp)
print("*"*60)"""
batting_averages= np.array([[50,60,80,90],[70,60,80,20],[10,60,55,90],[78,86,35,67]])
print(batting_averages)
print("size of the array",batting_averages.shape)
print("Maximum Average",batting_averages.max())
print("Maximum Average Column",batting_averages.max(axis=0))#column
print("Maximum Average Row",batting_averages.max(axis=1))#row
"""numbers= np.linspace(5,50,23,dtype=int).reshape(6,8)
print(numbers)
numbers1= np.arange(48).reshape(6,8)
print(numbers1)
print(numbers+numbers1)"""
arr1=np.arange(10,100,5,dtype=int).reshape(3,6)
arr2=np.arange(10,100,5,dtype=int).reshape(3,6)
print("sum",arr1+arr2)
square= np.array([[3,5,6,7],[2,8,5,3],[2,5,4,2],[6,9,7,8]])


for i in range(4):
    print("Values",i)
    print(square[:i].sum()==6)
print(square[:2,:2])
print(square[2:,0:])
numbers= np.linspace(5,50,24,dtype=int).reshape(4,-1)
print(numbers)
print(numbers.T)
mask=numbers%5==0
print("All valaues divide by 5",numbers[mask])
print("All valaues divide by 8",numbers[numbers%8==0])

print("Horizonal Sorting",np.sort(numbers,axis=0))
print("Vertical Sorting",np.sort(numbers,axis=1))
a=np.array([[4,8],[6,1]])
b=np.array([[3,5],[7,2]])
print("a",a)
print("b",b)
print(np.concatenate((b,a)),"Merging two array")
print(np.concatenate((b,a),axis=None),"Merging two array with axis")
print(np.hstack((b,a)))
print(np.vstack((b,a)))







