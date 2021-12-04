from constantes import *
# from .jogo_utils import *

import PPlay

class Play:

    @staticmethod
    def start():

        Play.running = True
        Play.next_screen = None 

    @staticmethod
    def render_objects( ):
        pass

    @staticmethod
    def update( ):
        pass

    @staticmethod
    def get_input( kb , ms ):
        
        if kb.key_pressed( "esc" ):
            print( "!" )
            Play.running = False
            Play.next_screen = MENU 