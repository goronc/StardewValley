import pygame
from game import Game

pygame.init()

# generer la fenetre du jeu

pygame.display.set_caption("Mon premier jeu")

screen = pygame.display.set_mode((1080,720))

bg = pygame.image.load("assets/bg.jpg")

game = Game()

running = True
while running:

    screen.blit(bg, (0,-200))

    screen.blit(game.player.image, game.player.rect)

    pygame.display.flip()

    print(game.player.rect.x , game.player.rect.y)

    #mouvement du joueur
    if game.pressed.get(pygame.K_z) and game.player.rect.y > 0:
        game.player.moove_up()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.moove_left()
    elif game.pressed.get(pygame.K_s) and game.player.rect.y + game.player.rect.height < 720:
        game.player.moove_down()
    elif game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < 1080:
        game.player.moove_right()

    #detection des evenemets
    for event in pygame.event.get():
        #femeture de fentre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
            print(" la fenetre a été fermé")
        #detecter input de touches
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


