print("Step1")
print("Step2")
print("Step3")

# if True:
# print("Hello")
# try:
#     print(7/0)
# except ZeroDivisionError:
#     print("You cannot divide any number by 0")

# try:
#     print(int("the world"))
# except ValueError:
#     print("Invalid Conversion!")

# try:
#     print("Hello"+"123")
#     print(int("hello")) 
# except ValueError:
#     print("Invalid Conversion!")
# except TypeError:
#     print("Invalid expression")

try:
    inp1=int(input("Enter your number1: "))
    inp2=int(input("Enter your number2: "))
    print(inp1/inp2)
except ZeroDivisionError:
    print("Invalid Expression!")
except ValueError:
    print("Invalid Value Given!")
finally:
    print("operation Over~")


print("Final Step")