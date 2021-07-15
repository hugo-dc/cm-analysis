#!/bin/env python
from graphviz import Digraph

def get_color(number, indices):
    print(number)
    print(indices)
    print(number in indices)
    if number in indices:
        print(number, "red")
        return "red"
    print(number, "blue")
    return "blue"


def generate_tree(tree, description):
    dot = Digraph()
    dot.graph_attr['rankdir'] = 'TB'
    dot.format = 'svg'

    ix = 0
    iy = 0

    allowed_nodes = ["1","2","3","4","5","6"]
    code_subtree = []

    while iy + 2 < len(tree):
        node_number = tree[ix]
        left_number = tree[ix+1]
        right_number = tree[ix+2]
        node_name = description[ix]
        left_name = description[iy+1]
        right_name = description[iy+2]

        if node_name in allowed_nodes or node_name in code_subtree:
            #fcolor = get_color(node_number, indices)
            print(ix)
            print(description[ix])
            
            dot.node(str(node_number), node_name) #, fillcolor=fcolor, style="filled")

            #fcolor = get_color(left_number, indices)
            dot.node(str(left_number), left_name) #, fillcolor=fcolor, style="filled")

            #fcolor = get_color(right_number, indices)
            dot.node(str(right_number), right_name) #, fillcolor=fcolor, style="filled")

            dot.edge(node_name, left_name)
            dot.edge(node_name, right_name)

            if node_number == 6 or node_name in code_subtree:
                code_subtree.append(left_name)
                code_subtree.append(right_name)

        iy += 2
        ix += 1

    return dot


code_hash = '0a84592dd9d53a4f475125d8a8bc9e6bd21da004081852646b6e74191f5a4aa0'

def read_file_data(fname):
    infile = open(fname, 'r')
    data = infile.read()
    infile.close()
    return data

baseline = read_file_data(code_hash + '_baseline.txt')
baseline = baseline.split('\n')

leavesStart = baseline.index("Leaves:")

indices = eval(baseline[1])
hashes = baseline[4:leavesStart-2]
leaves = baseline[leavesStart+1:-1]

print("Indices (" + str(len(indices)) + "):", indices)
print("Hashes (" + str(len(hashes)) + "):", hashes)
print("Leaves (" + str(len(leaves)) + "):", leaves)

depth_10 = range(1, 14337)
description = list(range(1, 14337))
description = [str(x) for x in description]

description[6] = "Chunks: " + leaves[0]
description[7] = "Version: " + leaves[1]
description[8] = "CodeHash: " + leaves[2]
description[9] = "CodeLength: " + leaves[3]
description[10] = "Empty"

tree = generate_tree(depth_10, description)
tree.render('tree.dot', view=False)

