#Try Except and finally - Architecture Structure
#Sintax: try: except: finally:
#Utility: Error handling
#Example: 
import traceback, os, sys #Traceback is a module that allows us to get the line where the error is located
from PackageTest.module import Title #Importing the module
import PackageTest #Importing the package

def calculation(a,b):
    c = a/b
    return c

def evaluateResult(x):
    if type(x) == float:
        return f"Float: {format(float(x), '.4f')}"
    elif type(x) == int:
        return f"Integer: {int(x)}"

def inputTwoNumbers():
    a = int(input("Type a number: "))
    b = int(input("Type another number: "))
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero") #Raaise the error and stop the program
    return a,b

try:
    print(Title)
    PackageTest.Advice()
        
    n1, n2 = inputTwoNumbers()
    result = evaluateResult(calculation(n1, n2)) #Trying to use nested functions

    print(f"Hello This is the result of the division {n1}/{n2} = {result}")

except ZeroDivisionError as ZeroError: #This is the specific error
    print(f'Error: {ZeroError.__class__.__name__} - Message: {ZeroError} - Line: {traceback.extract_tb(ZeroError.__traceback__)[0][1]}')
    result = None #This is the same as c = 0    
    
except Exception as e: #This is the general error
    print(f"Something went wrong - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")

finally:
    print("This is the end of the program")
    delay = input("Press any key to continue...")
    os.system("cls")
    sys.exit()
