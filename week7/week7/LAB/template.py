"""
RECORD CHECK  -  my version
===========================

Name  : Perrine Asia
Lane  :  Cyber     
Date  :  06.11.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean a messy record and return a dictionary."""

    # remove extra spaces from the line
    line = raw_line.strip()

    # create an empty dictionary to store the information
    fields = {}

    # split the record into parts using commas
    for piece in line.split(","):

        # separate each key and value
        key, value = piece.split("=")

        # clean the keys and values before storing them
        fields[key.strip().lower()] = value.strip().upper()

    # return the cleaned information as a dictionary
    return {
        "src": fields["src"],
        "attempts": float(fields["attempts"]),
        "result": fields["result"]
    }


def status_of(result):
    """Check if a login record should be flagged."""

    # check whether the login attempt failed
    if result == "FAILED":
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT

raw_records = []

# read the messy records from LAB//cyber_records.txt file
with open("LAB//cyber_records.txt") as f:
    for raw_line in f:
        raw_records.append(raw_line)

# =============================================================== PROCESS + OUTPUT

# start the counters at zero
total_records = 0
flagged_count = 0

# go through each record one at a time
for raw_record in raw_records:

    # clcean the record using the function
    record = parse_line(raw_record)

    # check the status of the record
    status = status_of(record["result"])

    # display the cleaned record and its status
    print(record, status)

    # count each record processed
    total_records += 1

    # count records that are flagged
    if status == "FLAGGED":
        flagged_count += 1


# display the summary in one line
print("Total records:", total_records, "| Flagged records:", flagged_count)



