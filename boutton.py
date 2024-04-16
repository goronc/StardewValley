import pygame

class Boutton:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def update(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.rect.inflate(-2, -2))

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surface, (127, 255, 212), self.rect.inflate(-2, -2))

        font = pygame.font.Font(None, 24)
        text = font.render("Click Me", True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)
