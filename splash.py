# importing required library
import pygame
import time
import keyboard
 
# activate the pygame library .
pygame.init()
 
# create the display surface object
# of specific dimension..e(X, Y).
screen = pygame.display.set_mode()
 
# set the pygame window name
pygame.display.set_caption('Splash Image')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("logo.jpg").convert()
imp = pygame.transform.scale(imp, (screen.get_size()))
 
# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))
 
# paint screen one time
pygame.display.flip()

# stays open for 5 seconds
slp_segs = 50 # Number of segments
slp_len = 5 # 5 seconds
for i in range(slp_segs):
    time.sleep(slp_len/slp_segs)

    # allows the splash screen to be closed by pressing the escape key
    if keyboard.is_pressed('escape'):
        break



# deactivates the pygame library
pygame.quit()
