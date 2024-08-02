import numpy as np
inputarray=np.array([[0,0,0],[0,0,0],[0,0,0]])
print(inputarray.shape)
def playera():
    inputValue = input("Player 1's Turn (Row,Column)")
    print(inputValue)
for char in inputValue:
    if char != '':
        print(char)
for i in range(inputarray.shape[0]):  # Loop over rows
    for j in range(inputarray.shape[1]):  # Loop over columns
        for char in inputValue:
            if char != '':

        inputarray[i, j] =1

print(inputarray)
"""for i in range()
    new_arr = np.insert(inputarray, 2, 10)
print(np.argmax(inputarray,axis=0))
print(np.argmax(inputarray,axis=1))"""