var bunyan = require("bunyan");
var log = bunyan.createLogger({name: "hiplight"});

function Logger() {};

Logger.prototype.info = function(msg) {
  log.info(msg);
};

module.exports = exports = new Logger();
