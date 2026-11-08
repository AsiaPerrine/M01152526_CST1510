# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

raw_line = "srv-01,used=unknown,total=100"
hostname_part, rest = raw_line.split(",", 1)

for piece in rest.split(","):
    key, value = piece.split("=")
   # print(key, float(value)) #the error is float() cannot change "unknown" into a number
# fix by using try and except to handle the error
    try:
        print(key, float(value))
    except ValueError:
        print("Could not convert:", value)