# TASK: https://adventofcode.com/2020/day/3/

with open('input', 'r') as input:
    lines =  input.read().splitlines()

# read the pattern width for the wraparound
width = len(lines[0])
# don't identify depth via index of the line in case lines aren't unique
depth = 0
# number of hit trees
trees = 0
for line in lines:
    # idea: we will always be at width of 3*depth (3 right, 1 down), mod width for the wraparound
    square = line[(3 * depth)%width]
    # we hit a tree
    if square == '#':
        trees += 1
    depth += 1 
print(f'Amount of trees hit: {trees}. Wow, thats a hit ratio of {round(trees/len(lines) * 100)}%!')