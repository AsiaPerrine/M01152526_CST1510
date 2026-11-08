# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

value_text = "87"

cleaned = value_text.strip() # the error is .strip() cannot be used on a float
# to fix the error clean the text first 

value = float(cleaned)  # the convert it to a number

print(cleaned)
