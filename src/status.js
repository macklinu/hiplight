module.exports = {
  parse: function(user) {
    if (!user) {
      return this.UNKNOWN;
    }

    if (user.presence) {
      if (user.presence.show == "chat") {
        return this.AVAILABLE;
      } else if (user.presence.show == "xa") {
        return this.AWAY;
      } else if (user.presence.show == "dnd") {
        return this.DO_NOT_DISTURB;
      }
      throw new Error();
    }

    return this.OFFLINE;
  },
  AVAILABLE: {
    "name": "available",
    "color": {
      "red": 0,
      "green": 255,
      "blue": 0
    }
  },
  AWAY: {
    "name": "away",
    "color": {
      "red": 255,
      "green": 255,
      "blue": 0
    }
  },
  DO_NOT_DISTURB: {
    "name": "do not disturb",
    "color": {
      "red": 255,
      "green": 0,
      "blue": 0
    }
  },
  OFFLINE: {
    "name": "offline",
    "color": {
      "red": 0,
      "green": 0,
      "blue": 0
    }
  },
  UNKNOWN: {
    "name": "unknown",
    "color": {
      "red": 0,
      "green": 0,
      "blue": 0
    }
  }
};
