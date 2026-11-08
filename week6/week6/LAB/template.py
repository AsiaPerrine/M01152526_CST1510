"""
RECORD CHECK  -  my version
===========================

Name  :  Perrine Asia
Lane  : Cyber
Date  :  03/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
"""Import libraries"""
import pandas as pd  #Import pandas
import matplotlib.pyplot as plt  #Import matplotlib for the chart

# ==================================================================== LOAD

"""Read the CSV file"""
df = pd.read_csv("LAB\\cyber_records.csv")  # read my cyber_records.csv file


# ================================================================= PROCESS

"""Calculate the percentage and set the status"""

df["percent"] = (df["value"] / df["limit"]) * 100 # calculate the percentage and add a percent column

#set the status for each record and add a "status" column 
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

# ================================================================== OUTPUT

print(df)  # display all the records

not_ok = df[df["status"] != "OK"] # keep records that are not OK
print(not_ok)  # display the filtered rows

counts = df.groupby("status").size()  # count records in each status
print(counts)  # display the status counts

df.to_csv("LAB\\cyber_report.csv", index=False)  # save all the records to a new CSV file

df["status"].value_counts().plot(kind="bar")  # make a bar chart of the status counts

plt.title("Cyber Record Status Counts")  # add a title to the chart
plt.savefig("cyber_status.png")  # save the chart as an image
plt.show() # display the chart
