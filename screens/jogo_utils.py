import pygame
from pygame.locals import *
pygame.init()

import numpy

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

class minion_matrix:

    def __init__( self , row = MINION_ROW , col = MINION_COL ):

        self.row = row
        self.col = col
        self.mat = numpy.ones( ( row , col ) )

        top_corner_x = SCREEN_W - ( GAP_W + MINION_W )
        top_corner_y = ( SCREEN_H - self.row*( GAP_H + MINION_H ) )/2
        self.corner = ( top_corner_x , top_corner_y )

        self.moving_up = True

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
        na tal nave 
        '''

        posicoes = []
        row , col = self.row , self.col

        for x in row:
            for y in col:
                if self.mat[ x , y ] == 1:
                    posicoes.append( ( x , y ) )
                break
        
        return posicoes

    def check_bolt_collision( self , ship_bolts ):

        posicoes = self.eligible_for_col()

        m  = map( self.minion_pos , posicoes )
        xs = [ x for ( x , _ ) in m ]
        ys = [ y for ( _ , y ) in m ]
        box_x1 = min( xs )
        box_x2 = max( xs ) + MINION_W
        box_y1 = min( ys )
        box_y2 = max( ys ) + MINION_H

        candidate_bolts = []
        for bolt in ship_bolts:
            
            a = ( bolt.x + bolt.width < box_x1 )
            b = ( bolt.y + bolt.height < box_y1 )
            c = ( bolt.y > box_y2 )
            if any( [ a , b , c ] ):
                continue

            if bolt.x > box_x2:
                break

            candidate_bolts.append( bolt )

        for bolt in candidate_bolts:
            for x , y  in posicoes:

                minion = self.spawn_minion( x , y )
                if bolt.collided_perfect( minion ):
                    self.mat[ x , y ] = 0
        
