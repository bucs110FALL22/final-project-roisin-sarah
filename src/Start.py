import pygame
import json
import src.Whitney
import src.Union
import src.Lecturehall
import src.Anderson 
import src.Scilibrary
import src.Library

class Start:

    def __init__(self, screen):
        #setup pygame data
        pygame.init()
        pygame.font.init()
        screenWidth = 800
        screenHeight = 500
        '''import background image '''
        self.screen = screen
        self.background_image = ["assets/Map.jpeg"]
        self.background = pygame.image.load(self.background_image[0])
        self.background = pygame.transform.scale(self.background, (screenWidth, screenHeight))
        self.points = 0

    def scoreboard(self):

        font = pygame.font.SysFont(None, 45)
        pointsText = font.render('Points: ' + str(self.points), True,
                                 (0, 0, 255))
        self.screen.blit(pointsText, (20, 275))

    def mainloop(self):
        while True:
            self.gameloop()

    def gameloop(self):

        self.screen.blit(self.background, (0, 0))
        self.scoreboard()
        pygame.display.update()
        buttonGroup = {}

        with open('etc/building_data.json', 'r') as fptr:
            data = json.load(fptr)
        '''create anderson, sci library, union, library, and whitney hall buttons'''
        for button in data['button']:
            buttonGroup[button['buttonName']] = pygame.Rect(
                button['x'], button['y'], button['w'], button['h'])
            pygame.draw.rect(self.screen, button['buttonColor'],
                             buttonGroup[button['buttonName']])
            font = pygame.font.SysFont(None, button['fontSize'])
            button['buttonVariable'] = font.render(button['buttonLabel'], True,
                                                   button['buttonTextColor'])
            self.screen.blit(button['buttonVariable'],
                             (button['buttonTextX'], button['buttonTextY']))
        '''lecture hall button and text - different because it's a circle'''
        lecturehallButton = pygame.draw.circle(self.screen, (0, 0, 0), (500, 100), 50)
        pygame.display.update()
        lectureHallText = font.render('LH', True, (255, 255, 255))
        self.screen.blit(lectureHallText, (500, 125))

        pygame.display.update()

        selected = False
        while not selected:
            done = False
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
                    if buttonGroup["andersonButton"].collidepoint(mousePos):
                        andersonpressed = True
                        done = True
                    if lecturehallButton.collidepoint(mousePos):
                        lecturehallpressed = True
                        done = True
                    if buttonGroup["scilibraryButton"].collidepoint(mousePos):
                        scilibrarypressed = True
                        done = True
                    if buttonGroup["unionButton"].collidepoint(mousePos):
                        unionpressed = True
                        done = True
                    if buttonGroup["libraryButton"].collidepoint(mousePos):
                        librarypressed = True
                        done = True
                    if buttonGroup["whitneyButton"].collidepoint(mousePos):
                        whitneypressed = True
                        done = True
            if andersonpressed == True:
                pygame.draw.rect(self.screen, (0, 255, 0),
                                 buttonGroup["andersonButton"])
                done = False
                anderson = src.Anderson.Anderson(self.screen)
                anderson.mainloop()
                self.points += anderson.andersonPoints
                selected = True
            if lecturehallpressed == True:
                pygame.draw.circle(self.screen, (0, 255, 0), (500, 100), 50)
                done = False
                lecturehall = src.Lecturehall.Lecturehall(self.screen)
                lecturehall.mainloop()
                self.points += lecturehall.lecturehallPoints
                selected = True
            if scilibrarypressed == True:
                pygame.draw.rect(self.screen, (0, 255, 0), buttonGroup["scilibraryButton"])
                done = False
                scilibrary = src.Scilibrary.Scilibrary()
                scilibrary.mainloop()
                self.points += scilibrary.scilibraryPoints
                selected = True
            if unionpressed == True:
                pygame.draw.rect(self.screen, (0, 255, 0), buttonGroup["unionButton"])
                done = False
                union = src.Union.Union(self.screen)
                union.mainloop()
                self.points += union.unionPoints
                selected = True
            if librarypressed == True:
                pygame.draw.rect(self.screen, (0, 255, 0), buttonGroup["libraryButton"])
                library = src.Library.Library(self.screen)
                library.mainloop()
                self.points += library.libraryPoints
                selected = True
            if whitneypressed == True:
                pygame.draw.rect(self.screen, (0, 255, 0), buttonGroup["whitneyButton"])
                done = False
                whitney = src.Whitney.Whitney(self.screen)
                whitney.mainloop()
                self.points += whitney.whitneyPoints
                selected = True

            pygame.display.update()


#        pygame.time.wait(100000)

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
