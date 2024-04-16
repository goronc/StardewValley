import pygame
import sys
from boutton import Boutton
from cookie import Cookie

class Game:
    def __init__(self):
        pygame.init()
        self.size = (1080, 720)
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Cookie Clicker')

        self.button = Boutton(125, 125, 150, 50)
        self.cookie = Cookie(200, 200)

        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.button.rect.collidepoint(event.pos):
                    self.cookie.increment()

    def update(self):
        self.button.update(self.window)
        self.cookie.update(self.window)

    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update()

            pygame.display.update()
            self.clock.tick(60)
