from constantes import *
from screens import jogo_utils

import PPlay
import time

class Play:

    @staticmethod
    def start():

        Play.running     = True
        Play.next_screen = None
        Play.last_t      = time.time()
        Play.last_dt     = 0

        Play.ship = jogo_utils.ship() 

    @staticmethod
    def render_objects( ):

        Play.ship.draw()
        pass

    @staticmethod
    def update( ):

        t = time.time()
        Play.last_dt = t - Play.last_t
        Play.last_t = t

        if not( Play.running ):
            return
        
        Play.ship.adjust()

    @staticmethod
    def get_input( kb , ms ):
        
        if kb.key_pressed( "esc" ):
            print( "!" )
            Play.running = False
            Play.next_screen = MENU

        v = 0
        if kb.key_pressed( "up" ):
            v = -1
        elif kb.key_pressed( "down" ):
            v = 1
        desloc = v*SHIP_SPEED*Play.last_dt
        Play.ship.y += desloc