import pygame
import src.whitney
import src.union
import json

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
        self.points = 0

    def scoreboard(self):

        font = pygame.font.SysFont(None, 45)
        pointsText = font.render('Points: ' + str(self.points), True, (0, 0, 255))
        self.screen.blit(pointsText, (20, 275))

    def mainloop(self):
        while True:
            self.gameloop()

    def gameloop(self):

        self.screen.blit(self.background, (0, 0))
        self.scoreboard()
        pygame.display.update()
        buttonGroup = {}

        with open('etc/building_data.json','r') as fptr:
          data = json.load(fptr)
        '''create anderson, sci library, union, library, and whitney hall buttons'''
        for button in data ['button']:
          buttonGroup[button['buttonName']] = pygame.Rect(button['x'],button['y'], button['w'],button['h'])
          pygame.draw.rect(self.screen, button['buttonColor'], buttonGroup[button['buttonName']])
          font = pygame.font.SysFont(None,button['fontSize'])
          button['buttonVariable'] = font.render(button['buttonLabel'], True, button['buttonTextColor'])
          self.screen.blit(button['buttonVariable'], (button['buttonTextX'], button['buttonTextY']))

        '''lecture hall button and text - different because it's a circle'''
        lecturehallButton = pygame.draw.circle(self.screen, (0, 0, 0), (500, 100), 50)
        pygame.display.update()
        lectureHallText = font.render('LH', True, (255, 255, 255))
        self.screen.blit(lectureHallText, (500, 125))

        pygame.display.update()

        selected = False
        while not selected:
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
                    if buttonGroup["andersonButton"].collidepoint(mousePos):
                        andersonpressed = True
                        done = True
                    # print(andersonpressed)
                    if lecturehallButton.collidepoint(mousePos):
                        lecturehallpressed = True
                        done = True
                    #  print(lecturehallpressed)
                    if buttonGroup["scilibraryButton"].collidepoint(mousePos):
                        scilibrarypressed = True
                        done = True
                    #   print(scilibrarypressed)
                    if buttonGroup["unionButton"].collidepoint(mousePos):
                        unionpressed = True
                        done = True
                    if buttonGroup["libraryButton"].collidepoint(mousePos):
                        librarypressed = True
                        done = True
                    #  print(unionpressed)
                    if buttonGroup["whitneyButton"].collidepoint(mousePos):
                        whitneypressed = True
                        done = True
                    #   print(whitneypressed)
            if andersonpressed == True:
                pygame.draw.rect(self.screen, (0, 255, 0), buttonGroup["andersonButton"])
                done = False
            if lecturehallpressed == True:
                pygame.draw.circle(self.screen, (0, 255, 0), (500, 100), 50)
                done = False
            if scilibrarypressed == True:
                pygame.draw.rect(self.screen, (0, 255, 0), buttonGroup["scilibraryButton"])
                done = False
            if unionpressed == True:
                pygame.draw.rect(self.screen, (0, 255, 0), buttonGroup["unionButton"])
                done = False
                union = src.union.Union()
                union.mainloop()
            if librarypressed == True:
                pygame.draw.rect(self.screen, (0, 255, 0), buttonGroup["libraryButton"])
            if whitneypressed == True:
                pygame.draw.rect(self.screen, (0, 255, 0), buttonGroup["whitneyButton"])
                done = False
                #print(self.points)
                whitney = src.whitney.Whitney()
                whitney.mainloop()
                #whitneyLoop(self)
                print(whitney.whitneyPoints)
                self.points += whitney.whitneyPoints
                selected = True

        # print(whitneyPoints)
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
