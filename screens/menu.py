from constantes import *

import PPlay
from PPlay.sprite import *

import pygame
from pygame.locals import *

pygame.init()

class Menu:

    @staticmethod
    def start():
        
        Menu.buttons = {}

        Menu.buttons[ PLAY ] = Sprite( PLAY_SPR )
        Menu.buttons[ PLAY ].set_position( *PLAY_POS )

        Menu.buttons[ DIFF ] = Sprite( DIFF_SPR )
        Menu.buttons[ DIFF ].set_position( *DIFF_POS )

        Menu.buttons[ RANK ] = Sprite( RANK_SPR )
        Menu.buttons[ RANK ].set_position( *RANK_POS )

        Menu.buttons[ EXIT ] = Sprite( EXIT_SPR )
        Menu.buttons[ EXIT ].set_position( *EXIT_POS )

        Menu.running = True
        Menu.next_screen = None

    @staticmethod
    def render_objects():
        for _ , button in Menu.buttons.items():
            button.draw()
    
    @staticmethod
    def get_input( kb , ms ):

        if ms.is_off_screen():
            return

        for i , button in Menu.buttons.items():

            a = ms.is_over_object( button )
            b = ms.is_button_pressed( 1 )
            if a:
                print( i )

            if a and b:
                Menu.running = False
                Menu.next_screen = i


           
        
        
    