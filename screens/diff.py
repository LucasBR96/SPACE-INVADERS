from constantes import *

import PPlay
from PPlay.sprite import *

import time

class Diff():

    diff_options = [ 0 ]*3

    add_btn = [ SPR , SPR ]
    btn_opt = [ [ 0 , 0 ] , [ 0 , 0 ] ]

    @staticmethod
    def start():

        Diff.selected_df = MEDM

        for x in [ EASY , MEDM , HARD ]:
            Diff.diff_options[ x ] = Sprite( DIFF_SPRS[ x ] )
            Diff.diff_options[ x ].set_position( *DIFF_POSP )
        
        for x in [ ADD , RMV ]:
            Diff.btn_opt[ x ][ SPR ] = Sprite( ALTER_SPR[ x ] )
            Diff.btn_opt[ x ][ SPR ].set_position( *ALTER_POS[ x ] )

            Diff.btn_opt[ x ][ HVR ] = Sprite( ALTER_HVR[ x ] )
            Diff.btn_opt[ x ][ HVR ].set_position( *ALTER_POS[ x ] )

        Diff.running = True
        Diff.next_screen = None

    @staticmethod
    def render_objects( ):

        pos = Diff.selected_df
        selected_diff = Diff.diff_options[ pos ]
        selected_diff.draw()

        x = Diff.add_btn[ ADD ]
        spr = Diff.btn_opt[ ADD ][ x ]
        spr.draw()

        x = Diff.add_btn[ RMV ]
        spr = Diff.btn_opt[ RMV ][ x ]
        spr.draw()

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
        
        for x in [ ADD , RMV ]:

            spr = Diff.btn_opt[ x ][ 0 ]
            if not ms.is_over_object( spr ):
                Diff.add_btn[ x ] = SPR
                continue
            Diff.add_btn[ x ] = HVR







