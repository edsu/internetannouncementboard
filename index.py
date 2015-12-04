#!/usr/bin/env python

import os

last_size = None
images_html = ""

files = os.listdir('.')
files.sort()

for filename in files:
    if not filename.endswith('.png'):
        continue
    size = os.path.getsize(filename)
    if last_size is not None and last_size == size:
        os.remove(filename)
    else:
        images_html += '<div><img src="%s"></div><br>\n' % filename
    last_size = size

html = """<!doctype html>
<html>
<head>
  <title>bad internetannouncementboard archive</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
</head>

<body>
<div class="container">

<div class="row">

<div class="col-lg-offset-3 col-lg-6 text-center">

<h1>internetannouncementboard archive</h1>

%s 

</div>

</body>
</html>
""" % images_html

open("index.html", "w").write(html)
