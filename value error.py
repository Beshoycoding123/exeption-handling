#using a try and exept
try:
    number=int(input("enter a number: "))
    print("the number is ",number)
#using value error
except ValueError as ex:
    print("exeption:",ex)