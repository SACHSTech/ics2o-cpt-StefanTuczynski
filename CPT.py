""" 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Name:   CPT.py
Purpose: CPT based on an interactive information kiosk that allows the user to click on certain buttons in enable to read up on what the button is specifically designed to give information
about. This kiosk is based on a computer, and the buttons will give a better image and also some information on the part and its function in the computer. My CPT is focused on the topic of 
what we learned in unit 1 of "Understanding Computers" and covers the hardware components section.

Author: Tuczynski.S

Date:   01/27/2021
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
 
import pygame
 
# Defined colors
BLACK          = (   0,   0,   0)
WHITE          = ( 255, 255, 255)
GREEN          = (   0, 255,   0)
RED            = ( 255,   0,   0)
BUTTON_ONE_COL = (  25, 190, 255)
HOVER_ONE_COL  = (  75, 225, 225)
BUTTON_TWO_COL = ( 200,   0,   0)
HOVER_TWO_COL  = ( 255, 100, 100)

# Initiate Pygame
pygame.init()

# Sets the width and height of the screen [width, height]
size = (1920, 1020)
screen = pygame.display.set_mode(size)

# Obtains the actions a user performs on screen
position = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

# Set Graphics
background = pygame.image.load("background.jpg").convert()
computer = pygame.image.load("computer.png").convert_alpha()
top_text = pygame.image.load("top_text.png").convert_alpha()
top_text_two = pygame.image.load("top_text_two.png").convert_alpha()
info_board = pygame.image.load("info_board.png").convert()

# Set text
font = pygame.font.SysFont('Calibri', 40, True, False)
text_one = font.render("Start", True, BLACK)
text_two = font.render("Quit", True, BLACK)

# Set position of graphics
background_position   = [0      ,0]
computer_position     = [525,  220]
top_text_position     = [300,  -30]
top_text_two_position = [775,  120]
text_one_position     = [555,  857]
text_two_position     = [1160, 857]
info_board_position   = [400,  300]
# Displays the title for the application
pygame.display.set_caption("Stefan's CPT")
 
# Loop until the user clicks the close button.
done = False

# Sets the start function to false, changes after the button is pressed
start = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if start == False: # Only occurs if the button was not clicked
            if 500 + 200 > position[0] > 500 and 850 + 50 > position[1] > 850: # If user is hovering over the "Start" button
                if event.type == pygame.MOUSEBUTTONDOWN: # If user clicked the button
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        start = not start # Create background and text to cover old images
        if start == False: # Only occurs if the button was not clicked
            if 1100 + 200 > position[0] > 1100 and 850 + 50 > position[1] > 850: # If user is hovering over the "Quit" button
                if event.type == pygame.MOUSEBUTTONDOWN: # If user clicked the button
                    quit() #Quits the program

    # Drawing code
    screen.blit(background, background_position)
    screen.blit(top_text, top_text_position)
    screen.blit(top_text_two, top_text_two_position)
    screen.blit(info_board, info_board_position)

    # Game logic 
    position = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Logic for Start Button in Menu
    if 500 + 200 > position[0] > 500 and 850 + 50 > position[1] > 850:
        pygame.draw.rect(screen, HOVER_ONE_COL,(500,850,200,50))
        screen.blit(text_one, text_one_position)
    else:
        pygame.draw.rect(screen, BUTTON_ONE_COL,(500,850,200,50))
        screen.blit(text_one, text_one_position)

    # Logic for Quit Button in Menu
    if 1100 + 200 > position[0] > 1100 and 850 + 50 > position[1] > 850:
        pygame.draw.rect(screen, HOVER_TWO_COL,(1100,850,200,50))
        screen.blit(text_two, text_two_position)
    else:
        pygame.draw.rect(screen, BUTTON_TWO_COL,(1100,850,200,50))
        screen.blit(text_two, text_two_position)

    if start:
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