# TASK: https://adventofcode.com/2020/day/2/

import re
with open('input', 'r') as input:
    lines: str =  input.read().splitlines()

constraints = [constraint.split(':')[0] for constraint in lines]
# regex to extract the respective parts: min appearances of letter, max appearances of letter, letter and the password
matches = [re.match(r'(?P<min>\d+)-(?P<max>\d+)\s(?P<letter>\w):\s(?P<pw>\w*)', line) for line in lines]

num_valid_passwords = 0 
for regex in matches:
    min, max, letter, pw = regex.group('min', 'max', 'letter', 'pw')
    # password is valid if it does not violate the policy (appearances of letter in [min,max])
    if pw.count(letter) in range(int(min), int(max)+1):
        num_valid_passwords += 1
#solution
print(num_valid_passwords)