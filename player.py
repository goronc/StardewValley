import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.defense = 10
        self.velocity = 1
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect() #rectangle de limage ou hitbox
        self.rect.x = 900
        self.rect.y = 700

    def moove_right(self):
        self.rect.x += self.velocity

    def moove_left(self):
        self.rect.x -= self.velocity
    
    def moove_up(self):
        self.rect.y -= self.velocity

    def moove_down(self):
        self.rect.y += self.velocity