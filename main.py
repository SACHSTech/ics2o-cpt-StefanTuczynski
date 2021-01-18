""" 
-------------------------------------------------------------------------
Name:   main.py
Purpose: CPT based on an interactive information kiosk that allows the user to click on certain buttons in enable to read up on what the button is specifically designed to give information
about. This kiosk is based on a computer, and the buttons will give a better image and also 

Author: Tuczynski.S

Date:   01/11/2021
-------------------------------------------------------------------------
"""
 
import pygame
 
# Define some colors
BLACK      = (   0,   0,   0)
WHITE      = ( 255, 255, 255)
GREEN      = (   0, 255,   0)
RED        = ( 255,   0,   0)
BUTTON_COL = (  25, 190, 255)
HOVER_COL  = (  75, 225, 225)
pygame.init()

# Set the width and height of the screen [width, height]
size = (1920, 1020)
screen = pygame.display.set_mode(size)

position = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

# Set Graphics
background = pygame.image.load("background.jpg").convert()
computer = pygame.image.load("computer.png").convert_alpha()
top_text = pygame.image.load("top_text.png").convert_alpha()
top_text_two = pygame.image.load("top_text_two.png").convert_alpha()

# Set position of graphics
background_position   = [0     ,0]
computer_position     = [525, 220]
top_text_position     = [300, -30]
top_text_two_position = [775, 120]

# Display title for the application
pygame.display.set_caption("Stefan's CPT")
 
#Loop until the user clicks the close button.
done = False

#Toggle whether image is shown or not (used to cover 1st page)
show_background = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if show_background == False:
            if 500 + 200 > position[0] > 500 and 450 + 50 > position[1] > 450:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        show_background = not show_background

    # --- Drawing code should go here
    screen.blit(background, background_position)
    screen.blit(top_text, top_text_position)
    screen.blit(top_text_two, top_text_two_position)

    # --- Game logic should go here
    position = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 500 + 200 > position[0] > 500 and 450 + 50 > position[1] > 450:
        pygame.draw.rect(screen, HOVER_COL,(500,450,200,50))

    else:
        pygame.draw.rect(screen, BUTTON_COL,(500,450,200,50))

    if show_background:
        screen.blit(background, background_position)
        screen.blit(top_text, top_text_position)
        screen.blit(top_text_two, top_text_two_position)
        screen.blit(computer, computer_position)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()