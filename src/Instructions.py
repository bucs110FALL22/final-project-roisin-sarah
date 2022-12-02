import pygame 
import src.Controller

class Instructions: 
    
  def __init__(self):
  #setup pygame data
    pygame.init()
    self.screen = pygame.display.set_mode()
    
  def mainloop(self):
    controllor = src.Controller.Controller()

    self.screen.fill((255, 0, 0))
    font = pygame.font.SysFont(None, 24)
    text = font.render('Instructions for Trivia Map Game\press b to return', True, (0,0,255))
    self.screen.blit(text, (20, 20))
    text = font.render('1) Press "Start" and a map of Binghamton University will appear.', True, (0,0,255))
    self.screen.blit(text, (20, 120))
    text = font.render('2) Click on any building. A multiple choice question will appear, and enter your', True, (0,0,255))
    self.screen.blit(text, (20, 220))
    text = font.render(' answer (either "a", "b", "c" or "d") using your keyboard', True, (0,0,255))
    self.screen.blit(text, (20, 240))
    text = font.render('3) You will earn one point for a correct answer and lose one point for an incorrect', True, (0,0,255))
    self.screen.blit(text, (20, 320))
    text = font.render(' answer. Click on as many buildings as you want! ', True, (0,0,255))
    self.screen.blit(text, (20, 340))
    
    

    pygame.display.update()
    answerQuestion = True 
    while answerQuestion == True: 
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_b:
            answerQuestion = False
    controllor.mainloop()

