'''
Import relevant modules
'''
import pygame # module for visual, audio and keystroke elements
import random # module that enables random selection

'''
Initialise Pygame and load relevant images
'''
pygame.init() # initialise imported Pygame modules

SCREEN = pygame.display.set_mode((500, 700)) # set up screen for game to run
CLOCK = pygame.time.Clock() # initialise clock object for fps control

BACKGROUND_IMAGE = pygame.image.load("background.jpg") # load background image
BIRD_IMAGE = pygame.image.load("bird.jpg") # load bird image

OBSTACLE_COLOR = (211, 253, 117) # define obstacle colour

FONT = pygame.font.Font(None, 48) # load fonts

'''
Game set-up
'''
score = 0

GRAVITY = 0.1 # set a proportionality constant for gravity

bird_x = 50 # constant for bird x position
bird_y = 300 # variable for bird y position
bird_y_speed = 0 # variable for bird instantaneous y speed

obstacle_x = 500 # variable for obstacle x position

def display_bird(x, y): # function to draw bird based on given x, y coordinates
    SCREEN.blit(BIRD_IMAGE, (x, y)) # display bird image

passed = False # boolean to prevent double counting score

obstacle_height = random.randint(50, 285) # select random obstacle height

running = True # boolean to control game loop

'''
GAME LOOP
'''
while running:

    SCREEN.blit(BACKGROUND_IMAGE, (0, 0)) # display background image

    for event in pygame.event.get(): # get events
        if event.type == pygame.QUIT: # close game window
            running = False

        if event.type == pygame.KEYDOWN: # get keystroke
            if event.key == pygame.K_SPACE: # get space key stroke
                bird_y_speed = -5 # make bird move upwards

    bird_y_speed += GRAVITY
    bird_y += bird_y_speed
    if bird_y < 0:
        bird_y = 0
        bird_y_speed = 0
    if bird_y > 575:
        running = False
    
    display_bird(bird_x, bird_y)

    if obstacle_x >= -20 and obstacle_x <= 141 and (bird_y < obstacle_height or bird_y > obstacle_height + 236):
        running = False

    obstacle_x -= 1.5

    if obstacle_x <= -20 and not passed:
        passed = True
        score += 1
        print(score)
    if obstacle_x <= -70:
        passed = False
        obstacle_x = 500
        obstacle_height = random.randint(50, 285)
    else:
        pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, 70, obstacle_height))
        bottom_height = 635 - obstacle_height - 300
        pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 635 - bottom_height, 70, bottom_height))

    text = FONT.render(f"{score}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(250, 50))
    SCREEN.blit(text, text_rect)

    pygame.display.update()
    CLOCK.tick(120)

pygame.quit()