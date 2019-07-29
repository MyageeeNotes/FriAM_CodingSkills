# using: utf-8

import pygame
from pygame.locals import *
import sys
import random
import time
import math

# Field info.
field = {
    'title': "Life Game - Kadai0205",
    'size': (720, 720),
    'x': 34,
    'y': 34,
    'screen': None,
    'lifes': [],
    'init': None,
    'random': 200
}
# Frame info.
frame = {
    'now': 0,
    'finish': 2019,
    'speed': 100
}

if __name__ == '__main__':

    # Drawing
    def mapping(axis_x, axis_y, flag):
        size = {
            'x': field['size'][0] / field['x'],
            'y': field['size'][1] / field['y'],
        }
        if flag == 2:
            pygame.draw.rect(
                field['screen'],
                (200, 100, 100),
                Rect(
                    axis_x * size['x'] + 1,
                    axis_y * size['y'] + 1,
                    size['x'] - 1, size['y'] - 2
                ))
        else:
            if flag:
                pygame.draw.rect(
                    field['screen'],
                    (200, 200, 200),
                    Rect(
                        axis_x * size['x'] + 1,
                        axis_y * size['y'] + 1,
                        size['x'] - 1, size['y'] - 2
                    ))
            else:
                pygame.draw.rect(
                    field['screen'],
                    (60, 60, 60),
                    Rect(
                        axis_x * size['x'] + 1,
                        axis_y * size['y'] + 1,
                        size['x'] - 1, size['y'] - 2
                    ))


    # SET UP -----
    pygame.init()
    field['screen'] = pygame.display.set_mode(field['size'])
    pygame.display.set_caption("Life Game - Kadai0205")

    # 1.CREATE MAP DATA
    # -- Create bool list
    def init_world(rand_flag=0):
        # Initialize Field life list
        field['init'] = [False] * (field['x'] * field['y'])
        field_len = len(field['init'])

        # Manual(rand_flag=0) or Random lifes > 0
        if rand_flag > 0:
            # Field ID list
            arr = list(range(field_len))
            # set Random field to give life
            lst = []
            for i in range(rand_flag):
                num = random.randint(0, len(arr) - 1)
                lst.append(arr[num])
                del arr[num]

            # set field info.
            for i in lst:
                field['init'][i] = True

    # 2. VISUALIZATION
    # Create HTML tags with 1.map data.
    def create_world():
        cnt = 0
        for y in range(field['y']):
            for x in range(field['x']):
                mapping(x, y, field['init'][cnt])
                td = Life([x, y], field['init'][cnt])
                field['lifes'].append(td)
                cnt += 1


    class Life:
        def __init__(self, pos, life):
            self.pos = pos
            self.life = life
            self.alives = 0
            self.center = {
                'x': self.pos[0],
                'y': self.pos[1]
            }

        def spend(self):
            # Neighbors alives
            self.alives = 0
            for i in range(9):
                px = self.center['x'] - 1 + math.floor(i % 3)
                py = self.center['y'] - 1 + math.floor(i / 3)
                # Is target in field?
                in_field_x = 0 <= px < field['x']
                in_field_y = 0 <= py < field['y']
                # Is not Myself
                not_myself = not (px == self.center['x'] and py == self.center['y'])
                if in_field_x and in_field_y and not_myself:
                    # Is target alive?
                    if self.get_vessel([px, py]).life:
                        self.alives += 1
            # DEAD or ALIVE
            if self.alives < 2 or 3 < self.alives:
                return False
            elif self.alives == 3:
                # BIRTH
                return True
            else:
                return self.life

        # Return oject
        def get_vessel(self, pos):
            return field['lifes'][pos[0] + pos[1] * field['x']]

        # Change class
        def set_vessel(self, flag):
            target = self.get_vessel(self.pos)
            target.life = flag

        # Manual set
        def god_hand(self):
            self.life = not self.life
            field['init'][self.pos[0] + self.pos[1] * field['x']] = self.life

    # Vessel Update
    def vessel_update():
        cnt = 0
        for y in range(field['y']):
            for x in range(field['x']):
                mapping(x, y, field['init'][cnt])
                cnt += 1

    # Judge life
    def spend():
        frame['now'] += 1
        for i in range(len(field['lifes'])):
            field['init'][i] = field['lifes'][i].spend()
        for i in range(len(field['lifes'])):
            field['lifes'][i].set_vessel(field['init'][i])

    # ------------------------------------------------------------------
    # set Playing stop
    playing_stat = True
    init_world(field['random'])
    create_world()

    while True:
        # Renew background image
        field['screen'].fill((50, 50, 50))

        if playing_stat:
            pygame.display.set_caption(field['title'] + " - START")
            spend()
        else:
            pygame.display.set_caption(field['title'] + " - STOP")
        vessel_update()

        # FINISH
        if frame['now'] == frame['finish']:
            print("Finish -- Max Frames: {}".format(frame['finish']))
            break

        pygame.display.update()

        # Events
        for event in pygame.event.get():
            # Close window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Keyboard event
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    playing_stat = not playing_stat
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                size = {
                    'x': field['size'][0] / field['x'],
                    'y': field['size'][1] / field['y'],
                }
                size['x'] - 1, size['y'] - 2
                px = math.floor(x / size['x'])
                py = math.floor(y / size['y'])
                field['lifes'][px + py * field['x']].god_hand()
                vessel_update()

        time.sleep(frame['speed'] / 1000)
