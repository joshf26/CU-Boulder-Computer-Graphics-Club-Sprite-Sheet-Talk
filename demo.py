from SpriteHelper import start, load, display
from time import sleep

# This assumes we have a sprite sheet called explosion.png that is a 9x9 animation with each frame being 100x100 pixels.
image = load("explosion.png")
size = 100
num_rows = 9
num_cols = 9

# This window is tiny, but big enough to hold the animation.
start(size=[size, size])

for row in range(0, size*num_rows, size):
    for col in range(0, size*num_cols, size):
        display(image, crop=[col, row, size, size])
        sleep(0.01)

