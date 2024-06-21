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

# !     X Let Enemy Randomly Spawn  X
#       XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#       X             |             X
#       X             v             X
#       X                           X
# !     X                           X   Make Powerups appear when Enemies die and randomly drop /  Chances = Low for random but better powerup
# !     X  - >      Player   <-     X   Let Enemy Randomly Spawn and on left side
#       X                           X 
#       X                           X
#       X             ^             X
#       X            |              X
#       X                           X
#       XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# !     X Let Enemy Randomly Spawn  X

# ! get Necessary imports
import pygame
# Initialize Pygame engine
pygame.init()
# Set Screen size and make screen to draw on 
screen = pygame.display.set_mode((600, 600))
# Register a Clock for later FPS cap etc. etc.
clock = pygame.time.Clock()
# running = if main game loop is running or not // if true == game runs else it closes
running = True
# Delta Time so all of the variables are equal on each PC, doesnt matter how fast, always the same 
# If a PC is faster deltaTime would be higher so values are multiplied by a fix deltaTime
# to remain equality on every System
deltatime = 0

# Event Definitions



# Overwrite last Frame so it isnt showing the last frame with the current frame mixed
def overwrite_Last_Frame():
    screen.fill("black")

class Player(object):

    # Constructor
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.player_position = (self.x, self.y)

    # Drawing the Player on the Screen
    # Instantiating a new class is needed to access this method
    def draw_Player(self, screen):
        pygame.draw.circle(screen, center=[int(self.x), int(self.y)], radius=self.radius, color=self.color) 
    

    # Keybind checking // Moving Player // Redrawing Position // 
    # Instantiating a new class is needed to access this method
    def player_input(self):
        # Get Inputs
        keys = pygame.key.get_pressed()
        # Walk Forward with Button W
        if keys[pygame.K_w]:
            # Update Player Position
            self.y -= 300 * deltatime

        # Walk Backwards with Button S
        if keys[pygame.K_s]:
            # Update Player Position
            self.y += 300 * deltatime

        # Walk To the left with Button A
        if keys[pygame.K_a]:
            # Update Player Position
            self.x -= 300 * deltatime

        # Walk Forward with Button D
        if keys[pygame.K_d]:
            # Update Player Position
            self.x += 300 * deltatime


# Instantiating new Instance of Classes
player = Player(x=200, y=200, radius=10, color="blue")
# Add Spawned Bullets and then pop them to make them despawn

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
    # Check for Player Movement
    player.draw_Player(screen)
    player.player_input()

    # Show what is happening on screen with flip 
    pygame.display.flip()
    # Set Max Fps to 60
    # Delta Time holds value of time from last frame
    deltatime = clock.tick(60) / 1000

# Quit when Loop breaks
pygame.quit()