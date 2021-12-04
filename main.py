import pygame
from pygame.locals import *

import PPlay
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.keyboard import *

from constantes import *
import screens
from screens.menu import Menu
from screens.jogo import Play
from screens.diff import Diff

def switch_screen():

    global screen
    if screen.next_screen == EXIT:
        sys.exit()
    
    # screen_options = [ Menu , Play , Diff , Rank ]
    screen_options = [ Menu , Play , Diff ]
    screen = screen_options[ screen.next_screen ]
    screen.start()


def init_globals():

    global janela
    janela = Window( SCREEN_W , SCREEN_H )
    janela.set_title( "space invaders" )

    global fundo
    fundo = GameImage( BACKGROUND )

    global ms
    ms = Mouse()

    global kb
    kb = Keyboard()

    global screen
    Menu.start()
    screen = Menu

def main():

    init_globals()
    while True:
        
        fundo.draw()

        if screen.running:
            screen.render_objects()
            screen.get_input( kb , ms )
        else:
            switch_screen()

        janela.update()

if __name__ == "__main__":
    main()