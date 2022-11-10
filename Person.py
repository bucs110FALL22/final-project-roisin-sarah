import pygame

class Person:

  pygame.init()
  screen = pygame.display.set_mode()
  screen.fill((255,255,255))
  color = (0,0,255)
  radius = 20

  xCoord = 30
  yCoord = 30

  pygame.draw.circle(screen, color, (xCoord,yCoord), radius)
  
  
  pygame.display.flip()
  pygame.time.wait(1000)
  screen.fill((255,255,255))
  pygame.display.flip()

  direction = ["UP", "DOWN", "LEFT", "RIGHT"]

  for i in direction:
      if i == "UP":
          yCoord = yCoord + 10
      elif i == "DOWN":
          yCoord = yCoord - 10
      elif i == "LEFT":
          xCoord = xCoord - 10
      elif i == "RIGHT":
          xCoord = xCoord + 10

      pygame.draw.circle(screen, color, (xCoord,yCoord), radius)

      pygame.display.flip()
      pygame.time.wait(500)
  
  for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          if (event.key == pygame.K_UP):
              yCoord = yCoord + 10
          elif (event.key == pygame.K_DOWN):
              yCoord = yCoord - 10
          elif (event.key == pygame.K_LEFT):
              xCoord = xCoord - 10
          elif (event.key == pygame.K_RIGHT):
              xCoord = xCoord + 10
          pygame.display.flip()
          pygame.time.wait(1000)
