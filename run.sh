#!/bin/bash

cd /home/ubuntu/internetannouncementboard;

phantomjs --ssl-protocol=any fetch.js 2>/dev/null;

./index.py;

git add *.png;

git commit -m 'latest' -a;

git push origin gh-pages;
