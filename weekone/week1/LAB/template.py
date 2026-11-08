"""
RECORD CHECK  -  my version
===========================

Name  : Perrine Asia
Lane  : Cyber      
Date  : 25/06/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
""""Calculate and print difference and percentage"""
# ask the user to enter a label and two numbers
label = input("Enter a Label: ")
first = float(input("Enter a Number:"))
second = float(input("Enter a Second Number: "))

# calculate the difference and percentage
difference = first - second
percentage = (first / second) * 100

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# display the results with two decimal places
print(f"Label      : {label:>10}")
print(f"First      : {first:>10.2f}")
print(f"Second     : {second:>10.2f}")
print(f"Difference : {difference:>+10.2f}")
print(f"Percentage : {percentage:>10.2f}")

print("=" * 34)

