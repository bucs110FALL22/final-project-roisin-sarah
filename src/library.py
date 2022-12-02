import pygame

class Library:

    def __init__(self, tag=""):
        pygame.init()
        self.screen = pygame.display.set_mode()
        size = pygame.display.get_window_size()
        self.background_image1 = ["assets/library.png"]
        self.background1 = pygame.image.load(self.background_image1[0])
        self.background1 = pygame.transform.scale(self.background1, size)

    def mainloop(self):
        self.libraryPoints = 0
        answerQuestion = True
        while answerQuestion == True:
            self.screen.blit(self.background1, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        answerQuestion = False
                        self.libraryPoints = self.libraryPoints - 1
                    if event.key == pygame.K_b:
                        answerQuestion = False
                        self.libraryPoints = self.libraryPoints + 1
                    if event.key == pygame.K_c:
                        answerQuestion = False
                        self.libraryPoints = self.libraryPoints - 1
                    if event.key == pygame.K_d:
                        answerQuestion = False
                        self.libraryPoints = self.libraryPoints - 1
        return self.libraryPoints 