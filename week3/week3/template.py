"""
RECORD CHECK  -  my version
===========================

Name  : Perrine Asia
Lane  : Cyber 
Date  : 8/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ===================================================================

def status_of(percent):
    """Returns status based on percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculates the difference and the percentage"""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Prints the report with borders"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")    
    print("=" * 34)
    print(f" Value      : {value:.2f}")
    print(f" Limit      : {limit:.2f}")
    print(f" Difference : {difference:+.2f}")
    print(f" Percent    : {percent:.2f}%")
    print(f" Status     : {status}")
    print("=" * 34)


over_limit_count = 0
while True:
 
    label = input("Enter label (a name, a hostname, an IP or type quit to stop): ")
    if label == "quit":
        break

    value = float(input("Enter value: "))
    limit = float(input("Enter limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(label, value, limit, difference, percent, status)

print(f"Total OVER LIMIT records: {over_limit_count} ")




