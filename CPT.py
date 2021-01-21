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
BLACK            = (   0,   0,   0)
WHITE            = ( 255, 255, 255)
GREEN            = (   0, 255,   0)
RED              = ( 255,   0,   0) 
BUTTON_ONE_COL   = (  25, 190, 255) # Start
HOVER_ONE_COL    = (  75, 225, 225) # Start
BUTTON_TWO_COL   = ( 200,   0,   0) # Quit
HOVER_TWO_COL    = ( 255, 100, 100) # Quit
BUTTON_THREE_COL = ( 238, 149, 114) # RAM
HOVER_THREE_COL  = ( 205, 129,  98) # RAM
BUTTON_FOUR_COL  = (   0, 238,   0) # GPU
HOVER_FOUR_COL   = (   0, 205,   0) # GPU
BUTTON_FIVE_COL  = ( 238,  44,  44) # CPU
HOVER_FIVE_COL   = ( 205,  38,  38) # CPU
BUTTON_SIX_COL   = ( 151, 255, 255) # PSU
HOVER_SIX_COL    = ( 121, 205, 205) # PSU
BUTTON_SEVEN_COL = ( 255, 185,  15) # Storage
HOVER_SEVEN_COL  = ( 205, 149,  12) # Storage
BUTTON_EIGHT_COL = ( 255,  20, 147) # Motherboard
HOVER_EIGHT_COL  = ( 205,  16, 118) # Motherboard
BUTTON_NINE_COL  = ( 255, 187, 255) # Case
HOVER_NINE_COL   = ( 205, 150, 205) # Case
BUTTON_TEN_COL   = (   0,   0, 255) # Peripherals Button Switch
HOVER_TEN_COL    = (   0,   0, 205) # Peripherals Button Switch

# Initiate Pygame
pygame.init()

# Sets the width and height of the screen [width, height]
size = (1920, 1020)
screen = pygame.display.set_mode(size)

# Obtains the actions a user performs on screen
position = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

# Set graphics
background = pygame.image.load("background.jpg").convert()
computer = pygame.image.load("computer.png").convert_alpha()
top_text = pygame.image.load("top_text.png").convert_alpha()
top_text_two = pygame.image.load("top_text_two.png").convert_alpha()
info_board = pygame.image.load("info_board.png").convert()
mouse = pygame.image.load("mouse.png").convert_alpha()
keyboard = pygame.image.load("keyboard.png").convert_alpha()
monitor = pygame.image.load("monitor.png").convert_alpha()

# Poster images
computer_poster = pygame.image.load("computer_poster.png").convert()
cpu_poster = pygame.image.load("cpu_poster.png").convert()
gpu_poster = pygame.image.load("gpu_poster.png").convert()

# Set font
font_one = pygame.font.SysFont('Calibri', 40, True, False)
font_two = pygame.font.SysFont('Calibri', 30, True, False)
font_three = pygame.font.SysFont('Calibri', 25, True, False)

# Set text
start_text = font_one.render("Start", True, BLACK)
quit_text = font_one.render("Quit", True, BLACK)
ram_text = font_one.render("RAM", True, BLACK)
gpu_text = font_one.render("GPU", True, BLACK)
cpu_text = font_one.render("CPU", True, BLACK)
psu_text = font_one.render("PSU", True, BLACK)
storage_text = font_two.render("Storage", True, BLACK)
motherboard_text = font_three.render("Motherboard", True, BLACK)
case_text = font_one.render("Case", True, BLACK)
peripheral_text = font_two.render("Peripherals", True, BLACK)
component_text = font_three.render("Components", True, BLACK)
monitor_text = font_one.render("Monitor", True, BLACK)
keyboard_text = font_two.render("Keyboard", True, BLACK)
mouse_text = font_one.render("Mouse", True, BLACK)
computer_text = font_two.render("Computer", True, BLACK)

# Set position of graphics
background_position      = [   0,    0]
computer_position        = [ 250,  300]
top_text_position        = [ 300,  -30]
top_text_two_position    = [ 775,  120]
info_board_position      = [ 400,  300]
mouse_position           = [ 700,  700]
keyboard_position        = [ 490,  175]
monitor_position         = [  20,  350]

# Set position of posters
computer_poster_position = [1200,  150]
cpu_poster_position      = [1200,  150]
gpu_poster_posution      = [1200,  150]

# Displays the title for the application
pygame.display.set_caption("Stefan's CPT")
 
# Loop until the user clicks the close button.
done = False

# Sets the start function to false, changes after the button is pressed
start = False
peripheral = False

