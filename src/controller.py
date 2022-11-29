import pygame
import src.start
import src.instructions
import sys


screen_width=800
screen_height=500
screen=pygame.display.set_mode([screen_width, screen_height])

class Controller:
  
  def __init__(self):
  #setup pygame data
    pygame.init()
    '''import background image '''
    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size() 
    self.background_image = ["assets/Map.jpeg" ]
    self.background = pygame.image.load(self.background_image[0])
    self.background = pygame.transform.scale(self.background, size) 
    self.screen.blit(self.background, (0,0))


  def mainloop(self):
    #select state loop
    '''display background image and caption'''
    pygame.display.set_caption('Binghamton University Map Trivia Game!')
    self.screen.blit(self.background, (0,0))
   # pygame.display.update()
    self.beginningMenu()

  ### below are some sample loop states ###

      
  def beginningMenu(self):
    print("hi")
    self.beginning = True 
    self.gameOver = False
    while self.beginning == True:


      self.image = pygame.image.load("assets/introLogo.png")
      screen.blit(pygame.transform.scale(self.image, (500, 500)), (80, -100))
      pygame.display.flip()
      
      startButton = pygame.Rect(125, 200, 100, 50)
      pygame.draw.rect(self.screen, (0, 255, 0), startButton)
      def text_type(text, font):
        textSurface = font.render(text, True, (0,0,0))
        return textSurface, textSurface.get_rect()

      def button_name(text):
        largeText = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_type(text, largeText)
        textRect.center = ((175),(230))
        screen.blit(textSurf, textRect)
      def button():
        button_name('START')
      button()
      instructionsButton = pygame.Rect(250, 200, 100, 50)
      pygame.draw.rect(self.screen, (0, 255, 0), instructionsButton)
      # def text_type(text, font):
      #   textSurface = font.render(text, True, (0,0,0))
      #   return textSurface, textSurface.get_rect()

      def button_name(text):
        largeText = pygame.font.Font('freesansbold.ttf',12)
        textSurf, textRect = text_type(text, largeText)
        textRect.center = ((300),(230))
        screen.blit(textSurf, textRect)
      def button():
        button_name('INSTRUCTIONS')
      button()
      quitButton = pygame.Rect(375, 200, 100, 50)
      pygame.draw.rect(self.screen, (0, 255, 0), quitButton)
      # def text_type(text, font):
      #   textSurface = font.render(text, True, (0,0,0))
      #   return textSurface, textSurface.get_rect()

      def button_name(text):
        largeText = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_type(text, largeText)
        textRect.center = ((425),(230))
        screen.blit(textSurf, textRect)
      def button():
        button_name('QUIT')
      button()
      pygame.display.update()
      
      
      done = False
      startPressed = False
      instructionsPressed = False
      quitPressed = False
      mousePos = pygame.mouse.get_pos()
      while done == False:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            done = True
          if event.type == pygame.MOUSEBUTTONUP:
           mousePos = pygame.mouse.get_pos()
          if startButton.collidepoint(mousePos):
              startPressed = True
              done = True
          if instructionsButton.collidepoint(mousePos):
            instructionsPressed = True
            done = True
          if quitButton.collidepoint(mousePos):
            quitPressed = True
            done = True
        
      if startPressed == True:
        pygame.draw.rect(self.screen, (255, 0, 0), startButton)
        pygame.display.flip()
        self.beginning = False
        start = src.start.Start()
        start.mainloop()

      if instructionsPressed == True:
        pygame.draw.rect(self.screen, (255, 0, 0), instructionsButton)
        pygame.display.flip()
        self.beginning = False
        instructions = src.instructions.Instructions()
        instructions.mainloop()
        
      if quitPressed == True:
        pygame.draw.rect(self.screen, (255, 0, 0), quitButton)
        pygame.display.flip()
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.quit()
        quit()

           
      #self.beginning = False
 # def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
 # def gameloop(self):
      #event loop

      #update data

      #redraw
    
 # def gameoverloop(self):
      #event loop

      #update data

      #redraw


# class Controller:

#     def __init__(self):
#         #setup pygame data
#         pygame.init()
#         pygame.font.init()
#         '''import background image '''
#         self.screen = pygame.display.set_mode()
#         size = pygame.display.get_window_size()
#         self.background_image = ["assets/Map.jpeg"]
#         self.background = pygame.image.load(self.background_image[0])
#         self.background = pygame.transform.scale(self.background, size)

#     def mainloop(self):
#         #select state loop
#         print("hi")
#         pygame.display.set_caption('B')
#         self.screen.blit(self.background, (0, 0))
#         pygame.display.update()

#         # mousePosition = pygame.mouse.get_pos()
#         #print(mousePosition)
#         done = False
#         pressed = False
#         mousePos = pygame.mouse.get_pos()
#         lecturehallButton = pygame.Rect(350, 300, 100, 50)
#         pygame.draw.rect(self.screen, (0, 0, 0), lecturehallButton)
#         pygame.display.update()
#         while done == False:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     done = True
#                 if event.type == pygame.MOUSEBUTTONUP:
#                     mousePos = pygame.mouse.get_pos()
#                     if lecturehallButton.collidepoint(mousePos):
#                         pressed = True
#                         done = True
#         if pressed == True:
#             pygame.draw.rect(self.screen, (0, 255, 0), lecturehallButton)
#             self.menu.add.label("Science Library", max_char=-1, font_size=14)
#         pygame.display.update()
