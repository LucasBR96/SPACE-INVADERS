import time
from collections import deque

import PPlay
from PPlay.sprite import *
from numpy import exp , random

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
        Play.last_hit   = time.time()
        Play.score      = 0

        Play.minions       = jogo_utils.minion_matrix()
        Play.minions_bolts = deque([])
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

        #----------------------------------------------------
        # Vendo se a nave pode atirar. Isso ocorre quando o tempo
        # passado desde o ultimo disparo e maior que o limite mínimo
        # O primeiro if é executado quando o player da o primeiro dis
        # paro da partida.
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
    def fire_minion():

        minions = Play.minions
        if minions.last_fire == 0:
            minions.last_fire = Play.last_t
        
        wait_time = MINION_FIRE_WAIT + MINION_FIRE_NOISE*random.normal()
        if not( Play.last_t - minions.last_fire > wait_time ):
            return
        minions.last_fire = Play.last_t

        positions = minions.eligible_for_col()
        idx = random.choice( len( positions ) )
        x , y  = positions[ idx ]
        minion = minions.spawn_minion( x , y )
        x , y = minion.x , minion.y
        
        bolt = Sprite( BOLT_SPR )
        bolt.x = x - bolt.width
        bolt.y = y + MINION_H/2
        Play.minions_bolts.append( bolt )

    
    @staticmethod
    def update_scores( count ):
        
        if count == 0:
            return

        dt = time.time() - Play.last_hit
        Play.last_hit += dt

        score = count*( SCORE_MIN + SCORE_MAX*exp( -SCORE_K*dt ))
        Play.score += score

    @staticmethod
    def bolt_update( ship = True ):

        dx = BOLT_SPEED*Play.last_dt

        if ship:
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

        else:
            for bolt in Play.minions_bolts:
                if bolt.x + bolt.width < 0:
                    continue
                bolt.x -= dx
            
            # removendo os bolts que sairam da tela
            while Play.minions_bolts:

                bolt = Play.minions_bolts.popleft()
                if bolt.x + bolt.width > 0:
                    Play.minions_bolts.appendleft( bolt )
                    break
            
    @staticmethod
    def render_objects( window ):

        if Play.ship.should_draw():
            Play.ship.draw()
        # else:
        #     Play.ship.hide()

        for seq in [ Play.ship_bolts , Play.minions_bolts ]:
            for bolt in seq:
                bolt.draw()
        
        mat = Play.minions
        for minion in mat.yield_minions():
            minion.draw()

        #renderizando o score
        s = "{:.2f}".format( Play.score )
        window.draw_text( s , SCREEN_W/2, 20 , size = SCORE_FONT , color = ( 255 , 255 , 255 ) )

        s = "Vidas: {}".format( Play.ship.lifes )
        window.draw_text( s , 3*SCREEN_W/4, 20 , size = SCORE_FONT , color = ( 255 , 255 , 255 ) )

    @staticmethod
    def update( ):

        # Atualizacao do clock do jogo
        t = time.time()
        Play.last_dt = t - Play.last_t
        Play.last_t = t

        if not( Play.running ):
            return
        
        Play.ship.adjust() # ver se o ship escapou da tela
        Play.bolt_update() # calculando as posicoes dos tiros
        Play.bolt_update( False )

        Play.minions.move( Play.last_dt )
        Play.minions.adjust()
        Play.fire_minion()

        Play.check_bolts()
    
    @staticmethod
    def check_bolts():

        count = Play.minions.check_bolt_collision( Play.ship_bolts )
        if not( count is None ):
            Play.update_scores( count )
        
        result = Play.ship.check_bolt_collision( Play.minions_bolts )
        if not ( result is None ):
            Play.minions_bolts.remove( result )
            if Play.ship.update_life_count( Play.last_t ):
                Play.exit()
    
    @staticmethod
    def exit():
        print( "!" )
        Play.running = False
        Play.next_screen = MENU

    @staticmethod
    def get_input( kb , ms ):
        
        if kb.key_pressed( "esc" ):
            Play.exit()

        a = kb.key_pressed( "up" )
        b = kb.key_pressed( "down" )
        if a != b:
            Play.move_ship( a )
        
        if kb.key_pressed( "space" ):
            Play.fire_ship()
