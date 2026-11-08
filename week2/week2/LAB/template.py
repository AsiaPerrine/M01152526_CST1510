"""
RECORD CHECK  -  my version
===========================

Name  :  Perrine Asia
Lane  :  Cyber
Date  : 02/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== 
# Start the OVER LIMIT counter
overLimit = 0

# Keep checking records until the user types quit
while True:
    # Ask the user to enter a label
    label = input("Enter a Label (name,hostname or an IP) or quit to stop: ")  
     # Stop the loop if the user enters quit
    if label == "quit":
        break   

    # Ask for the value and limit
    value = float(input("Enter Number: "))
    limit = float(input("Enter Second Number: "))

    # Calculate the difference and percentage
    difference = value - limit
    percent = (value / limit) * 100

    # Decide the status based on the percentage
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # Count records that are OVER LIMIT
    if status == "OVER LIMIT":
        overLimit += 1
    # Display the report
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    # Display the record details
    print(f"Label      : {label}")
    print(f"Value      : {value}")
    print(f"Limit      : {limit}")
    print(f"Difference : {difference:>+10.2f}")
    print(f"Percentage : {percent:>10.2f}%")
    print(f"Status     : {status}")

    print("=" * 34)
# Display the total number of OVER LIMIT records
print(f"Total OVER LIMIT : {overLimit}")



