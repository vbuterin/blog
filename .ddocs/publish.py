#!/usr/bin/python3
import os, sys, datetime

PRE_HEADER = """

<!DOCTYPE html>
<html>
<meta charset="UTF-8">

"""

HEADER_TEMPLATE = """

<link rel="stylesheet" type="text/css" href="$root/css/main.css">

<script>
MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']]
  },
  svg: {
    fontCache: 'global',
  }
};
</script>
<script type="text/javascript" id="MathJax-script" async
  src="$root/scripts/tex-svg.js">
</script>

<style>
</style>

<div id="doc" class="container-fluid markdown-body comment-enabled" data-hard-breaks="true">

<div id="color-mode-switch">
  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
    <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
  </svg>
  <input type="checkbox" id="switch" />
  <label for="switch">Dark Mode Toggle</label>
  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
    <path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
  </svg>
</div>
"""

TOGGLE_COLOR_SCHEME_JS = """
<script type="text/javascript">
  // Update root html class to set CSS colors
  const toggleDarkMode = () => {
    const root = document.querySelector('html');
    root.classList.toggle('dark');
  }

  // Update local storage value for colorScheme
  const toggleColorScheme = () => {
    const colorScheme = localStorage.getItem('colorScheme');
    if (colorScheme === 'light') localStorage.setItem('colorScheme', 'dark');
    else localStorage.setItem('colorScheme', 'light');
  }

  // Set toggle input handler
  const toggle = document.querySelector('#color-mode-switch input[type="checkbox"]');
  if (toggle) toggle.onclick = () => {
    toggleDarkMode();
    toggleColorScheme();
  }

  // Check for color scheme on init
  const checkColorScheme = () => {
    const colorScheme = localStorage.getItem('colorScheme');
    if (colorScheme === null || colorScheme === undefined) {
      // No saved preference — use OS preference
      if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        toggle.checked = true;
        toggleDarkMode();
        localStorage.setItem('colorScheme', 'dark');
      } else {
        localStorage.setItem('colorScheme', 'light');
      }
    } else if (colorScheme === 'dark') {
      toggle.checked = true;
      toggleDarkMode();
    }
  }
  checkColorScheme();
</script>
"""

RSS_LINK = """

<link rel="alternate" type="application/rss+xml" href="{}/feed.xml" title="{}">

"""

TITLE_TEMPLATE = """

<br>
<h1 style="margin-bottom:7px"> {0} </h1>
<small style="float:left; color: #888"> {1} </small>
<small style="float:right; color: #888"><a href="{2}/index.html">See all posts</a></small>
<br> <br> <br>
<title> {0} </title>

"""

TOC_TITLE_TEMPLATE = """

<title> {0} </title>
<br>
<center><h1 style="border-bottom:0px"> {0} </h1></center>

"""

FOOTER = """ </div> """

TOC_START = """

<br>
<ul class="post-list" style="padding-left:0">

"""

TOC_END = """ </ul> """

TOC_ITEM_TEMPLATE = """

<li>
    <span class="post-meta">{}</span>
    <h3 style="margin-top:12px">
      <a class="post-link" href="{}">{}</a>
    </h3>
</li>

"""

TWITTER_CARD_TEMPLATE = """
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="{}" />
<meta name="twitter:image" content="{}" />
"""


RSS_ITEM_TEMPLATE = """
<item>
<title>{title}</title>
<link>{link}</link>
<guid>{link}</guid>
<pubDate>{pub_date}</pubDate>
<description>{description}</description>
</item>
"""


