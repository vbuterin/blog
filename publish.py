#!/usr/bin/python3
import os, sys

HEADER = """

<link rel="stylesheet" type="text/css" href="/css/common-vendor.b8ecfc406ac0b5f77a26.css">
<link rel="stylesheet" type="text/css" href="/css/font-vendor.b86e2bf451b246b1a88e.css">
<link rel="stylesheet" type="text/css" href="/css/fretboard.f32f2a8d5293869f0195.css">
<link rel="stylesheet" type="text/css" href="/css/pretty.0ae3265014f89d9850bf.css">
<link rel="stylesheet" type="text/css" href="/css/pretty-vendor.83ac49e057c3eac4fce3.css">
<link rel="stylesheet" type="text/css" href="/css/list.css">

<div id="doc" class="container-fluid markdown-body comment-enabled" data-hard-breaks="true">

"""

FOOTER = """ </div> """

TOC_HEADER = """ <ul class="post-list"> """

TOC_FOOTER = """ </ul> """

TOC_ITEM_TEMPLATE = """

<li>
    <span class="post-meta">{}</span>
    <h3>
      <a class="post-link" href="{}">{}</a>
    </h3>
</li>

"""

def extract_metadata(fil, filename):
    assert filename[-3:] == '.md'
    metadata = {'filename': filename[:-3]+'.html'}
    while 1:
        line = fil.readline()
        if line[0] == '[' and ']' in line:
            key = line[1:line.find(']')]
            value_start = line.index('(')+1
            value_end = line.index(')')
            metadata[key] = line[value_start:value_end]
        else:
            break
    return metadata


def metadata_to_path(metadata):
    return os.path.join(metadata['category'].lower(), metadata['date'], metadata['filename'])


def make_toc_item(metadata):
    year, month, day = metadata['date'].split('/')
    month = 'JanFebMarAprMayJunJulAugSepOctNovDec'[int(month)*3-3:][:3]
    link = os.path.join('/', metadata_to_path(metadata))
    return TOC_ITEM_TEMPLATE.format(year+' '+month+' '+day, link, metadata['title'])

if __name__ == '__main__':
    # Arguments: location of the files
    for file_location in sys.argv[1:]:
        filename = os.path.split(file_location)[1]
        assert filename[-3:] == '.md'
        print("Processing file: {}".format(filename))
        
        # Extract path
        file_data = open(file_location).read()
        metadata = extract_metadata(open(file_location), filename)
        path = metadata_to_path(metadata)
        print("Path selected: {}".format(path))
        
        # Make sure target directory exists
        truncated_path = os.path.split(path)[0]
        os.system('mkdir -p {}'.format(os.path.join('site', truncated_path)))
        
        # Generate the html file
        out_location = os.path.join('site', path)
        
        os.system('pandoc -o /tmp/temp_output.html {}'.format(file_location))
        total_file_contents = HEADER + open('/tmp/temp_output.html').read() + FOOTER
    
        # Put it in the desired location
        open(out_location, 'w').write(total_file_contents)

    # Reset ToC
    metadatas = []
    for filename in os.listdir('posts'):
        if filename[-4:-1] != '.sw':
            metadatas.append(extract_metadata(open(os.path.join('posts', filename)), filename))

    sorted_metadatas = sorted(metadatas, key=lambda x: x['date'], reverse=True)
    toc_items = [make_toc_item(metadata) for metadata in sorted_metadatas]

    toc = HEADER + TOC_HEADER + ''.join(toc_items) + TOC_FOOTER

    open('site/index.html', 'w').write(toc)
