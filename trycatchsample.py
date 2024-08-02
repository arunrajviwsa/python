try:
    num1=int(input("Enter the number 1:"))
    num2=int(input("Enter the number 2:"))
    result=num1/num2
    print(num1,"/",num2,"=",result)
    x=[1,2,5,8,3,8]
    x[len(x)]=67
    print(x)
except ZeroDivisionError:
    print("Dinominator cannot be zero")
except IndexError:
    print("Error: Index you are using is not presentin the list, use insert method or check the index position")
finally :
    print("The program is ended")

