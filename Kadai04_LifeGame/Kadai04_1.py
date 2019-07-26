# using: utf-8

import pygame
from pygame.locals import *
import sys
import Math

if __name__ == '__main__':
    # SET UP -----
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Life Game - Kadai0205")

    # Field info.
    field = {
        'x': 10,
        'y': 10,
        'lifes': [],
        'init': None,
        'random': 80
    }
    # Frame info.
    frame = {
        'now': 0,
        'finish': 2019,
        'speed': 10
    }

    # 1.CREATE MAP DATA
    # -- Create bool list
    def initWorld(randFlag=0):
        # Initialize Field life list
        field.init = [False * field.x * field.y]
        fieldLen = len(field.init)

        # Manual(randFlag=0) or Random lifes > 0
        if randFlag > 0:
            # Field ID list
            arr = range(fieldLen)
            # set Random field to give life
            l = []
            for i in range(randFlag):
                num = Math.floor(Math.random() * arr.length)
            list.push(arr[num])
            arr.splice(num, 1)

            # set field info.
            for i in range(len(l)):
                field.init[l[i]] = True

    # 2. VISUALIZATION
    # Create HTML tags with 1.map data.
    def createWorld():
        cnt = 0
        for y in range(field.y):
            tr = $('<tr></tr>')
        for x in range(field.x):
            td = new Life([x, y], field.init[cnt])
            tr.append(td.elem)
            field['lifes'].push(td)
            cnt += 1

        $('#field').append(tr)


    class Life:
        def __init__(self, pos, life):
            self.pos = pos;
            self.life = life;
            self.elem = $('<td></td>');
            self.elem.attr('id', 'x' + pos[1] + 'y' + pos[0]);
            self.elem.attr('onclick', 'godhand(' + pos[1] + ',' + pos[0] + ');');
            self.alives = 0;
            self.center = {
                'x': self.pos[0],
                'y': self.pos[1]
            }
            if self.life:
                self.elem.addClass('alive')
            else:
                self.elem.addClass('dead')

            # Toggle life
            def godKnows():
                if self.life:
                    self.life = false
                else:
                    self.life = true
                    self.setVessel(self.life)

        def spend():
            # Neighbors alives
            self.alives = 0;
            # Left neighbor to Right neighbor[■□□ -> □□■]
            for i in range(3):
                px = self.center.x - 1 + i
                # Is target[x] in field?
                if px >= 0 and px < field.x:
                    # Above neighbor to Bottom neighbor
                    for j in range(3):
                        py = self.center.y - 1 + i
                        # Is target[y] in field?
                        if(py >= 0 and py < field.y:
                            # Is target alive?
                            if (self.getVessel([px, py]).hasClass('alive')):
                                # target is not myself?
                                if not (px == self.center.x and py == self.center.y):
                                    self.alives += 1
            # DEAD or ALIVE
            if self.alives < 2 or 3 < self.alives:
                return False
            elif self.alives == 3:
                # BIRTH
                return true
            else:
                return self.life

        # Return HTML oject
        def getVessel(pos):
            return $("#field tr:nth-child(" + (pos[1] + 1) + ") td:nth-child(" + (pos[0] + 1) + ")")

        # Change class
        def setVessel(flag):
            target = self.getVessel(self.pos)
            if flag:
                target.addClass('alive')
                target.removeClass('dead')
            else:
                target.addClass('dead')
                target.removeClass('alive')

        # Manual set
        def godhand(x, y):
            target = field.lifes[(x * field.x) + y]
            target.godKnows()

    # Judge life
    def spend():
        frame.now += 1
        $("#turn").text(frame.now + ' years')
        for i in range(len(field.lifes)):
            field.init[i] = field.lifes[i].spend()
        for i in range(len(field.lifes)):
            field.lifes[i].setVessel(field.init[i])

    # ------------------------------------------------------------------
    # set Playing stop
    playing_stat = False
    initWorld(field.random)
    createWorld()

    while True:
        if playing_stat:
            spend()
        # FINISH
        if frame.now == frame.finish:
            clearInterval(start)
            console.log("end")

        # Renew background image
        screen.fill((0, 0, 0))
        pygame.display.update()

        # Events
        for event in pygame.event.get():

            # Close window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()