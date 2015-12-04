var page = require('webpage').create();

var filename = Date.now() + ".png";

page.open('http://www.internetannouncementboard.com/', function(status) {
    page.render(filename);
    phantom.exit();
});
