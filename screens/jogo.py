import time
from collections import deque

import PPlay
from PPlay.sprite import *

from constantes import *
from screens import jogo_utils

class Play:

    @staticmethod
    def start():

        Play.running     = True
        Play.next_screen = None
        Play.last_t      = time.time()
        Play.last_dt     = 0

        Play.ship = jogo_utils.ship() 
        Play.ship_bolts = deque([])

        Play.minions = jogo_utils.minion_matrix()
        Play.diff = EASY

    @staticmethod
    def move_ship( up ):

        v = -1 if up else 1
        desloc = v*SHIP_SPEED*Play.last_dt
        Play.ship.y += desloc

    @staticmethod
    def fire_ship():

        ship = Play.ship
        wait = BOLT_RELOAD*( Play.diff + 1 )
        if ship.last_fire is None:
            ship.last_fire = Play.last_t - wait
        
        if ship.last_fire + wait > Play.last_t:
            return        
        ship.last_fire = time.time()

        bolt = Sprite( BOLT_SPR )
        bolt.x = ship.x + ship.width
        bolt.y = ship.y + ( ship.height - bolt.height )/2
        Play.ship_bolts.appendleft( bolt )
    
    @staticmethod
    def bolt_update():

        dx = BOLT_SPEED*Play.last_dt
        for bolt in Play.ship_bolts:
            if bolt.x > SCREEN_W:
                break
            bolt.x += dx
        
        # removendo os bolts que sairam da tela
        while Play.ship_bolts:

            bolt = Play.ship_bolts.pop()
            if bolt.x < SCREEN_W:
                Play.ship_bolts.append( bolt )
                break
            

    @staticmethod
    def render_objects( ):

        Play.ship.draw()
        for bolt in Play.ship_bolts:
            bolt.draw()
        
        mat = Play.minions
        for minion in mat.yield_minions():
            minion.draw()

    @staticmethod
    def update( ):

        t = time.time()
        Play.last_dt = t - Play.last_t
        Play.last_t = t

        if not( Play.running ):
            return
        
        Play.ship.adjust()
        Play.bolt_update()

        Play.minions.move( Play.last_dt )
        Play.minions.adjust()


    @staticmethod
    def get_input( kb , ms ):
        
        if kb.key_pressed( "esc" ):
            print( "!" )
            Play.running = False
            Play.next_screen = MENU

        a = kb.key_pressed( "up" )
        b = kb.key_pressed( "down" )
        if a != b:
            Play.move_ship( a )
        
        if kb.key_pressed( "space" ):
            Play.fire_ship()