# Toggle poster
cpu = False
gpu = False

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
        if start == True: # Only occurs if on the Components page
            if 10 + 150 > position[0] > 10 and 20 + 50 > position[1] > 20: # If user is hovering over the "Peripheral" button
                if event.type == pygame.MOUSEBUTTONDOWN: # If user clicks the button
                    peripheral = not peripheral # Sets the peripheral page by making it True
                    start = not peripheral # Erases the Components page
        if peripheral == True: # Only occurs if on the Peripherals page
            if 10 + 150 > position[0] > 10 and 20 + 50 > position[1] > 20: # If user is hovering over the "Components" button
                if event.type == pygame.MOUSEBUTTONDOWN: # If user clicks the button
                    start = not start # I literally don't know what I did here, but it made it work
        # Poster Buttons
        if start == True:
            if 330 + 150 > position[0] > 330 and 220 + 50 > position[1] > 220:
                cpu = True
            else:
                cpu = False
            if 30 + 150 > position[0] > 30 and 577 + 50 > position[1] > 577:
                gpu = True
            else:
                gpu = False

    # Draw Main Page
    screen.blit(background, background_position)
    screen.blit(top_text, top_text_position)
    screen.blit(top_text_two, top_text_two_position)
    screen.blit(info_board, info_board_position)

    # Game logic 
    position = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Hover Function for Start Button in Menu
    if 500 + 200 > position[0] > 500 and 850 + 50 > position[1] > 850:
        pygame.draw.rect(screen, HOVER_ONE_COL,(500,850,200,50))
        screen.blit(start_text, [555, 857])
    else:
        pygame.draw.rect(screen, BUTTON_ONE_COL,(500,850,200,50))
        screen.blit(start_text, [555, 857])

    # Hover Function for Quit Button in Menu
    if 1100 + 200 > position[0] > 1100 and 850 + 50 > position[1] > 850:
        pygame.draw.rect(screen, HOVER_TWO_COL,(1100,850,200,50))
        screen.blit(quit_text, [1160, 857])
    else:
        pygame.draw.rect(screen, BUTTON_TWO_COL,(1100,850,200,50))
        screen.blit(quit_text, [1160, 857])

    # Start Game Function
    if start:
        screen.blit(background, background_position)
        screen.blit(top_text, top_text_position)
        screen.blit(top_text_two, top_text_two_position)
        screen.blit(computer, computer_position)
        screen.blit(computer_poster, computer_poster_position)

        # Drawing lines and boxes with hover colour changer

        # Ram Button
        if 525 + 150 > position[0] > 525 and 250 + 50 > position[1] > 250:
            pygame.draw.line(screen, HOVER_THREE_COL, [600, 300], [500, 460], 5)
            pygame.draw.rect(screen, HOVER_THREE_COL,(525,250,150,50))
            screen.blit(ram_text, [554, 256])
        else:
            pygame.draw.line(screen, BUTTON_THREE_COL, [600, 300], [500, 460], 5)
            pygame.draw.rect(screen, BUTTON_THREE_COL,(525,250,150,50))
            screen.blit(ram_text, [554, 256])
    
        # GPU Button
        if 30 + 150 > position[0] > 30 and 577 + 50 > position[1] > 577:
            pygame.draw.line(screen, HOVER_FOUR_COL, [170, 600], [340, 610], 5)
            pygame.draw.line(screen, HOVER_FOUR_COL, [170, 600], [340, 570], 5)
            pygame.draw.rect(screen, HOVER_FOUR_COL, (30,577,150,50))
            screen.blit(gpu_text, [65, 585])
        else:
            pygame.draw.line(screen, BUTTON_FOUR_COL, [170, 600], [340, 610], 5)
            pygame.draw.line(screen, BUTTON_FOUR_COL, [170, 600], [340, 570], 5)
            pygame.draw.rect(screen, BUTTON_FOUR_COL, (30,577,150,50))
            screen.blit(gpu_text, [65,585])

        # CPU Button
        if 330 + 150 > position[0] > 330 and 220 + 50 > position[1] > 220:
            pygame.draw.line(screen, HOVER_FIVE_COL, [400, 230], [430, 480], 5)
            pygame.draw.rect(screen, HOVER_FIVE_COL, (330,220,150,50))
            screen.blit(cpu_text, [365,225])
        else:
            pygame.draw.line(screen, BUTTON_FIVE_COL, [400, 230], [430, 480], 5)
            pygame.draw.rect(screen, BUTTON_FIVE_COL, (330,220,150,50))
            screen.blit(cpu_text, [365,225])

        # PSU Button
        if 330 + 150 > position[0] > 330 and 800 + 50 > position[1] > 800:
            pygame.draw.line(screen, HOVER_SIX_COL, [400, 800], [340, 690], 5)
            pygame.draw.rect(screen, HOVER_SIX_COL, (330,800,150,50))
            screen.blit(psu_text, [370,810])
        else:
            pygame.draw.line(screen, BUTTON_SIX_COL, [400, 800], [340, 690], 5)
            pygame.draw.rect(screen, BUTTON_SIX_COL, (330,800,150,50))
            screen.blit(psu_text, [370,810])

        # Storage Button
        if 800 + 150 > position[0] > 800 and 575 + 50 > position[1] > 575:
            pygame.draw.line(screen, HOVER_SEVEN_COL, [800, 600], [620, 670], 5)
            pygame.draw.rect(screen, HOVER_SEVEN_COL, (800,575,150,50))
            screen.blit(storage_text, [825,585])
        else:
            pygame.draw.line(screen, BUTTON_SEVEN_COL, [800, 600], [620, 670], 5)
            pygame.draw.rect(screen, BUTTON_SEVEN_COL, (800,575,150,50))
            screen.blit(storage_text, [825,585])

        # Motherboard Button
        if 20 + 150 > position[0] > 20 and 375 + 50 > position[1] > 375:
            pygame.draw.line(screen, HOVER_EIGHT_COL, [170, 400], [420, 540], 5)
            pygame.draw.rect(screen, HOVER_EIGHT_COL, (20,375,150,50))
            screen.blit(motherboard_text, [25,386])

        else:
            pygame.draw.line(screen, BUTTON_EIGHT_COL, [170, 400], [420, 540], 5)
            pygame.draw.rect(screen, BUTTON_EIGHT_COL, (20,375,150,50))
            screen.blit(motherboard_text, [25,386])

        # Case Button
        if 800 + 150 > position[0] > 800 and 375 + 50 > position[1] > 375:
            pygame.draw.line(screen, HOVER_NINE_COL, [800, 400], [620, 550], 5)
            pygame.draw.rect(screen, HOVER_NINE_COL, (800,375,150,50))
            screen.blit(case_text, [835,380])
        else:
            pygame.draw.line(screen, BUTTON_NINE_COL, [800, 400], [620, 550], 5)
            pygame.draw.rect(screen, BUTTON_NINE_COL, (800,375,150,50))
            screen.blit(case_text, [835,380])

        # Peripheral Button
        if 10 + 150 > position[0] > 10 and 20 + 50 > position[1] > 20:
            pygame.draw.rect(screen, HOVER_TEN_COL, (10,20,150,50))
            screen.blit(peripheral_text, [14,30])
        else:
            pygame.draw.rect(screen, BUTTON_TEN_COL, (10,20,150,50))
            screen.blit(peripheral_text, [14,30])


        # Toggle poster commands

        #CPU Poster
        if cpu == True:
            screen.blit(cpu_poster, cpu_poster_position)
        if gpu == True:
            screen.blit(gpu_poster, gpu_poster_posution)
        

    # Peripheral Game Function
    if peripheral:
        screen.blit(background, background_position)
        screen.blit(top_text, top_text_position)
        screen.blit(top_text_two, top_text_two_position) 
        screen.blit(mouse, mouse_position)
        screen.blit(keyboard, keyboard_position) 
        screen.blit(monitor, monitor_position)

        # Component Button
        if 10 + 150 > position[0] > 10 and 20 + 50 > position[1] > 20:
            pygame.draw.rect(screen, HOVER_SIX_COL, (10,20,150,50))
            screen.blit(component_text, [16,32])
        else:
            pygame.draw.rect(screen, BUTTON_SIX_COL, (10,20,150,50))
            screen.blit(component_text, [16,32])

        # Monitor Button
        if 250 + 150 > position[0] > 250 and 380 + 50 > position[1] > 380:
            pygame.draw.line(screen, HOVER_THREE_COL, [300, 400], [400, 500], 5)
            pygame.draw.rect(screen, HOVER_THREE_COL, (250,380,150,50))
            screen.blit(monitor_text, [253,387])
        else:
            pygame.draw.line(screen, BUTTON_THREE_COL, [300, 400], [400, 500], 5)
            pygame.draw.rect(screen, BUTTON_THREE_COL, (250,380,150,50))
            screen.blit(monitor_text, [253,387])

        # Keyboard Button
        if 780 + 150 > position[0] > 780 and 540 + 50 > position[1] > 540:
            pygame.draw.line(screen, HOVER_FOUR_COL, [730, 420], [860, 543], 5)
            pygame.draw.rect(screen, HOVER_FOUR_COL, (780,540,150,50))
            screen.blit(keyboard_text, [795,550])
        else:
            pygame.draw.line(screen, BUTTON_FOUR_COL, [730, 420], [860, 543], 5)
            pygame.draw.rect(screen, BUTTON_FOUR_COL, (780,540,150,50))
            screen.blit(keyboard_text, [795,550])

        # Mouse Button
        if 890 + 150 > position[0] > 890 and 650 + 50 > position[1] > 650:
            pygame.draw.line(screen, HOVER_FIVE_COL, [950, 735], [1000, 670], 5)
            pygame.draw.rect(screen, HOVER_FIVE_COL, (890,650,150,50))
            screen.blit(mouse_text, [907,657])
        else:
            pygame.draw.line(screen, BUTTON_FIVE_COL, [950, 735], [1000, 670], 5)
            pygame.draw.rect(screen, BUTTON_FIVE_COL, (890,650,150,50))
            screen.blit(mouse_text, [907,657])
    
        
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()