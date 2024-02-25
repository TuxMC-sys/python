import sys
from collections import deque
if sys.argv[1] == "help":
    print("Put strings to be reversed in quotes")
    quit()
string_array = list(sys.argv[1])
reversed_string_array = deque([])
for x in string_array:
    reversed_string_array.appendleft(x)
reversed_string = ""
reversed_string = reversed_string.join(reversed_string_array)
print(reversed_string)