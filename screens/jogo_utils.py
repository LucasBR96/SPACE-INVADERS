import pygame
from pygame.locals import *
pygame.init()

import PPlay
from PPlay.sprite import *

from constantes import *

class ship( Sprite ):

    def __init__( self ):

        super().__init__( SHIP_SPR )
        self.set_position( *SHIP_POS )
        self.last_fire = None
    
    def adjust( self ):

        if self.y < 0:
            self.y = 0
        
        if self.y + self.height > SCREEN_H:
            self.y = SCREEN_H - self.height