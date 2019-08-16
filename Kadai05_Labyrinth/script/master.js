var field = {
  'range': { 'x': 11, 'y': 11 },
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
            if(!field.init[y * field.range.x + x]){ td.addClass('wall'); }
            tr.append(td);
        }
        $('#field').append(tr);
    }
}
function createWorld() {
    var pos = {x: field.start.x, y:field.start.y }
    var canDig = true;
    var count = 0;
    while(canDig == true && count < 1000){
        // Dig
        field.init[pos.y * field.range.x + pos.x] = true;
        field.stack.push(pos);
        // Explore
        result = sensor(pos);
        if(result[1] != 0){
            var direction = Math.floor( Math.random() * 4 );
            while (result[0][direction] == false){
                direction = Math.floor( Math.random() * 4 );
            }
            if (direction == 0) { pos.y -= 1; }
            if (direction == 1) { pos.x += 1; }
            if (direction == 2) { pos.y += 1; }
            if (direction == 3) { pos.x -= 1; }
        } else {
            result = 1;
            while ( 0 < field.stack.length && result == 0 ){
                var p = Math.floor( Math.random() * field.stack.length );
                console.log(p);
                pos = field.stack[p];
                result = sensor(pos)[1];
                if (result == 0) {
                    field.stack.splice(p,1);
                }
            }
            if ( field.stack.length == 0 ) {
                break;
            }
        }
        count++;
    }
}

function sensor(tg) {
    var dir = Array(4).fill(false);
    var cnt = 0;
    if (1 < tg.y) {
        if (!field.init[(tg.y - 1) * field.range.x + tg.x]) {
            if (!field.init[(tg.y - 2) * field.range.x + tg.x]) {
                dir[0] = true;
                cnt += 1;
            }
        }
    }
    if (tg.x < field.range.x - 2) {
        if (!field.init[tg.y * field.range.x + (tg.x + 1)]) {
            if (!field.init[tg.y * field.range.x + (tg.x + 2)]) {
                dir[1] = true;
                cnt += 1;
            }
        }
    }
    if (tg.y < field.range.y - 2) {
        if (!field.init[(tg.y + 1) * field.range.x + tg.x]) {
            if (!field.init[(tg.y + 2) * field.range.x + tg.x]) {
                dir[2] = true;
                cnt += 1;
            }
        }
    }
    if (1< tg.x) {
        if (!field.init[tg.y * field.range.x + (tg.x - 1)]) {
            if (!field.init[tg.y * field.range.x + (tg.x - 2)]) {
                dir[3] = true;
                cnt += 1;
            }
        }
    }
    return [dir, cnt];
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
