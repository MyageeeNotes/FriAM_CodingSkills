class Panel {
  constructor(pos_y, pos_x) {
    this.pos = {
      x: pos_x,
      y: pos_y
    };
    var path = '#div#board table:nth-child(';
    path += (pos_y + ') td:nth-child(');
    path += (pos_x + ')');
    this.body = $(path);
  }
}
