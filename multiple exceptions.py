try:
    num1,num2=eval(input("Enter 2 numbers, separated by a coma: "))
    result=num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("division by zero is an error!!")
except SyntaxError:
    print("Comma is missing. Enter 2 numbers seperated by a coma like this (1,2)")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")