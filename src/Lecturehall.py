import pygame

class Lecturehall:

    def __init__(self, tag=""):
        pygame.init()
        '''set up the screen'''
        screenWidth = 800
        screenHeight = 500
        self.screen = pygame.display.set_mode([screenWidth, screenHeight])
        self.background_image1 = ["assets/lecturehall.png"]
        self.background1 = pygame.image.load(self.background_image1[0])
        self.background1 = pygame.transform.scale(self.background1, (screenWidth, screenHeight))

    def mainloop(self):
        self.lecturehallPoints = 0
        answerQuestion = True
        while answerQuestion == True:
            self.screen.blit(self.background1, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        answerQuestion = False
                        self.lecturehallPoints = self.lecturehallPoints - 1
                    if event.key == pygame.K_b:
                        answerQuestion = False
                        self.lecturehallPoints = self.lecturehallPoints - 1
                    if event.key == pygame.K_c:
                        answerQuestion = False
                        self.lecturehallPoints = self.lecturehallPoints - 1
                    if event.key == pygame.K_d:
                        answerQuestion = False
                        self.lecturehallPoints = self.lecturehallPoints + 1
        return self.lecturehallPoints 