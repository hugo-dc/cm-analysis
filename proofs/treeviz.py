#!/bin/env python
from graphviz import Digraph

def generate_tree(top_tree):
    dot = Digraph()
    dot.graph_attr['rankdir'] = 'TB'
    dot.format = 'svg'

    tree = top_tree

    ix = 0
    iy = 0

    allowed_nodes = ["1","2","3","4","5","6"]
    code_subtree = []

    while iy + 2 < len(tree):
        node_name = str(tree[ix])
        left_name = str(tree[iy+1])
        right_name = str(tree[iy+2])

        print(node_name)

        if node_name in allowed_nodes or node_name in code_subtree:
           dot.node(node_name, node_name)
            dot.node(left_name, left_name)
            dot.node(right_name, right_name)

            dot.edge(node_name, left_name)
            dot.edge(node_name, right_name)

           if node_name == "6" or node_name in code_subtree:
                code_subtree.append(left_name)
                code_subtree.append(right_name)

        iy += 2
        ix += 1

    return dot

depth_10 = range(1,24577)
tree = generate_tree(depth_10)
tree.render('tree.dot', view=False)

