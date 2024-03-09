import pygame
import sys
from robot import Circle

pygame.init()

WIDTH, HEIGHT = 600, 600
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

RADIUS = 20
SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brownian Motion")

clock = pygame.time.Clock()

circle = Circle((WIDTH, HEIGHT), WIDTH // 2, HEIGHT // 2, RADIUS, SPEED)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (0, 0, WIDTH, HEIGHT), 2)

    # Move the circle
    circle.move()

    # Get the circle and line positions
    circle_center_position, line_ending_postion = circle.draw()

    pygame.draw.circle(screen, RED, (circle_center_position[0], circle_center_position[1]), RADIUS)
    pygame.draw.line(screen, BLACK, (circle_center_position[0], circle_center_position[1]), (line_ending_postion[0], line_ending_postion[1]), 10)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
