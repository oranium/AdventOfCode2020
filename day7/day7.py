# TASK: https://adventofcode.com/2020/day/7/

import re
with open('input', 'r') as input:
    lines =  input.read().splitlines()

# helper class for DFS
class Node:
    def __init__(self, name: str, containing: set, contains_gold: bool) -> None:
        self.name = name
        self.containing = containing
        self.contains_gold = contains_gold


# DFS helper function
def dfs(node: Node, visited=set()):
    if node not in visited:
        visited.add(node)
        for bag in node.containing:
            node.contains_gold = dfs(nodes[bag], visited)[0] or node.contains_gold
    return node.contains_gold, visited

# save nodes in dictionary, so we can identify then by their name
nodes = {}
for line in lines:
    # name of the type of bag
    bag_type = line.split('bags')[0].strip()
    # find all the bags that can be inside of the current bag
    for can_contain in line.split('bags contain')[1:]:
        # short for 'no other bags'
        if 'no o' in can_contain:
            nodes[bag_type] = (Node(bag_type, set(), False))
        else:
            amt_type_string = " ".join(can_contain.replace(',', '').replace('.','').replace('bags', '').replace('bag', '').split())
            # regex that finds all the possible bags inside of the current bag type
            regex_string = r'(\d) (\w+\s\w+)'
            # we can remove the numbers because we only care about the binary information: holds a type of bag or no
            # use set to avoid infinite bag cycles / redundant entries
            contains_first_level = set(map(lambda found: found[1],re.findall(regex_string, can_contain)))
            nodes[bag_type] = Node(bag_type, contains_first_level, 'shiny gold' in contains_first_level)

# now we can apply dfs to find the amount of bag types that can contain shiny gold? bags 
visited_graphs = set()

# there is no guarantee that the graph is connected - we need to check for every node
for node in nodes.values():
    # don't run DFS for a visited node
    if node not in visited_graphs:
        # save newly visited graphs
        _ ,visited_graphs = dfs(node,visited_graphs)

# solution
print(sum(map(lambda node: node.contains_gold, nodes.values())))