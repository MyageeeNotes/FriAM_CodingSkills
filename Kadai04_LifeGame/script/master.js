var field = {
  'range': [30, 30],
  'lifes': [],
  'init': undefined
}
var frame = {
  'now': 0,
  'finish': 10
}

function initWorld(randFlag=0){
  field['init'] = Array(field.range[0] * field.range[1]);
  field['init'].fill(false);
  fieldLen = field['init'].length;
  if (randFlag > 0){
    var arr = [...Array(fieldLen).keys()];
    var list = [];
    for (var i = 0; i < randFlag; i++) {
      var num = Math.floor(Math.random() * arr.length);
      list.push(arr[num]);
      arr.splice(num,1);
    }
    for (var i = 0; i < list.length; i++) {
      field['init'][list[i]] = true;
    }
  }
}

function createWorld() {
  var cnt = 0;
  for (var y = 0; y < field.range[1]; y++) {
    var tr = $('<tr></tr>');
    for (var x = 0; x < field.range[0]; x++) {
      var td = new Life([x ,y], field.init[cnt]);
      tr.append(td.elem);
      field['lifes'].push(td);
      cnt += 1;
    }
    $('#field').append(tr);
  }
}

class Life {
  constructor(pos, life) {
    this.pos = pos;
    this.life = life;
    this.elem = $('<td></td>');
    this.elem.attr('id', 'x' + pos[1] + 'y' + pos[0]);
    this.elem.attr('onclick', 'godhand(' + pos[1] + ',' + pos[0] + ');');
    if(this.life){ this.elem.addClass('alive'); }
  }

  godKnows(){
    if(this.life){
      this.life = false;
    } else {
      this.life = true;
    }
    this.setVessel(this.life);
  }

  spend(){
    var alives = 0;
    var center = this.pos;
    for (var px = center[0] - 1; px <= center[0] + 1; px++) {
      if(px >= 0 && px != center[0] && px < field.range[0]){
        for (var py = center[1] - 1; py <= center[1] + 1; py++){
          if (py >= 0 && py != center[1] && py < field.range[1]) {
            if (field.lifes[(px * field.range[0]) + py].life) {
              alives += 1;
            }
          }
        }
      }
    }
    if(alives < 2 || 3 < alives){
      this.life = false;
    } else if (alives == 2){
      this.life = true;
    }
    this.setVessel(this.life);
  }

  getVessel(pos){
    return $("#field tr:nth-child(" + (pos[1] + 1) + ") td:nth-child(" + (pos[0] + 1) + ")");
  }

  setVessel(flag){
    var target = this.getVessel(this.pos);
    if(flag){
      target.addClass('alive');
    } else {
      target.removeClass('alive');
    }
  }
}

function godhand(x, y) {
  var target = field.lifes[(x * field.range[0]) + y];
  target.godKnows();
}

$(function () {
  initWorld(50);
  createWorld();

  var start = setInterval(function() {
    frame.now++;
    console.log('TURN:', frame.now);
  	for (var i = 0; i < field.lifes.length; i++) {
      field.lifes[i].spend();
     }
    //FINISH
		if (frame.now == frame.finish) {
		  clearInterval(start);
      console.log("end");
    }
  }, 500);
});
