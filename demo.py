from SpriteHelper import start, load, display
from time import sleep

image = load("explosion.png")
size = 1000
num_rows = 9
num_cols = 9

start(size=[size, size])

for row in range(0, size*num_rows, size):
    for col in range(0, size*num_cols, size):
        display(image, crop=[col, row, size, size])
        sleep(0.01)

