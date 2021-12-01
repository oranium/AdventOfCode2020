# TASK: https://adventofcode.com/2020/day/1/

with open('input', 'r') as input:
    expenses = [int(expense) for expense in input.read().splitlines()]

for expense in expenses:
    idx = expenses.index(expense)
    # only iterate over the following list indices; the previous ones have been tested with the current expense
    # this could be quicker if the list was sorted
    complement = 2020-expense
    if complement in expenses[idx+1:]:
        idx_complement = expenses.index(2020-expense)
        # solution
        print(f'{expense} * {complement} = {expense*complement}')