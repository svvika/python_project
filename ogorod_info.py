BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (75, 37, 0)

WIDTH = 600
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

TILE_SIZE = 60
TILE_NUM_W = WIDTH // TILE_SIZE
TILE_NUM_H = HEIGHT // TILE_SIZE

PLAYER = "character2.png"
OBJECT = "carrot.png"

FPS = 15
# Optimal for tile size 60 (10 tiles/row) = (FPS - 2) * 2
# ? Optimal for tile size 75 (8 tiles/row) = (FPS - 4) * 2
if TILE_SIZE == 75:
    TPS = (FPS - 4) * 2
elif TILE_SIZE == 60:
    TPS = (FPS - 2) * 2

WIN_COUNT = 30
