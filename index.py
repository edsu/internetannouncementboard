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
    t = datetime.datetime.fromtimestamp(int(filename.strip(".png"))/1000 - 18000)
    t = t.strftime("%H:%M")
    size = os.path.getsize(filename)
    if last_size is not None and last_size == size:
        os.remove(filename)
    else:
        images_html += '<div><img class="img-thumbnail" src="%s"><br><span style="font-size: 14pt">%s ET</span></div><br>\n' % (filename, t)
    last_size = size

html = """<!doctype html>
<html>
<head>
  <title>bad internetannouncementboard archive</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
</head>

<body>
<div class="container-fluid">

<div class="row">

<div class="col-lg-offset-3 col-lg-6 text-center">

<h2>pathetic internetannouncementboard archive</h2>
<hr>

%s 

<p>
<em>This was a waste of time while I should have been writing a final paper for
my class about web archiving.</em>
</p>

</div>


</body>
</html>
""" % images_html

open("index.html", "w").write(html)
