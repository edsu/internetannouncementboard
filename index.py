#!/usr/bin/env python

import os
import datetime

last_size = None
images_html = ""

files = os.listdir('.')
files.sort()

for filename in files:
    if not filename.endswith('.png'):
        continue
    t = datetime.datetime.fromtimestamp(int(filename.strip(".png")))
    t = t.strftime("%H:%M:%s")
    size = os.path.getsize(filename)
    if last_size is not None and last_size == size:
        os.remove(filename)
    else:
        images_html += '<div><img src="%s"><br><span>%s</span></div>\n' % (filename, t)
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

<h1>flaky<br>internetannouncementboard<br>archive</h1>
<hr>

%s 

</div>

</body>
</html>
""" % images_html

open("index.html", "w").write(html)
