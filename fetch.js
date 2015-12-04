var page = require('webpage').create();

var filename = Date.now() + ".jpg";

page.open('http://www.internetannouncementboard.com/', function(status) {
    console.log(status);
    page.render(filename);
    phantom.exit();
});
