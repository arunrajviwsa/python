"""yob=int(input("Enter the year of birth"))
age=2024-yob
if age < 18:
    raise Exception(f'Entry age for the PG program is greater than 18 for the Year 2024')

"""
def divide(x,y):
    try:
        if y==0:
            raise ZeroDivisionError("Cannot Divide by zero")
        result=x/y
        return result
    except (ZeroDivisionError,AssertionError) as e:
        print("Error",e)
    except TypeError as e:
        print("Error", e)
    except:
        print("System Error")
divide(10,'w')
