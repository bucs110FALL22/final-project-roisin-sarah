import pygame
import src.Start
import src.Instructions
import json

class Controller:

    def __init__(self):
        #setup pygame data
        screenWidth = 800
        screenHeight = 500
        pygame.init()
        '''import background image '''
        self.screen = pygame.display.set_mode([screenWidth, screenHeight])
        self.background_image = ["assets/Map.jpeg"]
        self.background = pygame.image.load(self.background_image[0])
        self.background = pygame.transform.scale(self.background, (screenWidth, screenHeight))
        self.screen.blit(self.background, (0, 0))

    def mainloop(self):
        #select state loop
        '''display background image and caption'''
        pygame.display.set_caption('Binghamton University Map Trivia Game!')
        self.screen.blit(self.background, (0, 0))
        self.beginningMenu()
      
    def beginningMenu(self):
        self.beginning = True
        self.gameOver = False
        buttonGroup = {}
        '''load and disply intro logo picture'''
        self.image = pygame.image.load("assets/introLogo.png")
        self.screen.blit(pygame.transform.scale(self.image, (500, 500)), (80, -100))
        '''load json file '''
      
        with open('etc/button_data.json','r') as fptr:
          data = json.load(fptr)
        '''create the start, instructions, and quit buttons'''
        for button in data ['button']:
          buttonGroup[button['buttonName']] = pygame.Rect(button['x'],button['y'], button['w'],button['h'])
          pygame.draw.rect(self.screen, button['buttonColor'], buttonGroup[button['buttonName']])
          font = pygame.font.SysFont(None,button['fontSize'])
          button['buttonVariable'] = font.render(button['buttonLabel'], True, button['buttonTextColor'])
          self.screen.blit(button['buttonVariable'], (button['buttonTextX'], button['buttonTextY']))

        '''update the screen'''
        pygame.display.update()
  
        while self.beginning == True:
            
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
                    if buttonGroup["startButton"].collidepoint(mousePos):
                        startPressed = True
                        done = True
                    if buttonGroup["instructionButton"].collidepoint(mousePos):
                        instructionsPressed = True
                        done = True
                    if buttonGroup["quitButton"].collidepoint(mousePos):
                        quitPressed = True
                        done = True

            if startPressed == True:
                pygame.draw.rect(self.screen, (255, 0, 0), buttonGroup["startButton"])
                pygame.display.flip()
                self.beginning = False
                start = src.Start.Start(self.screen)
                start.mainloop()

            if instructionsPressed == True:
                pygame.draw.rect(self.screen, (255, 0, 0), buttonGroup["instructionButton"])
                pygame.display.flip()
                self.beginning = False
                instructions = src.Instructions.Instructions()
                instructions.mainloop()

            if quitPressed == True:
                pygame.draw.rect(self.screen, (255, 0, 0), buttonGroup["quitButton"])
                pygame.display.flip()
                self.screen.fill((0, 0, 0))
                pygame.display.flip()
                pygame.quit()
                quit()

            #self.beginning = False
    def points(self):
        points = 0
        font = pygame.font.SysFont(None, 30)
        pointsText = font.render('Points: ' + points, True, (255, 0, 0))
        self.screen.blit(pointsText, (100, 200))
        print(points)

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
