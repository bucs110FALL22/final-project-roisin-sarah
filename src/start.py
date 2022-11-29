import pygame 


class Start: 
    
  def __init__(self):
  #setup pygame data
    pygame.init()
    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size() 
    self.background_image = ["assets/Map.jpeg" ]
    self.background = pygame.image.load(self.background_image[0])
    self.background = pygame.transform.scale(self.background, size) 
    self.screen.blit(self.background, (0,0))

  def mainloop(self):
    print("hey queen")
    self.screen.blit(self.background, (0,0))
    pygame.display.update()