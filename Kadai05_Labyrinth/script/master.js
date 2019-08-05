var field = {
  'range': { 'x': 7, 'y': 7 },
  'init': undefined,
  'start': { 'x': 1, 'y': 1 },
  'stack': []
}
var frame = {
  'now': 0,
  'finish': 1
}

function initWorld(){
    // Initialize Field life list
	field.init = Array(field.range.x * field.range.y);
    field.init.fill(false);
	fieldLen = field.init.length;
}
function setDom(){
    for (var y = 0; y < field.range.y; y++) {
        var tr = $('<tr></tr>');
        for (var x = 0; x < field.range.x; x++) {
            var td =  $('<td></td>');
            td.attr('id', 'x' + x + 'y' + y);
            if(!field.init[y * field.range.x + x]){ td.addClass('wall') }
            tr.append(td);
        }
        $('#field').append(tr);
    }
}
function createWorld() {

}

function sensor(tg) {
    var dir = 0;
    if (0 < tg.y) {
        if (getDom(tg.x, tg.y - 1).hasClass('wall')) { dir += 1; }
    }
    if (tg.x < field.range.x - 1) {
        if (getDom(tg.x + 1, tg.y).hasClass('wall')) { dir += 2; }
    }
    if (tg.y < field.range.y - 1) {
        if (getDom(tg.x, tg.y + 1).hasClass('wall')) { dir += 4; }
    }
    if (0 < tg.x) {
        if (getDom(tg.x - 1, tg.y).hasClass('wall')) { dir += 8; }
    }
    return dir;
}
function getDom(x, y){
    return $("#field tr:nth-child(" + y + ") td:nth-child(" + x + ")");
}
$(function () {
    initWorld();
    createWorld();
    setDom();

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
