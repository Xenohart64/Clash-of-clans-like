import pygame

# pygame setup
pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))

rows = columns = 10

cell_size = (width/columns, height/rows)

for row in range(rows):
    start_pos = (0, row * cell_size[1])
    end_pos = (width, row * cell_size[1])
    pygame.draw.line(screen, (255, 255, 255), start_pos, end_pos)

for col in range(columns):
    start_pos = (col * cell_size[0], 0)
    end_pos = (col * cell_size[0], height)
    pygame.draw.line(screen, (255, 255, 255), start_pos, end_pos)

running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # pygame.draw.line(screen, (255, 255, 255), (10, 20), (150, 200), 2)
        pygame.display.flip()

pygame.quit()