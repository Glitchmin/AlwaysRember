import pygame

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

pygame.init()
pygame.display.set_caption("AlwaysRember")

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True

ground_texture_file = open("textures/ground.png")
ground_texture = pygame.image.load(ground_texture_file)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    for i in range(SCREEN_HEIGHT // 16):
        for j in range(SCREEN_WIDTH // 16):
            screen.blit(
                ground_texture,
                (
                    ground_texture.get_width() * i,
                    ground_texture.get_height() * j,
                ),
            )

    pygame.display.flip()

pygame.quit()
