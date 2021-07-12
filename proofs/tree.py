#!/bin/env python

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


