# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]})  # the error was that the values were stored as text instead of numbers

df["value"] = df["value"].astype(int)  # fixed it by converting the value column to integers using astype(int)

df["percent"] = (df["value"] / df["limit"]) * 100

