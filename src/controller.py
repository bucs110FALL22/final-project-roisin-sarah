import pygame

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

    self.beginningMenu()

  def mainloop(self):
    #select state loop
    '''display background image and caption'''
    pygame.display.set_caption('Binghamton University Map Trivia Game!')
    self.screen.blit(self.background, (0,0))
   # pygame.display.update()

  ### below are some sample loop states ###

      
  def beginningMenu(self):
    print("hi")
    self.beginning = True 
    self.gameOver = False
    while self.beginning == True:
      #self.screen.fill((0, 0, 0))
      print("here i am")
      self.image = pygame.image.load("assets/introLogo.png")
      #self.image = pygame.transform.scale(self.image, (screen_width/2,screen_height/2),self.screen) 
     # self.screen.blit(self.image, self.image.get_rect())
     # rect = self.move(300, 300)
      #screen.blit(self.image, rect)
      
      #pic = pygame.image.load("image.png")
      screen.blit(pygame.transform.scale(self.image, (500, 500)), (80, -100))
      pygame.display.flip()

      
      pygame.display.update()
      mousePos = pygame.mouse.get_pos()
      print(mousePos)
      #pygame.time.wait(1000)
      #startButton = 
      
      #pygame.display.set_caption(width, text, font)
      startButton = pygame.Rect(125, 200, 100, 50)
      pygame.draw.rect(self.screen, (0, 255, 0), startButton)
      instructionsButton = pygame.Rect(250, 200, 100, 50)
      pygame.draw.rect(self.screen, (0, 255, 0), instructionsButton)
      quitButton = pygame.Rect(375, 200, 100, 50)
      pygame.draw.rect(self.screen, (0, 255, 0), quitButton)
      pygame.display.update()

       # mousePos = pygame.mouse.get_pos()
      #  print(mousePos)
      #gameTitle = self.defButton("Logo.jpg", 700, 400)
     # print("here i am now")

      #self.screen.blit(gameTitle, (300, 300))

      # self.introImage = ["assets/introLogo.png" ]
      # pygame.image.load(self.introImage[0])
      # pygame.transform.scale(self.introImage, 30)
      #pygame.time.wait(1000)
      #done = False
      #pressed = False
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
      self.beginning = False
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
