# TASK: https://adventofcode.com/2020/day/4/

import re
with open('input', 'r') as input:
    # different whitespaces inside an ID document; double newline always separates ID documents
    lines =  input.read().split('\n\n')

# replace \n whitespace by space in document
lines = [line.replace('\n', ' ') for line in lines]
# find all key value pairs for each entry
matches = (re.findall(r'(?P<key>\w+):\S', line) for line in lines)
# case distinction:
# case 1: 7 keys, but cid is contained: invalid
# case 2: less than 7 keys: invalid
# case 2: 7 keys, but only key 'cid' is missing: valid
valid = list(map(lambda regex: 0 if (len(regex) == 7 and 'cid' in regex or len(regex) < 7 ) else 1, matches))
# solution
print(sum(valid))
