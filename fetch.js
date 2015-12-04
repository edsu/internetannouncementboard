var page = require('webpage').create();
page.settings.resourceTimeout = 3000;

var filename = Date.now() + ".png";

page.open('http://www.internetannouncementboard.com/', function(status) {
    page.render(filename);
    phantom.exit();
});
