import pygame

# pygame setup
pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))

rows = columns = 10

cell_size = (width/columns, height/rows)

# pygame.draw.rect(screen,(255, 255, 255), pygame.Rect(128,0,128,128), 1)

for col in range(columns):
    start_pos = (col * cell_size[0], 0)
    end_pos = (width/columns * col, 72)
    rect = pygame.Rect(start_pos,end_pos)
    pygame.draw.rect(screen, (255, 255, 255), rect, 1)

running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # pygame.draw.line(screen, (255, 255, 255), (10, 20), (150, 200), 2)
        pygame.display.flip()

pygame.quit()