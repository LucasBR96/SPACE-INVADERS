from constantes import *

import PPlay
from PPlay.sprite import *

import time

class Diff():

    @staticmethod
    def start():

        Diff.selected = MEDM

        Diff.center_button = Sprite( DIFF_SPR[ MEDM ] )
        Diff.center_button.set_position( DIFF_POS )

        Diff.add_button = Sprite( ADD_SPR )
        Diff.add_button.set_position( ADD_POS )

        Diff.rmv_button = Sprite( RMV_SPR )
        Diff.rmv_button.set_position( RMV_POS )

        Diff.running = True
        Diff.next_screen = None 

    @staticmethod
    def render_objects( ):
        
        Diff.center_button.image = DIFF_SPR[ Diff.selected ]
        Diff.center_button.draw()

        Diff.add_button.draw()
        Diff.rmv_button.draw()

    @staticmethod
    def update( ):
        pass

    @staticmethod
    def get_input( kb , ms ):
        
        if kb.key_pressed( "esc" ):
            Diff.running = False
            Diff.next_screen = MENU

        if ms.is_off_screen( ):
            return

        a = ms.is_over_object( Diff.add_button )
        b = ms.is_over_object( Diff.rmv_button )
        if not ( a or b ):
            Diff.add_button.image = ADD_SPR
            Diff.rmv_button.image = RMV_SPR
            return
        
        btn = Diff.add_button if a else Diff.rmv_button
        spr = ADD_HVR if a else RMV_HVR
        btn.image = spr

        if not ms.is_button_pressed( 1 ):
            return
        
        val = 1 if a else -1
        Diff.selected += val
        if Diff.selected > HARD: Diff.selected = HARD
        elif Diff.seleceted < EASY: Diff.selected = EASY
        time.sleep( .3 )