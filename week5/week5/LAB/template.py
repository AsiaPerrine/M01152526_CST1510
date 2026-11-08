"""
RECORD CHECK  -  my version
===========================

Name  :  Perrine Asia
Lane  :  Cyber
Date  : 22.10.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# Create a class to store record information
class Record:
    """Store a label, value, and limit"""

    # Count how many records are over the limit
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Set record's label, value, and limit"""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT, WARNING, or OK based on percentage"""
        # Calculate the percentage
        percent = (self.value / self.limit) * 100
         # Check the percentage and return the status
        if percent >= 100:
            Record.over_limit_count += 1   
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Read a records.txt file and return a list of Record objects"""
    # Create an empty list for the records
    records = []
    # Read each record from the file
    with open(path) as f:
        for line in f:
            # Separate the label, value, and limit
            label, value, limit = line.strip().split(",")
            # Create a Record object and add it to the list
            records.append(Record(label, float(value), float(limit))) 
    return records

# Load the records from the text file
records = load_records("LAB\\records.txt")

# Start the over-limit counter
over_count = 0 
# Check each record and display its report
for record in records:
    s = record.status()

    # Count records that are over the limit
    if s == "OVER LIMIT":
        over_count += 1   

    # Display the record details
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  Value  : {record.value}")
    print(f"  Limit  : {record.limit}")
    print(f"  Status : {record.status()}")

    print("=" * 34)

# Display the total number of over-limit records
print()
print(f"Total OVER LIMIT: {over_count}")

