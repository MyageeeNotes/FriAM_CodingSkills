$(function () {
    var table = $("#table");
    var board = $("#board");
    var panel = $("#board table")
    var tgPanel;

    var bd = new setup();

    // board create
    for (var j = 0; j < 8; j++) {
      var tr = $("<tr></tr>");
      for (var i = 0; i < 8; i++) {
        tr.append($("<td onclick='panelClick("+j+","+i+");'></td>"));
      }
      $("div#board table").append(tr);
      var pnl = panel(j, i);
      bd.board.append(pnl);
    }

    $("td").hover(function () {
      var y = $(this).parent().index();
      var x = $(this).index();
      var me = getPanel(y,x);
      //getPanel(y+1, x+1).css("background-color", 'pink');
    });
});

class setup {
  constructor() {
    this.board = [];
  }
}

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

function panelClick(y,x){

}

function getPanel(y, x){
  var target = $(
    "#board table tr:nth-child("+(y+1)+") td:nth-child("+(x+1)+")"
  );
  return target;
}

function loop(){
  while (true) {

  }
}
