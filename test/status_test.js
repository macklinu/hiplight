var should = require("should");
var Status = require("../src/status");

describe("Status", function() {
  describe("#parse", function() {
    it("should return Status.UNKNOWN if user is null", function(done) {
      var status = Status.parse(null);
      status.should.equal(Status.UNKNOWN);
      done();
    });
    it("should return Status.OFFLINE if user.presence is null", function(done) {
      var status = Status.parse({presence: null});
      status.should.equal(Status.OFFLINE);
      done();
    });
    it("should return Status.AVAILABLE if user.presence.show is 'chat'", function(done) {
      var status = Status.parse({presence: {show: "chat"} });
      status.should.equal(Status.AVAILABLE);
      done();
    });
    it("should return Status.AWAY if user.presence.show is 'xa'", function(done) {
      var status = Status.parse({presence: {show: "xa"} });
      status.should.equal(Status.AWAY);
      done();
    });
    it("should return Status.DO_NOT_DISTURB if user.presence.show is 'dnd'", function(done) {
      var status = Status.parse({presence: {show: "dnd"} });
      status.should.equal(Status.DO_NOT_DISTURB);
      done();
    });
    it("should throw if user.presence.show is invalid", function(done) {
      (function() {
        Status.parse({presence: {show: null} });
      }).should.throw();
      done();
    });
  });
});
