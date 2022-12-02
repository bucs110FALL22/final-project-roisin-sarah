import pygame
import src.Start
import src.Instructions
import json

class Controller:

    def __init__(self):
        pygame.init()
        '''set up screen'''
        screenWidth = 800
        screenHeight = 500
        self.screen = pygame.display.set_mode([screenWidth, screenHeight])
        '''import background image and display'''
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
        self.screen.blit(pygame.transform.scale(self.image, (500, 500)), (140, -100))
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
        '''create loop to know if button was clicked'''
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
    '''creates a points tally and displays to screen'''
    def points(self):
        points = 0
        font = pygame.font.SysFont(None, 30)
        pointsText = font.render('Points: ' + points, True, (255, 0, 0))
        self.screen.blit(pointsText, (100, 400))
        print(points)

