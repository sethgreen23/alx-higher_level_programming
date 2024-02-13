#!/usr/bin/node

module.exports = class Square extends Square {
  charPrint (c) {
    if (c === undefined || !this.isCharacter(c)) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }

  isCharacter (char) {
    return (/[a-zA-Z]/).test(char);
  }
};
