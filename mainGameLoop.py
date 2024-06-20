import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
running = True
# In the Middle of the Screen (always) maxHeight / 2 and maxWidth / 2
player_Position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
deltatime = 0

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
    for event in pygame.event.get():
        # When Player clicks X on windows the game loop will break 
        if event.type == pygame.QUIT:
            running = False
    # First thing todo in each frame ->> Clear old frame -> make new Frame so just fill with black
    # Before anything else gets drawn because otherwise tít will not be shown 
    screen.fill("black")

    # Draw Player onto screen / happens every frame
    pygame.draw.circle(screen, "blue", player_Position, radius=7)
    # Check for Movement
    PlayerMovementCheck()

    # Show what is happening on screen with flip 
    pygame.display.flip()
    # Set Max Fps to 60
    # Delta Time holds value of time from last frame
    deltatime = clock.tick(60) / 1000

# Quit when Loop breaks
pygame.quit()