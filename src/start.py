# import pygame 


# class Start: 
    
#   def __init__(self):
#   #setup pygame data
#     pygame.init()
#     self.screen = pygame.display.set_mode()
#     size = pygame.display.get_window_size() 
#     self.background_image = ["assets/Map.jpeg" ]
#     self.background = pygame.image.load(self.background_image[0])
#     self.background = pygame.transform.scale(self.background, size) 
#     self.screen.blit(self.background, (0,0))

#   def mainloop(self):
#     print("hey queen")
#     self.screen.blit(self.background, (0,0))
#     pygame.display.update()


import pygame
import src.whitney 
import src.union

screen_width = 800
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])


class Start:

    def __init__(self):
        #setup pygame data
        pygame.init()
        pygame.font.init()
        '''import background image '''
        self.screen = pygame.display.set_mode()
        size = pygame.display.get_window_size()
        self.background_image = ["assets/Map.jpeg"]
        self.background = pygame.image.load(self.background_image[0])
        self.background = pygame.transform.scale(self.background, size)


        #print(self.points)
   # def whitneyLoop(self):
    #  print("now in whitney")
      
    def mainloop(self):
        #select state loop
        print("hi")
        pygame.display.set_caption('B')
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()
        #self.points(2)
      
        '''anderson center button and text'''
        andersonButton = pygame.Rect(310, 300, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), andersonButton)
        pygame.display.update()
        font = pygame.font.SysFont(None, 25)
        andersonCenterText = font.render('AC', True, (255, 255, 255))
        self.screen.blit(andersonCenterText, (360, 325))
        '''lecture hall button and text'''
        lecturehallButton = pygame.draw.circle(self.screen, (0, 0, 0),
                                               (500, 100), 50)
        #WHERE DO WE DRAW THE LECTURE HALL
        pygame.display.update()
        lectureHallText = font.render('LH', True, (255, 255, 255))
        self.screen.blit(lectureHallText, (500, 125))
        '''science library button and text'''
        scilibraryButton = pygame.Rect(485, 290, 50, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), scilibraryButton)
        scienceLibraryText = font.render('SL', True, (255, 255, 255))
        self.screen.blit(scienceLibraryText, (510, 315))
        pygame.display.update()
        '''union button and text'''
        unionButton = pygame.Rect(210, 100, 60, 100)
        pygame.draw.rect(self.screen, (0, 0, 0), unionButton)
        pygame.display.update()
        unionText = font.render('UU', True, (255, 255, 255))
        self.screen.blit(unionText, (240, 150))
        '''library button and text'''
        libraryButton = pygame.Rect(350, 90, 60, 90)
        pygame.draw.rect(self.screen, (0, 0, 0), libraryButton)
        pygame.display.update()
        unionText = font.render('LIB', True, (255, 255, 255))
        self.screen.blit(unionText, (380, 130))
        '''whitney button and text'''

        whitneyButton = pygame.Rect(70, 200, 40, 40)
        pygame.draw.rect(self.screen, (0, 0, 0), whitneyButton)
        whitneyText = font.render('WH', True, (255,255,255))
        self.screen.blit(whitneyText, (75, 205))
        pygame.display.update()

        self.points(0)
        pygame.display.update()

       # pygame.display.update()

        # mousePosition = pygame.mouse.get_pos()
        #print(mousePosition)

        #lecturehallButton = pygame.Rect(350, 300, 100, 50)
        #pygame.draw.rect(self.screen, (0, 0, 0), lecturehallButton)
        #words = 20000
        for i in range(200000):
          done = False
          #pressed = False
          andersonpressed = False
          lecturehallpressed = False
          scilibrarypressed = False
          unionpressed = False
          librarypressed = False
          whitneypressed = False
          mousePos = pygame.mouse.get_pos()
          while done == False:
              for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                      done = True
                  if event.type == pygame.MOUSEBUTTONUP:
                      mousePos = pygame.mouse.get_pos()
                  if andersonButton.collidepoint(mousePos):
                      andersonpressed = True
                      done = True
                  # print(andersonpressed)
                  if lecturehallButton.collidepoint(mousePos):
                      lecturehallpressed = True
                      done = True
                  #  print(lecturehallpressed)
                  if scilibraryButton.collidepoint(mousePos):
                      scilibrarypressed = True
                      done = True
                  #   print(scilibrarypressed)
                  if unionButton.collidepoint(mousePos):
                      unionpressed = True
                      done = True
                  if libraryButton.collidepoint(mousePos):
                      librarypressed = True
                      done = True
                  #  print(unionpressed)
                  if whitneyButton.collidepoint(mousePos):
                      whitneypressed = True
                      done = True
                  #   print(whitneypressed)
          if andersonpressed == True:
              pygame.draw.rect(self.screen, (0, 255, 0), andersonButton)
              done = False
          if lecturehallpressed == True:
              pygame.draw.circle(self.screen, (0, 255, 0), (500, 100), 50)
              done = False
          if scilibrarypressed == True:
              pygame.draw.rect(self.screen, (0, 255, 0), scilibraryButton)
              done = False
          if unionpressed == True:
              pygame.draw.rect(self.screen, (0, 255, 0), unionButton)
              done = False
              union = src.union.Union()
              union.mainloop()
          if librarypressed == True:
              pygame.draw.rect(self.screen, (0,255,0), libraryButton)
          if whitneypressed == True:
              pygame.draw.rect(self.screen, (0, 255, 0), whitneyButton)
              done = False
              print(self.points)
              whitney = src.whitney.Whitney()
              whitney.mainloop()
              #whitneyLoop(self)

          
          pygame.display.update()
        pygame.time.wait(100000)

    ### below are some sample loop states ###


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




    def points(self,x):
        self.x = 0 
        self.points = 0 +self.x
        font = pygame.font.SysFont(None, 45)
        pointsText = font.render('Points: '+str(self.points), True, (0, 0, 255))
        self.screen.blit(pointsText, (20, 275))
      