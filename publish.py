#!/usr/bin/python3
import os, sys

HEADER = """

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<link rel="stylesheet" type="text/css" href="/css/common-vendor.b8ecfc406ac0b5f77a26.css">
<link rel="stylesheet" type="text/css" href="/css/font-vendor.b86e2bf451b246b1a88e.css">
<link rel="stylesheet" type="text/css" href="/css/fretboard.f32f2a8d5293869f0195.css">
<link rel="stylesheet" type="text/css" href="/css/pretty.0ae3265014f89d9850bf.css">
<link rel="stylesheet" type="text/css" href="/css/pretty-vendor.83ac49e057c3eac4fce3.css">
<link rel="stylesheet" type="text/css" href="/css/misc.css">

<script type="text/javascript" id="MathJax-script" async
  src="/scripts/mathjax.js">
</script>

<style>
@font-face {
    font-family: MJXc-TeX-math-Iw;
    src: url("https://assets.hackmd.io/build/MathJax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff")
}
@font-face {
    font-family: MJXZERO;
    src: url("https://assets.hackmd.io/build/MathJax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff")
}
@font-face {
    font-family: MJXTEX;
    src: url("https://assets.hackmd.io/build/MathJax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff")
}

.math { font-family: MJXc-TeX-math-Iw }
</style>

<div id="doc" class="container-fluid markdown-body comment-enabled" data-hard-breaks="true">

"""

FOOTER = """ </div> """

TOC_HEADER = """

<br>
<h1>{}</h1>
<br>
<br>
<ul class="post-list">

"""

TOC_FOOTER = """ </ul> """

TOC_ITEM_TEMPLATE = """

<li>
    <span class="post-meta">{}</span>
    <h3>
      <a class="post-link" href="{}">{}</a>
    </h3>
</li>

"""

TWITTER_CARD_TEMPLATE = """
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="{}" />
<meta name="twitter:image" content="{}" />
"""

def extract_metadata(fil, filename=None):
    metadata = {}
    if filename:
        assert filename[-3:] == '.md'
        metadata["filename"] = filename[:-3]+'.html'
    while 1:
        line = fil.readline()
        if line and line[0] == '[' and ']' in line:
            key = line[1:line.find(']')]
            value_start = line.index('(')+1
            value_end = line.index(')')
            metadata[key] = line[value_start:value_end]
        else:
            break
    return metadata


def metadata_to_path(metadata):
    return os.path.join(metadata['category'].lower(), metadata['date'], metadata['filename'])


def make_twitter_card(metadata, global_config):
    return TWITTER_CARD_TEMPLATE.format(metadata['title'], global_config['icon'])


def defancify(text):
    return text \
        .replace("’", "'") \
        .replace('“', '"') \
        .replace('”', '"') \
        .replace('…', '...') \


def make_toc_item(metadata):
    year, month, day = metadata['date'].split('/')
    month = 'JanFebMarAprMayJunJulAugSepOctNovDec'[int(month)*3-3:][:3]
    link = os.path.join('/', metadata_to_path(metadata))
    return TOC_ITEM_TEMPLATE.format(year+' '+month+' '+day, link, metadata['title'])

if __name__ == '__main__':
    # Get blog config
    global_config = extract_metadata(open('config.md'))

    # Special case: '--sync' option
    if sys.argv[1:] == ['--sync']:
        os.system('rsync -av site/. {}:{}'.format(global_config['server'], global_config['website_root']))
        os.system('rsync -av images {}:{}'.format(global_config['server'], global_config['website_root']))
        sys.exit()

    # Normal case: process each provided file
    for file_location in sys.argv[1:]:
        filename = os.path.split(file_location)[1]
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
        options = metadata.get('pandoc', '')
        
        os.system('pandoc -o /tmp/temp_output.html {} {}'.format(file_location, options))
        total_file_contents = (
            HEADER +
            make_twitter_card(metadata, global_config) +
            defancify(open('/tmp/temp_output.html').read()) +
            FOOTER
        )
    
        # Put it in the desired location
        open(out_location, 'w').write(total_file_contents)

    # Reset ToC
    metadatas = []
    for filename in os.listdir('posts'):
        if filename[-4:-1] != '.sw':
            metadatas.append(extract_metadata(open(os.path.join('posts', filename)), filename))

    sorted_metadatas = sorted(metadatas, key=lambda x: x['date'], reverse=True)
    toc_items = [make_toc_item(metadata) for metadata in sorted_metadatas]

    toc = (
        HEADER +
        make_twitter_card(global_config, global_config) +
        TOC_HEADER.format(global_config['title']) +
        ''.join(toc_items) +
        TOC_FOOTER
    )

    open('site/index.html', 'w').write(toc)
