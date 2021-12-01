# TASK: https://adventofcode.com/2020/day/6/

with open('input', 'r') as input:
    lines =  input.read().split('\n\n')

# set(string) replaces the string with a new one containing only unique values - we remove \n so the count is not too high by 1
counts = map(lambda line: len(set(line.replace('\n',''))), lines)
# the solution is the sum of unique declarations in each group
print(sum(counts))