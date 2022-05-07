from pathlib import Path

# Surface
WIDTH = 800
HEIGHT = 600

TITLE = 'Save the Cookie Cat'

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game
LIVES = 3
GAME_VOL = 0.8
FPS = 60

# Font
FONT = 'Arial bold'
POS_Y = 20
FONT_SIZE = 36

# Player
PLAYER_SPEED = 10


# Objects
DRILLS_GAP = 300
COOKIES_GAP = 800
SURFACE_MARGIN_LEFT = 0
SURFACE_MARGIN_RIGHT = WIDTH - 70
FALL_SPEED = 10
DRILLS_PER_LEVEL = 8
COOKIES_PER_LEVEL = 5

# Paths
CURRENT_DIRECTORY = Path.cwd()
PATH = Path(CURRENT_DIRECTORY)

SCORE_DIRECTORY = PATH / 'game/sources/score.txt'
SOUNDS_DIRECTORY = PATH / 'game/sources/sounds/'
SPRITES_DIRECTORY = PATH / 'game/sources/sprites/'

# Hasta aquí sigue la posibilidad de que aparezcan en un mismo espacio
DRILLS_GRID = int((SURFACE_MARGIN_RIGHT - SURFACE_MARGIN_LEFT) / 14) # 730 - área en el que puede aparacer