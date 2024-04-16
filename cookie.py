import pygame

class Cookie:
    def __init__(self, x, y):
        self.value = 0
        self.font = pygame.font.Font(None, 24)
        self.text_surface = self.font.render(str(self.value), True, (255, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(x, y))

    def increment(self):
        self.value += 1
        self.update_text()

    def update_text(self):
        # Effacer la surface du texte précédent avec une couleur de fond
        self.text_surface.fill((0, 0, 0, 0))  # Remplir avec une couleur transparente

        # Redessiner le texte avec la nouvelle valeur
        self.text_surface = self.font.render(str(self.value), True, (255, 0, 0))

    def update(self, surface):
        # Afficher le texte du compteur de cookies sur la surface spécifiée
        surface.blit(self.text_surface, self.text_rect)
