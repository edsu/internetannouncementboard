var page = require('webpage').create();

var filename = Date.now() + ".png";

//page.open('http://www.internetannouncementboard.com/', function(status) {
page.open('http://inkdroid.org/', function(status) {
    console.log(status);
    page.render(filename);
    phantom.exit();
});
