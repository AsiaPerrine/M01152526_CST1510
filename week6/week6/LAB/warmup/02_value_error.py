# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],
    "value": [87, 120, 55],
})  # the error is that "label" has 3 values whereas "value" has only 2
# fix by adding 55 to the column "value" so both columns have the same number of values
