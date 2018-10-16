#!/usr/bin/env python3

import os.path
import re
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

ns = {'content': 'http://purl.org/rss/1.0/modules/content/'}

tree = ET.parse('data.xml')
root = tree.getroot()
channel = root.find('channel')

template = '''+++
title = "{name}"
+++

{summary}

<!--more-->

{content}
'''

for item in channel.findall('item'):
    name = item.find('title').text
    link = item.find('link').text
    path = urlparse(link).path
    if path.endswith('/'):
        path = path[:-1]
    filename = os.path.basename(path) + '.md'
    content = item.find('content:encoded', ns).text or ''
    no_html_content = re.sub('<[^<]+?>', '', content)

    categories = item.findall('category')
    summary = ', '.join(sorted([c.text for c in categories if c.text not in ['Musicians', 'Groups']]))

    with open(filename, 'w') as f:
        f.write(template.format(name=name, content=no_html_content, summary=summary))

