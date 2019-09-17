from SpriteHelper import Screen
from time import sleep

# Create the screen.
screen = Screen(window_name='Graphics Club!')

# Animate the skeleton walking down.
# This assumes you have a sprite sheet titled 'skeleton.png' in your directory.
skeleton_size = 64
skeleton_cols = 8
for i in range(5):
    for col in range(skeleton_size, skeleton_size*skeleton_cols, skeleton_size):
        screen(
            'skeleton.png',
            crop=[col, skeleton_size * 2, skeleton_size, skeleton_size],
            scale=4
        )
        screen.y += 5
        sleep(0.1)

# Animate the explosion.
# This assumes you have a sprite sheet titled 'explosion.png' in your directory.
explosion_size = 100
explosion_rows = 9
explosion_cols = 9
for row in range(0, explosion_size*explosion_rows, explosion_size):
    for col in range(0, explosion_size*explosion_cols, explosion_size):
        screen(
            'explosion.png',
            crop=[col, row, explosion_size, explosion_size],
            scale=(skeleton_size/explosion_size)*4
        )
        sleep(0.001)
