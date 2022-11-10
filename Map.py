
import pygame
pygame.init()
screen = pygame.display.set_mode()
screen.fill((255,255,255))
color = (0,255,0)
radius = 20
numberOfBuildings = 4
library = (50,10)
lecture = (300,10)
classroomWing = (50, 100)
scienceLibrary = (300,100)
coordinates = [library, lecture, classroomWing, scienceLibrary]
number_in_coords_list = 0

for _ in range(numberOfBuildings):
  pygame.draw.circle(screen, color, coordinates[number_in_coords_list], radius)
  number_in_coords_list = number_in_coords_list+1 
  pygame.display.flip()

pygame.display.flip()
pygame.time.wait(1000)
screen.fill((255,255,255))
pygame.display.flip()