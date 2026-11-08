# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

piece = "note=server=east"
key, value = piece.split("=",1)   # the error is the code tries to put 3 parts into 2 variables, too many values to unpack
# fix by adding 1 inside .split("=", 1) so that Python splits the text only once.

print(key, value)
