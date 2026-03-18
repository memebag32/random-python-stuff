"""
Filename: average_calculator_2.py
Created: <03/12/2026>
"""

lst = []
while True:
    op = input("Please select your desired operation by typing the number, then pressing \"enter\"\n"
               "Fill out the rest of the options here\n"
               "1) Add a number to the list\n"
               "2) Remove a number from the list\n"
               "3) Compute the average value of the list\n"
               "4) Print the list\n"
               "5) Exit the program. !WARNING! all data will be erased!\n")
    if op == "1":
        lst.append(int(input("Enter the number you want to the list.\n")))
    elif op == "2":
        lst.remove(int(input("Enter the number you want gone.\n")))
    
    elif op == "3":
        numbers = (lst)
        sum = 0
        for n in numbers:
             sum = sum + n

        print(sum / len(numbers))
    
    elif op == "4":
        print(lst)

    elif op == "5":
        break
    else:
        print(f"{op} is not a supported operation! Try again.\n")
print("Thank you for using this average calculator!")