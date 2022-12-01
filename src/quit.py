import pygame 
import src.controller

class Quit: 
    
  def __init__(self):
  #setup pygame data
    pygame.init()
    self.screen = pygame.display.set_mode()
    
  def mainloop(self):
    controllor = src.controller.Controller()

    self.screen.fill((0, 255, 0))
    font = pygame.font.SysFont(None, 24)
    text = font.render('Instructions for Trivia Map Game\press b to return', True, (0,0,255))
    self.screen.blit(text, (20, 20))
    pygame.display.update()
    answerQuestion = True 
    while answerQuestion == True: 
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_b:
            print("you pressed b ")
            answerQuestion = False
    controllor.mainloop()

