
# All screens --------------------------------------------
SCREEN_H = 450
SCREEN_W = 1200
BACKGROUND = 'assets/via-lactea.jpg'

MENU = 0
PLAY = 1
DIFF = 2
RANK = 3
EXIT = 4

SPR = 0
HVR = 1

# Menu screen -------------------------------------------

# Positioning
BUTTON_W = 200
BUTTON_H = 70
W_GAP    = 80

PLAY_POS = ( W_GAP , SCREEN_H/2 - BUTTON_H/2 )
PLAY_SPR = 'assets/menu/botao_jogar.png'
PLAY_HVR = 'assets/menu/hover_jogar.png'

DIFF_POS = ( 2*W_GAP + BUTTON_W , PLAY_POS[ 1 ] )
DIFF_SPR = 'assets/menu/botao_diff.png'
DIFF_HVR = 'assets/menu/hover_diff.png'

RANK_POS = ( 3*W_GAP + 2*BUTTON_W , PLAY_POS[ 1 ] )
RANK_SPR = 'assets/menu/botao_rank.png'
RANK_HVR = 'assets/menu/hover_rank.png'

EXIT_POS = ( 4*W_GAP + 3*BUTTON_W  , PLAY_POS[ 1 ] )
EXIT_SPR = 'assets/menu/botao_sair.png'
EXIT_HVR = 'assets/menu/hover_sair.png'

#---------------------------------------------------
#jogo em si

SHIP_W = 48
SHIP_H = 52
SHIP_SPEED = 200 #pixels per second

SHIP_LIFES = [ 7 , 5 , 3 ]

SHIP_INVC = 2.
SHIP_BLINK_TIME = SHIP_INVC/8

SHIP_SPR = 'assets/game_sprites/nave.png'
SHIP_POS = ( 0 , ( SCREEN_H - SHIP_H )/2 )

BOLT_SPR = 'assets/game_sprites/bolt.png'
BOLT_SPEED = 500
BOLT_RELOAD = .3

MINION_W = 21
MINION_H = 26
GAP_W = MINION_W/2
GAP_H = MINION_H/2
MINION_ROW = 8
MINION_COL = 3

MINION_SPEED_Y = SCREEN_H/3
MINION_SPEED_X = -SCREEN_W/48

MINION_SPRITE = "assets/game_sprites/minion.png"

SCORE_MIN = 1
SCORE_MAX = 4
SCORE_K   = .7

SCORE_FONT = 16
SCORE_POS  = ( SCREEN_W/2 , 20 )

MINION_FIRE_WAIT  = .3
MINION_FIRE_NOISE = .03
#---------------------------------------------------
#Dificulade
EASY = 0
MEDM = 1
HARD = 2

DIFF_POSP = ( ( SCREEN_W - BUTTON_W )/2 , ( SCREEN_H - BUTTON_H )/2 )
DIFF_SPRS = {}
DIFF_SPRS[ EASY ] = 'assets/diff/easy.png'
DIFF_SPRS[ MEDM ] = 'assets/diff/medm.png'
DIFF_SPRS[ HARD ] = 'assets/diff/hard.png'

ADD = 0
RMV = 1

ADD_DIF_X0 = ( DIFF_POSP[ 0 ] - W_GAP - BUTTON_H )
ADD_DIF_X1 = ( DIFF_POSP[ 0 ] + W_GAP + BUTTON_W )
ADD_DIF_Y  = DIFF_POSP[ 1 ]

ALTER_POS = {}
ALTER_POS[ ADD ] = ( ADD_DIF_X1 , ADD_DIF_Y )
ALTER_POS[ RMV ] = ( ADD_DIF_X0 , ADD_DIF_Y )

ALTER_SPR = {}
ALTER_SPR[ ADD ] = 'assets/diff/add.png'
ALTER_SPR[ RMV ] = 'assets/diff/rmv.png'

ALTER_HVR = {}
ALTER_HVR[ ADD ] = 'assets/diff/ahvr.png'
ALTER_HVR[ RMV ] = 'assets/diff/rhvr.png'
