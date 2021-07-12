#!/bin/env python

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

html_header = '<html><head></head><body style="background: #FDF6E3; color:#333333;"><div style="font-size:18px">'
html_footer = "</div></body></html>"

html_chunks = ""
ix = 0
for chunk in chunks:
    if ix in touched_chunks:
        html_chunks += '<pre style="background-color: #F1D49B;display:inline;margin:0">[' + str(ix) + "]\t" + chunk + "\n</pre>"
    else:
        html_chunks += '<pre style="display:inline;margin:0">[' + str(ix) + "]\t" + chunk + "\n</pre>"
    ix += 1

html = html_header + html_chunks + html_footer

fout = open("./result.html", 'w')
fout.write(html)
fout.close()
