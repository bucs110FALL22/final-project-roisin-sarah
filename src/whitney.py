import pygame
import src.start
import json


class Whitney:

    def __init__(self, tag=""):
        #   #setup pygame data
        pygame.init()
        #load json
        #config = object.get(tag)
        self.screen = pygame.display.set_mode()
        size = pygame.display.get_window_size()
        self.background_image1 = ["assets/whitney.png"]
        self.background1 = pygame.image.load(self.background_image1[0])
        self.background1 = pygame.transform.scale(self.background1, size)

    # self.screen.blit(self.background1, (0,0))
 
    def mainloop(self):
        #     print("hey queen")
        start = src.start.Start()
        self.whitneyPoints = 0
        answerQuestion = True
        while answerQuestion == True:
            self.screen.blit(self.background1, (0, 0))
            pygame.display.update()
            #  keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print("you pressed a ")
                        answerQuestion = False
                    if event.key == pygame.K_b:
                        print("you pressed b ")
                        answerQuestion = False
                    if event.key == pygame.K_c:
                        print("you pressed c ")
                        answerQuestion = False
                    if event.key == pygame.K_d:
                        print("you pressed d ")
                        answerQuestion = False
                        #  print(int(start.points()))
                        # str(self.points)
                        #start.points(1)
                        self.whitneyPoints = self.whitneyPoints + 1

        return self.whitneyPoints 
       # start.mainloop()
