import pygame
import src.start

class Union: 
    
  def __init__(self):
#   #setup pygame data
    pygame.init()
    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size()
    self.background_image = ["assets/union.png"]
    self.background = pygame.image.load(self.background_image[0])
    self.background = pygame.transform.scale(self.background, size) 
    self.screen.blit(self.background, (0,0))

  def mainloop(self):
#     print("hey queen")
    self.screen.blit(self.background, (0,0))
    pygame.display.update()
    answerQuestion = True 
    while answerQuestion == True: 
    #  keys = pygame.key.get_pressed()
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a:
            print("you pressed a ")
            answerQuestion == False
          if event.key == pygame.K_b:
            print("you pressed b ")
            answerQuestion == False
          if event.key == pygame.K_c:
            print("you pressed c ")
            # start.mainloop()
            #self.points = self.points + 1 
            #go back to main screen
            answerQuestion == False
          if event.key == pygame.K_d:
            print("you pressed d ")
            answerQuestion == False

