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

    # Check the percentage
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculates the difference and the percentage"""
    # Calculate the difference and percentage
    difference = value - limit
    percent = (value / limit) * 100

     # Return both results
    return difference, percent

    
    # Display the report heading
def print_report(label, value, limit, difference, percent, status):
    """Prints the report with borders"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")    
    print("=" * 34)

    # Display the record details
    print(f" Value      : {value:.2f}")
    print(f" Limit      : {limit:.2f}")
    print(f" Difference : {difference:+.2f}")
    print(f" Percent    : {percent:.2f}%")
    print(f" Status     : {status}")

    print("=" * 34)


# Start the OVER LIMIT counter
over_limit_count = 0

# Keep asking for records until the user enters quit
while True:

    # Ask for a label
    label = input("Enter label (a name, a hostname, an IP or type quit to stop): ")
    
    # Stop the loop if the user enters quit
    if label == "quit":
        break

    # Ask for the value and limit
    value = float(input("Enter value: "))
    limit = float(input("Enter limit: "))

    # Call the functions to calculate the results
    difference, percent = check(value, limit)
    status = status_of(percent)

    # Count the OVER LIMIT records
    if status == "OVER LIMIT":
        over_limit_count += 1

    # Call the function to display the report
    print_report(label, value, limit, difference, percent, status)

# Display the total number of OVER LIMIT records
print(f"Total OVER LIMIT records: {over_limit_count} ")




