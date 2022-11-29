import pygame
class Controller:
  
  def __init__(self):
  #setup pygame data
    pygame.init()
    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size() 
    self.background_image = ["assets/Map.jpeg" ]
    self.background = pygame.image.load(self.background_image[0])
    self.background = pygame.transform.scale(self.background, size)  
  def mainloop(self):
    #select state loop
    print("hi")
    self.screen.blit(self.background, (0,0))
    pygame.display.update()
  
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
