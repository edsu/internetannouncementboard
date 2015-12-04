#!/usr/bin/env python

import os

last_size = None

images_html = ""

for filename in os.listdir('.'):
    if not filename.endswith('.png'):
        continue
    size = os.path.getsize(filename)
    if last_size is not None and last_size == size:
        os.remove(filename)
    else:
        images_html += '<div><img src="%s"></div>\n' % filename
    last_size = size

html = """<!doctype html>
<html>
<head>
  <title>internetannouncementboard archive</title>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"></script>
</head>

<body>
<div class="container">

<h1>internetannouncementboard archive</h1>

%s 

</div>
</body>
</html>
""" % images_html

open("index.html", "w").write(html)
