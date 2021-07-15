#!/bin/env python
import html

code_hash = '0a84592dd9d53a4f475125d8a8bc9e6bd21da004081852646b6e74191f5a4aa0'

def read_file_data(fname):
    infile = open(fname, 'r')
    data = infile.read()
    infile.close()
    return data


code = read_file_data(code_hash + '_code.txt')
initial_code = code
touched_chunks = read_file_data(code_hash + '_chunks.txt')
touched_chunks = eval(touched_chunks)
touched_chunks.sort()

total_bytes = len(code) // 2

chunks = []
while len(code) > 0:
    if len(code) >= 64:
        chunks.append(code[:64])
        code = code[64:]
    else:
        chunks.push(code)
        code = ""

for c in chunks:
    print(c)

print("Total bytes:", total_bytes)
print("Total chunks:", len(chunks))
print("Touched chunks:", len(touched_chunks))

new_chunks = []
ix = 0
for chunk in chunks:
    nc = {}
    nc['marked'] = ix in touched_chunks
    nc['line'] = chunk
    new_chunks.append(nc)
    ix += 1

html_chunks = html.html_chunks(new_chunks)

stats = ["Total bytes: " + str(total_bytes),
        "Total chunks: " + str(len(chunks)), 
        "Touched chunks: " + str(len(touched_chunks))]
html_stats = html.html_lines(stats)

html.write_html("./result.html", [html_chunks, html_stats])

