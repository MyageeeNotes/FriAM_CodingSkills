// Field info.
var field = {
	'x':10,
	'y': 10,
	'lifes': [],
	'init': undefined,
	'random': 80
}
// Frame info.
var frame = {
	'now': 0,
	'finish': 2019,
	'speed': 10
}

// 1. CREATE MAP DATA
// -- Create bool list
function initWorld(randFlag=0){
	// Initialize Field life list
	field.init = Array(field.x * field.y);
    field.init.fill(false);
	fieldLen = field.init.length;

    // Manual ( randFlag = 0 ) or Random lifes > 0
    if (randFlag > 0){
        // Field ID list
		var arr = [...Array(fieldLen).keys()];
        // set Random field to give life
        var list = [];
		for (var i = 0; i < randFlag; i++) {
			var num = Math.floor(Math.random() * arr.length);
			list.push(arr[num]);
			arr.splice(num,1);
		}
        // set field info.
		for (var i = 0; i < list.length; i++) {
			field.init[list[i]] = true;
		}
	}
}

// 2. VISUALIZATION
// Create HTML tags with 1.map data.
function createWorld() {
	var cnt = 0;
	for (var y = 0; y < field.y; y++) {
		var tr = $('<tr></tr>');
		for (var x = 0; x < field.x; x++) {
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
		this.alives = 0;
		this.center = {
            'x': this.pos[0],
            'y': this.pos[1]
        }
		if(this.life){ this.elem.addClass('alive'); }
        else { this.elem.addClass('dead'); }
	}

	// Toggle life
	godKnows(){
		if(this.life){
			this.life = false;
		} else {
			this.life = true;
		}
		this.setVessel(this.life);
	}

	spend(){
		// Neighbors alives
		this.alives = 0;
		// Left neighbor to Right neighbor [ ■□□ -> □□■ ]
		for (var px = this.center.x - 1; px <= this.center.x + 1; px++) {
			// Is target[x] in field?
			if(px >= 0 && px < field.x){
				// Above neighbor to Bottom neighbor
				for (var py = this.center.y - 1; py <= this.center.y + 1; py++){
					// Is target[y] in field?
					if (py >= 0 && py < field.y) {
						// Is target alive?
						if (this.getVessel([px, py]).hasClass('alive')) {
							// target is not myself?
                            if(!(px == this.center.x && py == this.center.y)){
                                this.alives += 1;
                            }
						}
					}
				}
			}
		}
		// DEAD or ALIVE
		if(this.alives < 2 || 3 < this.alives){
			return false;
		} else if (this.alives == 3){
			// BIRTH
			return true;
		} else {
			return this.life;
		}
	}

	// Return HTML oject
	getVessel(pos){
		return $("#field tr:nth-child(" + (pos[1] + 1) + ") td:nth-child(" + (pos[0] + 1) + ")");
	}

	// Change class
	setVessel(flag){
		var target = this.getVessel(this.pos);
		if(flag){
			target.addClass('alive');
            target.removeClass('dead');
		} else {
			target.addClass('dead');
            target.removeClass('alive');
		}
	}
}

// Manual set
function godhand(x, y) {
	var target = field.lifes[(x * field.x) + y];
	target.godKnows();
}

// Judge life
function spend() {
	frame.now++;
	$("#turn").text(frame.now  + ' years');
	for (var i = 0; i < field.lifes.length; i++) {
		field.init[i] = field.lifes[i].spend();
	 }
	 for (var i = 0; i < field.lifes.length; i++) {
		field.lifes[i].setVessel(field.init[i]);
	 }
}

// -- Main --
$(function () {
	// set Playing stop
	var playing_stat = false;
	initWorld(field.random);
	createWorld();
	var start = setInterval(function() {
		if (playing_stat) {
			spend();
		}
		//FINISH
		if (frame.now == frame.finish) {
			clearInterval(start);
			console.log("end");
		}
	}, frame.speed);

	// Controllers & Buttons
	$("#turn").click(function () { spend(); });
	$("#controller td.stop").click(function(){ frame.now = 0; playing_stat = true; });
	$("#controller td.pause").click(function(){  playing_stat = false;  });
	$("#controller td.play").click(function(){  playing_stat = true; });
});
