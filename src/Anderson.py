import pygame

class Anderson:

    def __init__(self, tag=""):
        pygame.init()
        self.SCREEN = pygame.display.set_mode()
        size = pygame.display.get_window_size()
        self.background_image1 = ["assets/anderson.png"]
        self.background1 = pygame.image.load(self.background_image1[0])
        self.background1 = pygame.transform.scale(self.background1, size)

    def mainloop(self):
        self.andersonPoints = 0
        answerQuestion = True
        while answerQuestion == True:
            self.SCREEN.blit(self.background1, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        answerQuestion = False
                        self.andersonPoints = self.andersonPoints - 1
                    if event.key == pygame.K_b:
                        answerQuestion = False
                        self.andersonPoints = self.andersonPoints + 1
                    if event.key == pygame.K_c:
                        answerQuestion = False
                        self.andersonPoints = self.andersonPoints - 1
                    if event.key == pygame.K_d:
                        answerQuestion = False
                        self.andersonPoints = self.andersonPoints - 1
        return self.andersonPoints 