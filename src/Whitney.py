import pygame

class Whitney:

    def __init__(self, tag=""):
        '''sets up the screen, and displays the image of the question with choices'''
        pygame.init()
        screenWidth = 800
        screenHeight = 500
        self.screen = pygame.display.set_mode([screenWidth, screenHeight])
        self.background_image1 = ["assets/whitney.png"]
        self.background1 = pygame.image.load(self.background_image1[0])
        self.background1 = pygame.transform.scale(self.background1, (screenWidth, screenHeight))

    def mainloop(self):
        '''Checks what key has been pressed. Adds a point for a correct answer to the question and subtracts a point for a wrong answer'''
        self.whitneyPoints = 0
        answerQuestion = True
        while answerQuestion == True:
            self.screen.blit(self.background1, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        answerQuestion = False
                        self.whitneyPoints = self.whitneyPoints - 1
                    if event.key == pygame.K_b:
                        answerQuestion = False
                        self.whitneyPoints = self.whitneyPoints - 1
                    if event.key == pygame.K_c:
                        answerQuestion = False
                        self.whitneyPoints = self.whitneyPoints - 1
                    if event.key == pygame.K_d:
                        answerQuestion = False
                        self.whitneyPoints = self.whitneyPoints + 1
        return self.whitneyPoints 