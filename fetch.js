var page = require('webpage').create();
page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36';

var filename = Date.now() + ".png";

page.open('http://www.internetannouncementboard.com/', function(status) {});

function snap() {
  page.render(filename);
  phantom.exit();
}

setTimeout(snap, 5000);
