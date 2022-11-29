#import pygame
# #import your controller
# # from Schedule import Schedule 
# # from Map import Map
# # from Person import Person

# def main():
  
#     pygame.init()

        
#     #Create an instance on your controller object
#     #Call your mainloop
    
#     ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# # https://codefather.tech/blog/if-name-main-python/
# main()
# if __name__ == '__main__':
#     main()
    
#    def __init__(self):
# import pygame
# import src.Controller

# def main():
#   pygame.init()
#   controller = src.controller.Controller()
#   controller.mainloop()

# main()


import src.controller

def main():
    controller = src.controller.Controller()
    controller.mainloop()

main()