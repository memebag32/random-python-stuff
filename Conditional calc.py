
print("Hello this program is ment to be a conditional calculator")
num1 = input("Put your first number\n")
op = input("Put your operation\n")
"+: Addition\n"
"-: Subtraction\n"
"*: Multiplication\n"
"/: Division\n"
num2 = input("Put your second number\n")

num1 = int(num1)
num2 = int(num2)

if op == "+":
    print(f"addition: {num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"addition: {num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"addition: {num1} * {num2} = {num1 * num2}")
elif op == "/":
    print(f"addition: {num1} / {num2} = {num1 / num2}")
if op == "minus":
    print("sorry that operation is not supported")

print("Thank you for using conditional calculator")





