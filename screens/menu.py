from constantes import *

import PPlay
from PPlay.sprite import *
from PPlay.gameimage import *

import pygame
from pygame.locals import *

pygame.init()

class Menu:

    @staticmethod
    def start():
        
        opt_types = [ PLAY , DIFF , RANK , EXIT ]

        Menu.buttons = { x:dict() for x in opt_types }

        Menu.buttons[ PLAY ][ SPR ] = Sprite( PLAY_SPR )
        Menu.buttons[ PLAY ][ SPR ].set_position( *PLAY_POS )
        Menu.buttons[ PLAY ][ HVR ] = Sprite( PLAY_HVR )
        Menu.buttons[ PLAY ][ HVR ].set_position( *PLAY_POS )

        Menu.buttons[ DIFF ][ SPR ] = Sprite( DIFF_SPR )
        Menu.buttons[ DIFF ][ SPR ].set_position( *DIFF_POS )
        Menu.buttons[ DIFF ][ HVR ] = Sprite( DIFF_HVR )
        Menu.buttons[ DIFF ][ HVR ].set_position( *DIFF_POS )

        Menu.buttons[ RANK ][ SPR ] = Sprite( RANK_SPR )
        Menu.buttons[ RANK ][ SPR ].set_position( *RANK_POS )
        Menu.buttons[ RANK ][ HVR ] = Sprite( RANK_HVR )
        Menu.buttons[ RANK ][ HVR ].set_position( *RANK_POS )

        Menu.buttons[ EXIT ][ SPR ] = Sprite( EXIT_SPR )
        Menu.buttons[ EXIT ][ SPR ].set_position( *EXIT_POS )
        Menu.buttons[ EXIT ][ HVR ] = Sprite( EXIT_HVR )
        Menu.buttons[ EXIT ][ HVR ].set_position( *EXIT_POS )

        Menu.selected = { x:SPR for x in opt_types }
        Menu.running = True
        Menu.next_screen = None

    @staticmethod
    def render_objects():
        for a , b in Menu.selected.items():
            spr = Menu.buttons[ a ][ b ]
            spr.draw()

    @staticmethod
    def update():
        pass
    
    @staticmethod
    def get_input( kb , ms ):

        if ms.is_off_screen():
            return

        for i , j in Menu.selected.items():
            
            spr = Menu.buttons[ i ][ j ]

            a = ms.is_over_object( spr )
            b = ms.is_button_pressed( 1 )
            
            Menu.selected[ i ] = SPR
            if a:
                Menu.selected[ i ] = HVR

            if a and b:
                Menu.running = False
                Menu.next_screen = i


           
        
        
    