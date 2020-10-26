from publish import extract_metadata
import os, sys

METADATA_TEMPLATE = """

[category]: <> (General)
[date]: <> ({})
[title]: <> ({})
[pandoc]: <> ({})

# {}
"""

def translate(contents):
    uses_mathjax = '$' in contents
    lines = contents.split('\n')
    assert lines[0] == '---'
    pos = 1
    while 1:
        newline = lines[pos]
        if newline == '---':
            break
        elif newline[:6] == 'title:':
            title = newline[newline.find('"')+1: newline.rfind('"')]
        elif newline[:5] == 'date:':
            simpledate = newline[5:].lstrip()[:10]
            year, month, day = simpledate.split('-')
        pos += 1
    header = METADATA_TEMPLATE.format(year+'/'+month+'/'+day, title, '--mathjax' if uses_mathjax else '', title)
    body = ('\n'.join(lines[pos+1:])) \
        .replace('http://vitalik.ca/files/posts_files/', '/images/') \
        .replace('https://vitalik.ca/files/posts_files/', '/images/')
    return header.strip() + "\n" + body

if __name__ == '__main__':
    for filepath in sys.argv[1:]:
        body = translate(open(filepath).read())
        new_location = os.path.join('posts', os.path.split(filepath)[1][11:])
        if new_location[-9:] == '.markdown':
            new_location = new_location[:-9] + '.md'
        open(new_location, 'w').write(body)
