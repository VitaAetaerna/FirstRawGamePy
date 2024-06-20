# Full Source -> https://github.com/VitaAetaerna/FirstRawGamePy
# TODO: KEEP FULLY DOCUMENTED ._.




# Todo: Collisions for Player and Enemy
# Todo: Player CANNOT exit map, always comes back from opposite direction   | <- player going out left   |  <- coming back from right
# Todo: Powerups
# Todo: Enemy Kill Counter
# Todo: Make Player dash function
# Todo: Player Endurance maybe with UI 
# ? Round Counter
# ? Enemies can spawn in all Directions and maybe change direction they are going to 
# ? Player can shoot missiles infront 
# ? Make Player Rotate with Mouse for aiming while shooting
# In-Game Money for Upgrades / upgrade gets lost when player dies
# TODO: Optimization, dont  it get too big <- it depends on the technique anyways ;)


                # Design and Art
# Todo: Maybe make own art for this

#       X Let Enemy Randomly Spawn  X
#       XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#       X             |             X
#       X             v             X
#       X                           X
#       X                           X   Make Powerups appear when Enemies die and randomly drop /  Chances = Low for random but better powerup
#       X  - >      Player   <-     X   Let Enemy Randomly Spawn and on left side
#       X                           X 
#       X                           X
#       X             ^             X
#       X            |              X
#       X                           X
#       XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#       X Let Enemy Randomly Spawn  X

# get Necessary imports
import pygame
# Initialize Pygame engine
pygame.init()
# Set Screen size and make screen to draw on 
screen = pygame.display.set_mode((600, 600))
# Register a Clock for later FPS cap etc. etc.
clock = pygame.time.Clock()
# running = if main game loop is running or not // if true == game runs else it closes
running = True
# In the Middle of the Screen (always) maxHeight / 2 and maxWidth / 2
player_Position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# Delta Time so all of the variables are equal on each PC, doesnt matter how fast, always the same 
# If a PC is faster deltaTime would be higher so values are multiplied by a fix deltaTime
# to remain equallitxy on evey System
deltatime = 0

def overwrite_Last_Frame():
    screen.fill("black")

def draw_Player():
    # Draw Player onto screen / happens every frame
    # args(where to draw, color, position, radius of circle)
    pygame.draw.circle(screen, "blue", player_Position, radius=7)

def PlayerMovementCheck():
    # Get Inputs
    keys = pygame.key.get_pressed()
    # Walk Forward with Button W
    if keys[pygame.K_w]:
        # Update Player Position
        player_Position.y -= 300 * deltatime

    # Walk Backwards with Button S
    if keys[pygame.K_s]:
        # Update Player Position
        player_Position.y += 300 * deltatime

    # Walk To the left with Button A
    if keys[pygame.K_a]:
        # Update Player Position
        player_Position.x -= 300 * deltatime

    # Walk Forward with Button D
    if keys[pygame.K_d]:
        # Update Player Position
        player_Position.x += 300 * deltatime

# Main Game Loop
while running:
    # Event Handling
    for event in pygame.event.get():
        # When Player clicks X on windows the game loop will break 
        if event.type == pygame.QUIT:
            running = False
    # First thing todo in each frame ->> Clear old frame -> make new Frame so just fill with black
    # Before anything else gets drawn because otherwise it will not be shown 
    overwrite_Last_Frame()
    draw_Player()
    # Check for Player Movement
    PlayerMovementCheck()







    # Show what is happening on screen with flip 
    pygame.display.flip()
    # Set Max Fps to 60
    # Delta Time holds value of time from last frame
    deltatime = clock.tick(60) / 1000

# Quit when Loop breaks
pygame.quit()