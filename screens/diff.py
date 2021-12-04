from constantes import *

import PPlay
from PPlay.sprite import *

import time

class Diff():

    @staticmethod
    def start():

        Diff.selected = MEDM
        Diff.set_diff()
        
        Diff.alter_buttons = {}
        Diff.change_alt_button( ADD )
        Diff.change_alt_button( RMV )

        Diff.running = True
        Diff.next_screen = None

    @staticmethod
    def set_diff():
        Diff.center_button = Sprite( DIFF_SPRS[ Diff.selected ] )
        Diff.center_button.set_position( *DIFF_POSP )
    
    def change_alt_button( butt , hvr = False ):

        img = ALTER_SPR[ butt ]
        if hvr:
            img = ALTER_HVR[ butt ]
        pos = ALTER_POS[ butt ]

        Diff.alter_buttons[ butt ] = Sprite( img )
        Diff.alter_buttons[ butt ].set_position( *pos )

    @staticmethod
    def render_objects( ):
        
        Diff.center_button.draw()
        
        if Diff.selected != HARD:
            Diff.alter_buttons[ ADD ].draw()
        
        if Diff.selected != EASY:
            Diff.alter_buttons[ RMV ].draw()

    @staticmethod
    def update( ):
        pass

    @staticmethod
    def get_input( kb , ms ):
        
        if kb.key_pressed( "esc" ):
            Diff.running = False
            Diff.next_screen = MENU

        if ms.is_off_screen():
            return
        
        for butt in [ ADD , RMV ]:

            spr = Diff.alter_buttons[ butt ]
            hvr = False
            if ms.is_over_object( spr ):
                hvr = True
            Diff.change_alt_button( butt , hvr )

            if not( hvr and ms.is_button_pressed( 1 ) ):
                continue

            val = 1 if butt == ADD else -1
            Diff.selected += val
            if Diff.selected > HARD: Diff.selected = HARD
            elif Diff.selected < EASY: Diff.selected = EASY

            time.sleep( .3 )  


