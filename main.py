import pygame
import sys

# Initialize Pygame
pygame.init()

# creation de la 
taille = (1080, 720)
window = pygame.display.set_mode(taille)
pygame.display.set_caption('Cookie')

# Create a font object
font_boutton = pygame.font.Font(None, 24)
font_cookie = pygame.font.Font(None, 24)

# Create a surface for the button
boutton_surface = pygame.Surface((150, 50))
nb_cookie_surface = pygame.Surface((150, 50))

# Ajouter du Text
text_boutton = font_boutton.render("Click Me", True, (0, 0, 0))
text_boutton_rect = text_boutton.get_rect(center=(boutton_surface.get_width()/2, boutton_surface.get_height()/2))

nb_cookie = 0

text_cookie = font_cookie.render(str(nb_cookie), True, (255, 0, 0))
text_cookie_rect = text_cookie.get_rect(center=(nb_cookie_surface.get_width()/2, nb_cookie_surface.get_height()/2))






# Create a pygame.Rect object that represents the button's boundaries
button_rect = pygame.Rect(125, 125, 150, 50)  # Adjust the position as needed

while True:
    # Couleur de fond
    window.fill((155, 255, 155))

    # Gestion des événements
    for event in pygame.event.get():
        # Quitter la fenêtre
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Si la souris est sur le bouton et clique
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                nb_cookie += 1
                # Mettre à jour le texte du nombre de cookies
                text_cookie = font_cookie.render(str(nb_cookie), True, (255, 0, 0))
                text_cookie_rect = text_cookie.get_rect(center=(nb_cookie_surface.get_width() / 2, nb_cookie_surface.get_height() / 2))

    # Effet hover sur le bouton
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(boutton_surface, (127, 255, 212), (1, 1, 148, 48))
    else:
        pygame.draw.rect(boutton_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(boutton_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(boutton_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(boutton_surface, (0, 100, 0), (1, 48, 148, 10), 2)

    # Afficher le texte du bouton
    boutton_surface.blit(text_boutton, text_boutton_rect)
    # Afficher le bouton
    window.blit(boutton_surface, (button_rect.x, button_rect.y))

    # Effacer la surface du nombre de cookies avec la couleur de fond
    nb_cookie_surface.fill((155, 255, 155))
    # Afficher le texte du nombre de cookies
    nb_cookie_surface.blit(text_cookie, text_cookie_rect)
    # Afficher la surface du nombre de cookies
    window.blit(nb_cookie_surface, (200, 200))

    # Mettre à jour l'écran
    pygame.display.update()
