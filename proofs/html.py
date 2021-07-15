
html_header = '<html><head></head><body style="background: #FDF6E3; color:#333333;"><div style="font-size:18px">'
html_footer = "</div></body></html>"

def html_chunks(lst):
    html_body = ''
    ix = 0
    for l in lst:
        if l['marked']:
            html_body += '<pre style="background-color: #F1D49B;display:inline;margin:0">[' + str(ix) + "]\t" + l['line'] + "\n</pre>"
        else:
            html_body += '<pre style="display:inline;margin:0">[' + str(ix) + "]\t" + l['line'] + "\n</pre>"

        ix += 1
    return html_body

def html_lines(lines):
    html_body = '<p><pre>'

    for line in lines:
        html_body += line + '\n'
    html_body += '</pre></p>'
    return html_body

def write_html(fname, sections):
    fout = open(fname, 'w')
    fout.write(html_header)
    for html in sections:
        fout.write(html)
    fout.write(html_footer)
    fout.close()

