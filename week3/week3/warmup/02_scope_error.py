# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status # this sends back the output


status = check(87, 100) #it stores the output
print(status)# this displays the output
