
# All screens --------------------------------------------
SCREEN_H = 450
SCREEN_W = 1200
BACKGROUND = 'assets/via-lactea.jpg'

MENU = 0
PLAY = 1
DIFF = 2
RANK = 3
EXIT = 4

# Menu screen -------------------------------------------

# Positioning
BUTTON_W = 200
BUTTON_H = 100
W_GAP    = 80

PLAY_POS = ( W_GAP , SCREEN_H/2 - BUTTON_H/2 )
PLAY_SPR = 'assets/botao_jogar.png'
PLAY_HVR = 'assets/hover_jogar.png'

DIFF_POS = ( 2*W_GAP + BUTTON_W , PLAY_POS[ 1 ] )
DIFF_SPR = 'assets/botao_diff.png'
DIFF_HVR = 'assets/hover_diff.png'

RANK_POS = ( 3*W_GAP + 2*BUTTON_W , PLAY_POS[ 1 ] )
RANK_SPR = 'assets/botao_rank.png'
RANK_HVR = 'assets/hover_rank.png'

EXIT_POS = ( 4*W_GAP + 3*BUTTON_W  , PLAY_POS[ 1 ] )
EXIT_SPR = 'assets/botao_sair.png'
EXIT_HVR = 'assets/hover_sair.png'

#---------------------------------------------------
#jogo em si

#---------------------------------------------------
#Dificulade
EASY = 1
MEDM = 2
HARD = 3

DIFF_POS = ( ( SCREEN_W - BUTTON_W )/2 , ( SCREEN_H - BUTTON_H )/2 )
DIFF_SPR = {}
DIFF_SPR[ EASY ] = 'assets/diff/easy.png'
DIFF_SPR[ MEDM ] = 'assets/diff/medm.png'
DIFF_SPR[ HARD ] = 'assets/diff/hard.png'

ADD_DIF_X0 = ( DIFF_POS[ 0 ] - W_GAP - BUTTON_H )
ADD_DIF_X1 = ( DIFF_POS[ 0 ] + W_GAP + BUTTON_W )
ADD_DIF_Y  = DIFF_POS[ 1 ]

ADD_POS = ( ADD_DIF_X1 , ADD_DIF_Y )
ADD_SPR = 'assets/diff/add.png'
ADD_HVR = 'assets/diff/ahvr.png'

RMV_POS = ( ADD_DIF_X0 , ADD_DIF_Y )
RMV_SPR = 'assets/diff/rmv.png'
RMV_HVR = 'assets/diff/rhvr.png'