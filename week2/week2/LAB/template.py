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
overLimit = 0

while True:
    label = input("Enter a Label (name,hostname or an IP) or quite to stop: ")  
    if label == "quit":
        break   

    value = float(input("Enter Number: "))
    limit = float(input("Enter Second Number: "))

    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    if status == "OVER LIMIT":
        overLimit += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Label      : {label}")
    print(f"Value      : {value}")
    print(f"Limit      : {limit}")
    print(f"Difference : {difference:>+10.2f}")
    print(f"Percentage : {percent:>10.2f}%")
    print(f"Status     : {status}")

    print("=" * 34)
#total over limit
print(f"Total OVER LIMIT : {overLimit}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
