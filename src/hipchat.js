// jscs:disable requireCamelCaseOrUpperCaseIdentifiers

require("dotenv").load();

var bunyan = require("bunyan");
var log = require("./logger");
var Rx = require("rx");
var Hipchatter = require("hipchatter");
var hipchatter = new Hipchatter(process.env.HIPCHAT_API_TOKEN);
var Status = require("./status");

const EMAIL_ADDRESS = process.env.HIPCHAT_EMAIL_ADDRESS;

function HipChat() {};

HipChat.prototype.getUser = function() {
  return Rx.Observable.create(function(observer) {
    Rx.Scheduler.default.schedulePeriodic(
      5000,
      function() {
        hipchatter.view_user(EMAIL_ADDRESS, function(err, user) {
          if (!err) {
            log.info(user);
            var status = Status.parse(user);
            observer.onNext(status);
          } else {
            observer.onError(err);
          }
        })
      }
    )
  });
}

module.exports = exports = new HipChat();
