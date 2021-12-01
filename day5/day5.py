# TASK: https://adventofcode.com/2020/day/5/

with open('input', 'r') as input:
    lines =  input.read().splitlines()
# get list of rows (first 7 chars), columns (last 3 chars)

# also replace L and R by F and B respectively for easier processing
seats = ((line[:7], line[7:].replace('L', 'F').replace('R', 'B')) for line in lines)

# helper function to avoid code duplication
def interpret_encoded_seat(string):
    max = 2**len(string)
    min = 0
    for char in string[:-1]:
        # B: keep upper half
        if char == 'B':
            min += (max-min) / 2
        # F: keep lower half
        else:
            max -= (max-min) / 2
    res = max-1 if string[-1] == 'B' else min
    return res

# map the generator of tuples with (row_str, seat_str) to the seat ID which is defined as 8*row_int + seat
ids = map(lambda tpl: 8 * interpret_encoded_seat(tpl[0]) + interpret_encoded_seat(tpl[1]), seats)
# the solution is the maximum of the ID's
print(max(ids))

