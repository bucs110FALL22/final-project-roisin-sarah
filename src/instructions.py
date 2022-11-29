import pygame 


class Instructions: 
    
  def __init__(self):
  #setup pygame data
    pygame.init()
    self.screen = pygame.display.set_mode()
    # size = pygame.display.get_window_size() 
    # self.background_image = ["assets/Map.jpeg" ]
    # self.background = pygame.image.load(self.background_image[0])
    # self.background = pygame.transform.scale(self.background, size) 
    # self.screen.blit(self.background, (0,0))

  def mainloop(self):

    self.screen.fill((255, 0, 0))
    font = pygame.font.SysFont(None, 24)
    text = font.render('Instructions for Trivia Map Game', True, (0,0,255))
    self.screen.blit(text, (20, 20))
    pygame.display.update()



    # instructionMenu()

      
   # def instructionMenu(self):
   #  instruction1 = self.drawFont("Player1  :  a / d --- move left / move right", 200, 50)
   #  instruction2 = self.drawFont( "Player1  :  f / g / h / j --- punch / kick / block / ultimate", 200, 100)
   #  instruction3 = self.drawFont("Player2  :  leftarrow / rightarrow --- move left / move right", 200, 150)
   #  instruction4 = self.drawFont("Player2  :  KP4 / KP5 / KP6 / KP7 --- punch / kick / block / ultimate", 200, 200)
   #  instruction5 = self.drawFont("Build up SP by fighting and hold down j or KP7 to fire laser!",200, 250)
     