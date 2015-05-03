var api = require("./hipchat");
var log = require("./logger");
var pins = require("./pins");

process.on("SIGINT", function() {
  if (userStatusSubscription) {
    userStatusSubscription.dispose();
  }
  process.exit();
});

var userStatusSubscription = api.getUser()
  .subscribe(
    function(status) {
      log.info(status);
      log.info(status.color);
      pins.apply(status.color);
    },
    function(err) {
      log.info(err);
    },
    function() {}
  );
