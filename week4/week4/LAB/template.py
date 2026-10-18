"""
RECORD CHECK  -  my version
===========================

Name  : Perrine Asia
Lane  :  Cyber
Date  : 15.10.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# ================================================================


def check_record(value, limit):

    """Calculates the difference, percentage and status."""

    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # Send all three results back to the main program
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Prints the report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f" Value      : {value:.2f}")
    print(f" Limit      : {limit:.2f}")
    print(f" Difference : {difference:+.2f}")
    print(f" Percent    : {percent:.2f}%")
    print(f" Status     : {status}")
    print("=" * 34)




def load_records(path):
    """Reads records from a file and returns a list of dictionaries."""

    # Create an empty list to store all the records
    records = []

    # Open the file in read mode "r"
    # Python closes the file automatically when the block ends
    with open(path, "r") as file:

        # Read the file one line at a time
        for line in file:

            # Remove whitespace and split the line at each comma
            label, value, limit = line.strip().split(",")

            # Create a dictionary to store one record
            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }

            # Add this dictionary to the records list
            records.append(record)

    return records





# Start the counter at zero
over_limit_count = 0

try:
    # Read all records from file
    records = load_records("LAB\\records_sample.txt")

    # Open results.txt in write mode "w"
    # This creates the file or replaces its previous contents
    with open("results.txt", "w") as output_file:

        # Process each record in the list
        for record in records:

            # Get the values from the dictionary
            label = record["label"]
            value = record["value"]
            limit = record["limit"]

            # Calculate the difference, percentage and status
            difference, percent, status = check_record(value, limit)

            # Print the report for this record
            print_report(
                label, value, limit,
                difference, percent, status
            )

            
            if status == "OVER LIMIT":
                over_limit_count += 1

            output_file.write(f"{label}, {status}\n")

    # Print the total after all records have been processed
    print(f"\nTotal OVER LIMIT records: {over_limit_count}")

    # Tell the user where the results have been saved
    print("Results saved to results.txt")

# Handle the error if the input file cannot be found
except FileNotFoundError:
    print("Error: LAB/records_sample.txt was not found.")
    print("Check that the LAB folder and file exist.")


