"""
Filename: Average_calc.py
Author: Chrobak, Walter>
Created: <10/31/2025>
Instructor: Holtslander
"""

sum = 0
entries = 0

again = "y"
while again == "y":
    num = int(input("Enter a number.\n"))
    sum = sum + num
    entries = entries + 1
    print(f"Current sum is {sum}")
    print(f"Current number of entries is {entries}")
    print(f"Current average is {sum / entries}")
    again = input("Would you like to enter another one? (y/n).\n")






























