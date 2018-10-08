import pygame
import threading


def _event_loop():
    """ Keeps the pygame window open in another thread. """

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False


def start(size=None, window_name='Sprite Helper'):
    """ Opens the pygame window and keeps it open. """

    global screen

    if size is None:
        size = [640, 480]

    # Setup pygame window.
    pygame.init()
    pygame.display.set_caption(window_name)
    screen = pygame.display.set_mode(size)
    pygame.display.flip()

    # Start event loop in another thread to keep the pygame window open.
    threading.Thread(target=_event_loop).start()


def load(path):
    """ Wrapper around pygame's image load function. """

    image = pygame.image.load(path)
    return image


def display(image, position=None, crop=None, scale=1):
    """ Displays an image on the screen. """

    global screen

    if position is None:
        position = [0, 0]

    # Clear the screen.
    screen.fill([0, 0, 0])

    # Apply scaling.
    if not scale == 1:
        image = pygame.transform.scale(image, (
            int(image.get_width() * scale),
            int(image.get_height() * scale)
        ))
        position[0] *= scale
        position[1] *= scale

    # Apply cropping.
    if crop:
        crop = [int(i * scale) for i in crop]
    else:
        crop = [0, 0, image.get_width(), image.get_height()]

    # Display the image.
    screen.blit(image, position, crop)
    pygame.display.flip()
