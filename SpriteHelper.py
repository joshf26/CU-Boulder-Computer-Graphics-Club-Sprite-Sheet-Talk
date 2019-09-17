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


class Screen:
    def __init__(self, size=None, window_name='Sprite Helper'):
        if size is None:
            size = [640, 480]

        self.images = {}

        self.x = 0
        self.y = 0

        # Setup pygame window.
        pygame.init()
        pygame.display.set_caption(window_name)
        self.screen = pygame.display.set_mode(size)
        pygame.display.flip()

        # Start event loop in another thread to keep the pygame window open.
        threading.Thread(target=_event_loop).start()

    def __call__(self, path, crop=None, scale=1):
        # Check if the image has already been loaded.
        if path not in self.images:
            self.images[path] = pygame.image.load(path)

        image = self.images[path]

        # Clear the screen.
        self.screen.fill([0, 0, 0])

        # Apply scaling.
        if not scale == 1:
            image = pygame.transform.scale(image, (
                int(image.get_width() * scale),
                int(image.get_height() * scale)
            ))
            # x_pos = self.x * scale
            # y_pos = self.y * scale

        # Apply cropping.
        if crop:
            crop = [int(i * scale) for i in crop]
        else:
            crop = [0, 0, image.get_width(), image.get_height()]

        # Display the image.
        self.screen.blit(image, [self.x, self.y], crop)
        pygame.display.flip()
