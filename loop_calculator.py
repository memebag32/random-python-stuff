

print("This program provides the functionality of a four-function calculator.\n"
      "The program will take two user-generated numbers and one of the four basic arithmetic operations\n"
      "(addition, subtraction, multiplication, and division), then perform the desired operation on the\n"
      "two numbers.\n")

num1 = int(input("Please enter your first number on the line below.\n"))

op = input("Please enter your desired operation.\n"
           "For addition please input: +\n"
           "For subtraction please input: -\n"
           "For multiplication please input: *\n"
           "For division please input: /\n")

num2 = int(input("Please enter your second number on the line below.\n"))

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    num1 = input
    num1 = input
    for num1 in range(0, num2, 1):
        print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
        num1 = input
        num1 = input
        while num1 < 10:
            print(num1)
        num2 = num1 - 1
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print(f"Operation: {op} is not supported.")
int("")
print(f"\nThank you for using the four-function calculator.\n")