RSS_MAIN_TEMPLATE = """
<?xml version="1.0" ?>
<rss version="2.0">
<channel>
  <title>{title}</title>
  <link>{link}</link>
  <description>{title}</description>
  <image>
      <url>{icon}</url>
      <title>{title}</title>
      <link>{link}</link>
  </image>
{items}
</channel>
</rss>
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
            value_start = line.find('(')+1
            value_end = line.rfind(')')
            if key in ('category', 'categories'):
                metadata['categories'] = set([
                    x.strip().lower() for x in line[value_start:value_end].split(',')
                ])
                assert '' not in metadata['categories']
            else:
                metadata[key] = line[value_start:value_end]
        else:
            break
    return metadata


def metadata_to_path(global_config, metadata):
    return os.path.join(
        global_config.get('posts_directory', 'posts'),
        metadata['date'],
        metadata['filename']
    )


def generate_feed(global_config, metadatas):
    def get_link(route):
        return global_config['domain'] + "/" + route

    def get_date(date_text):
        year, month, day = (int(x) for x in date_text.split('/'))
        date = datetime.date(year, month, day)
        return date.strftime('%a, %d %b %Y 00:00:00 +0000')

    def get_item(metadata):
        return RSS_ITEM_TEMPLATE.format(
            title=metadata['title'],
            link=get_link('/'.join([global_config['posts_directory'], metadata['date'], metadata['filename']])),
            pub_date=get_date(metadata['date']), description=''
        )

    return RSS_MAIN_TEMPLATE.strip().format(
        title=global_config['title'],
        link=get_link(''),
        icon=global_config['icon'],
        items="\n".join(map(get_item, metadatas))
    )




def make_twitter_card(title, global_config):
    return TWITTER_CARD_TEMPLATE.format(title, global_config['icon'])


def defancify(text):
    return text \
        .replace("’", "'") \
        .replace('“', '"') \
        .replace('”', '"') \
        .replace('…', '...') \


def make_categories_header(categories, root_path):
    o = ['<center><hr>']
    for category in categories:
        template = '<span class="toc-category" style="font-size:{}%"><a href="{}/categories/{}.html">{}</a></span>'
        o.append(template.format(min(100, 900 // len(category)), root_path, category, category.capitalize()))
    o.append('<hr></center>')
    return '\n'.join(o)


def get_printed_date(metadata):
    year, month, day = metadata['date'].split('/')
    month = 'JanFebMarAprMayJunJulAugSepOctNovDec'[int(month)*3-3:][:3]
    return year + ' ' + month + ' ' + day

def make_toc_item(global_config, metadata, root_path):
    link = metadata_to_path(global_config, metadata)
    return TOC_ITEM_TEMPLATE.format(get_printed_date(metadata), root_path + '/' + link, metadata['title'])


def make_toc(toc_items, global_config, all_categories, category=None):
    if category:
        title = category.capitalize()
        root_path = '..'
    else:
        title = global_config['title']
        root_path = '.'

    return (
        PRE_HEADER +
        RSS_LINK.format(root_path, title) +
        HEADER_TEMPLATE.replace('$root', root_path) +
        TOGGLE_COLOR_SCHEME_JS +
        make_twitter_card(title, global_config) +
        TOC_TITLE_TEMPLATE.format(title) +
        make_categories_header(all_categories, root_path) +
        TOC_START +
        ''.join(toc_items) +
        TOC_END
    )


if __name__ == '__main__':
    # Get blog config
    global_config = extract_metadata(open('config.md'))

    # Special case: '--sync' option
    if '--sync' in sys.argv:
        os.system('rsync -av site/. {}:{}'.format(global_config['server'], global_config['website_root']))
        sys.exit()

    # Normal case: process each provided file
    for file_location in sys.argv[1:]:
        filename = os.path.split(file_location)[1]
        print("Processing file: {}".format(filename))

        # Extract path
        file_data = open(file_location).read()
        metadata = extract_metadata(open(file_location), filename)
        path = metadata_to_path(global_config, metadata)

        # Generate the html file
        options = metadata.get('pandoc', '')

        os.system('pandoc -o /tmp/temp_output.html {} {}'.format(file_location, options))
        root_path = '../../../..'
        total_file_contents = (
            PRE_HEADER +
            RSS_LINK.format(root_path, metadata['title']) +
            HEADER_TEMPLATE.replace('$root', root_path) +
            TOGGLE_COLOR_SCHEME_JS +
            make_twitter_card(metadata['title'], global_config) +
            TITLE_TEMPLATE.format(metadata['title'], get_printed_date(metadata), root_path) +
            defancify(open('/tmp/temp_output.html').read()) +
            FOOTER
        )

        print("Path selected: {}".format(path))

        # Make sure target directory exists
        truncated_path = os.path.split(path)[0]
        os.system('mkdir -p {}'.format(os.path.join('site', truncated_path)))

        # Put it in the desired location
        out_location = os.path.join('site', path)
        open(out_location, 'w').write(total_file_contents)

    # Reset ToC
    metadatas = []
    categories = set()
    for filename in os.listdir('posts'):
        if filename[-4:-1] != '.sw':
            metadatas.append(extract_metadata(open(os.path.join('posts', filename)), filename))
            categories = categories.union(metadatas[-1]['categories'])
    categories = sorted(categories)

    print("Detected categories: {}".format(' '.join(categories)))

    sorted_metadatas = sorted(metadatas, key=lambda x: x['date'], reverse=True)
    feed = generate_feed(global_config, sorted_metadatas) if 'domain' in global_config else None

    os.system('mkdir -p {}'.format(os.path.join('site', 'categories')))

    print("Building tables of contents...")

    homepage_toc_items = [
        make_toc_item(global_config, metadata, '.') for metadata in sorted_metadatas if
        global_config.get('homepage_category', '') in metadata['categories'].union({''})
    ]

    for category in categories:
        category_toc_items = [
            make_toc_item(global_config, metadata, '..') for metadata in sorted_metadatas if
            category in metadata['categories']
        ]
        toc = make_toc(category_toc_items, global_config, categories, category)
        open(os.path.join('site', 'categories', category+'.html'), 'w').write(toc)

    if feed:
        open('site/feed.xml', 'w').write(feed)
    open('site/index.html', 'w').write(make_toc(homepage_toc_items, global_config, categories))

    # Copy CSS and scripts files
    this_file_directory = os.path.dirname(__file__)
    os.system('cp -r {} site/'.format(os.path.join(this_file_directory, 'css')))
    os.system('cp -r {} site/'.format(os.path.join(this_file_directory, 'scripts')))
    os.system('rsync -av images site/')
