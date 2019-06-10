$(function () {
    var table = $("#table");
    var board = $("#board");
    var panel = $("#board table")
    var tgPanel;

    // board create
    for (var j = 0; j < 8; j++) {
      var tr = $("<tr></tr>");
      for (var i = 0; i < 8; i++) {
        tr.append($("<td onclick='panelClick("+j+","+i+");'></td>"));
      }
      $("div#board table").append(tr);
    }

    $("td").hover(function () {
      var y = $(this).parent().index();
      var x = $(this).index();
      var me = getPanel(y,x);
      //getPanel(y+1, x+1).css("background-color", 'pink');
    });
});

function panelClick(y,x){

}

function getPanel(y, x){
  var target = $(
    "#board table tr:nth-child("+(y+1)+") td:nth-child("+(x+1)+")"
  );
  return target;
}
