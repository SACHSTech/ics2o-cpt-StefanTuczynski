""" 
A basic pygame template
"""
 
import pygame
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width, height]
size = (1920, 1020)
screen = pygame.display.set_mode(size)

# Set Graphics
background = pygame.image.load("background.jpg").convert()
computer = pygame.image.load("computer.png").convert_alpha()

# Set position of graphics
background_position = [0,0]
computer_position = [0,100]
pygame.display.set_caption("Stefan's CPT")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
  
    # --- Game logic should go here
 
    # --- Drawing code should go here
    screen.blit(background, background_position)
    pygame.draw.rect(screen, GREEN,(750,450,400,50))
    #screen.blit(computer, computer_position)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()