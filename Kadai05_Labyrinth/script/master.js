var field = {
  'range': [30, 30],
  'lifes': [],
  'init': undefined
}
var frame = {
  'now': 0,
  'finish': 1
}

var stack = [];

function createWorld() {
  var cnt = 0;
  for (var y = 0; y < field.range[1]; y++) {
    var tr = $('<tr></tr>');
    for (var x = 0; x < field.range[0]; x++) {
      var td =  $('<td></td>');
      td.attr('id', 'x' + x + 'y' + y);
      tr.append(td);

      // EDGE
      if (x == 0 || y == 0 || x == field.range[0] - 1 || y == field.range[1] - 1) {
          td.addClass('wall');
      }

      field['lifes'].push(td);
      cnt += 1;
    }
    $('#field').append(tr);
  }
}

$(function () {
  createWorld();

  var start = setInterval(function() {
    frame.now++;
    // START
    console.log('TURN:', frame.now);

  	//FINISH
	if (frame.now == frame.finish) {
	    clearInterval(start);
        console.log("end");
    }
  }, 500);
});
