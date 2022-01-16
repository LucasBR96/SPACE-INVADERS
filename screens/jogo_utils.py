import time

import pygame
from pygame.locals import *
pygame.init()
import numpy

import PPlay
from PPlay.sprite import *

from constantes import *

class ship( Sprite ):

    def __init__( self , lifes = 5  ):

        super().__init__( SHIP_SPR )
        self.set_position( *SHIP_POS )
        self.last_fire = None

        self.lifes      = lifes
        self.invincible = False
        self.last_hit   = 0
    
    def adjust( self ):

        if self.y < 0:
            self.y = 0
        
        if self.y + self.height > SCREEN_H:
            self.y = SCREEN_H - self.height
    
    def update_life_count( self , last_t ):

        self.last_hit = last_t

        self.lifes -= 1
        self.set_position( *SHIP_POS )
        return self.lifes <= 0
    
    def should_draw( self ):

        self.invincible = ( time.time() - self.last_hit < SHIP_INVC ) 
        if not self.invincible:
            return True
        
        delta_t = time.time() - self.last_hit
        k = numpy.floor( delta_t/SHIP_BLINK_TIME )
        return int( k )%2 == 0
    

    def check_bolt_collision( self , minion_bolts ):

        if self.invincible or not minion_bolts:
            return

        result = None
        # minion_bolts.sort( key = lambda b : b.x )

        for bolt in minion_bolts:

            if bolt.x > self.x + self.width:
                break

            if self.collided( bolt ):
                result = bolt
                break
        
        return result
class minion_matrix:

    def __init__( self , row = MINION_ROW , col = MINION_COL ):

        self.row = row
        self.col = col
        self.mat = numpy.ones( ( row , col ) )

        top_corner_x = SCREEN_W - ( GAP_W + MINION_W )
        top_corner_y = ( SCREEN_H - self.row*( GAP_H + MINION_H ) )/2
        self.corner = ( top_corner_x , top_corner_y )

        self.moving_up = True
        self.last_fire = 0

    def minion_pos( self , x , y ):

        mat_x , mat_y = self.corner
        minion_x = mat_x + y*( MINION_W + GAP_W )        
        minion_y = mat_y + x*( MINION_H + GAP_H )

        return ( minion_x, minion_y )

    def spawn_minion( self , x , y ):

        minion_x, minion_y = self.minion_pos( x , y )
        minion = Sprite( MINION_SPRITE )
        minion.set_position( minion_x , minion_y )

        return minion

    def yield_minions( self ):

        for x in range( self.row ):
            for y in range( self.col ):

                if self.mat[ x , y ] == 0:
                    continue

                yield self.spawn_minion( x , y )

    def move( self , dt ):

        x , y = self.corner

        x += MINION_SPEED_X*dt
        k = -1 if self.moving_up else 1
        y += k*MINION_SPEED_Y*dt

        self.corner = ( x , y )

    def adjust( self ):

        '''
            Corrige a posicao dos minions caso eles escapem da tela
        '''
        x , y = self.corner

        if y < 0:
            self.corner = ( x , 0 )
            self.moving_up = False
        
        if y + self.row*( MINION_H + GAP_H) > SCREEN_H:
            self.corner = ( x , SCREEN_H - self.row*( MINION_H + GAP_H) ) 
            self.moving_up = True

    def eligible_for_col( self ):

        '''
        retorna as posicoes de todos os minions que podem ser
        atingidos pelo laser da nave. Ou todos que podem atirar
        na tal nave. O criterio para ser elegível é não existir
        um outro minion entre a posição e a nave 
        '''

        posicoes = []
        row , col = self.row , self.col

        for x in range( row ):
            for y in range( col ):
                if self.mat[ x , y ] == 1:
                    posicoes.append( ( x , y ) )
                    break
        
        return posicoes

    def check_bolt_collision( self , ship_bolts ):

        '''
        Verifica se algum disparo da nave vai atingiu algum minion
        Essa é a versão ja otimizada
        '''

        if not ship_bolts:
            return

        #----------------------------------------------------------
        # Primeiro são selecionadas as posições vulneraveis aos disparos
        # da nave, e cria-se um caixa de colisão ao redor delas 
        posicoes = self.eligible_for_col()
        m  = [ self.minion_pos( x , y ) for x , y in posicoes ]
        xs = [ x for ( x , _ ) in m ]
        ys = [ y for ( _ , y ) in m ]
        box_x1 = min( xs )
        box_x2 = max( xs ) + MINION_W
        box_y1 = min( ys )
        box_y2 = max( ys ) + MINION_H

        #---------------------------------------------------------
        # Agora são selecionados os projeteis que interceptam tal
        # caixa
        candidate_bolts = []
        for bolt in ship_bolts:
            
            a = ( bolt.x + bolt.width < box_x1 )
            b = ( bolt.y + bolt.height < box_y1 )
            c = ( bolt.y > box_y2 )
            if any( [ a , b , c ] ):
                continue
            
            # ---------------------------------------------------
            # como os disparos estão ordenados da nave para os minions
            # qualquer projetil a partir da primeira que esteja atrás 
            # da caixa pode ser descartado.
            if bolt.x > box_x2:
                break

            candidate_bolts.append( bolt )
        
        if not candidate_bolts:
            return
        
        #---------------------------------------------------------
        # depois de filtrados os bolts e minions, agora da pra testar para
        # valer
        count = 0
        for bolt in candidate_bolts:
            for x , y  in posicoes:

                minion = self.spawn_minion( x , y )
                if bolt.collided( minion ):
                    self.mat[ x , y ] = 0
                    ship_bolts.remove( bolt )
                    count += 1
                    break
        return count

        
