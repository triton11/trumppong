import pygame
import tweepy
import random
#user:TrumpPong
#password:FUPgdpp100t

auth = tweepy.OAuthHandler("VOrDwufgnBfc9Pg7MU0NNJnhg", "U34un9TLQjiC0vSZT5ACkYIG8anlNibZSsEq5QCjZP4fsIk4SR")
auth.set_access_token("747244855550582784-NY7T1r6SfVQ8lEMtUPXfsr8IBtysolN","9h8fYzJEWMVnvpCAyJzLs8du17X7H170lAc1PdywnX3II")

api = tweepy.API(auth)

# -- Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
GREEN = (0, 255, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 100])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.score = 0

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Ball(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.hit = None
        self.change_x = 0
        self.change_y = 0

        self.trump = None


    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.hit, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

            self.change_x = -1*(self.change_x+random.randrange(-2, 3))
            self.change_y += random.randrange(-2, 3)

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.hit, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

            self.change_y = -1*(self.change_y+random.randrange(-2, 3))
            self.change_x += random.randrange(-2, 3)



class Trump(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
        self.string = ""
        x = random.randrange(0,3)
        if x == 0:
            self.string = "trump1.jpg"
        elif x == 1:
            self.string = "trump2.jpg"
        else:
            self.string = "trump3.png"
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.image.load(self.string).convert()


        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(10,500)
        self.rect.x = random.randrange(10,700)

        self.hit = None



# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('Test')

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
hit_list = pygame.sprite.Group()
trump_list = pygame.sprite.Group()

wall = Wall(0, 0, 800, 10)
wall_list.add(wall)
hit_list.add(wall)
all_sprite_list.add(wall)


wall = Wall(0, 590, 800, 10)
wall_list.add(wall)
hit_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(790, 0, 10, 270)
wall_list.add(wall)
hit_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(790, 330, 10, 270)
wall_list.add(wall)
hit_list.add(wall)
all_sprite_list.add(wall)

trumpeter = Trump()
trump_list.add(trumpeter)

# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list
hit_list.add(player)

ball = Ball(300,400,20,20)
ball.change_x = -6
ball.change_y = 6
ball.hit = hit_list
ball.trump = trump_list

all_sprite_list.add(player)
all_sprite_list.add(ball)
all_sprite_list.add(trumpeter)


clock = pygame.time.Clock()

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                player.changespeed(0, -8)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 8)

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                player.changespeed(0, 8)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -8)

    all_sprite_list.update()
    trump_hit_list = pygame.sprite.spritecollide(ball, ball.trump, True)
    for block in trump_hit_list:
        player.score += 1
        trumpeter = Trump()
        ball.trump.add(trumpeter)
        all_sprite_list.add(trumpeter)

    if ball.rect.x > 810:
        api.update_status("@realDonaldTrump " + input("what is your name?")+ " scored " + str(player.score) + " in Trump Pong.")
        done = True
    if ball.rect.x < 0:
        player.score = 0
        ball.rect.x = 400
        ball.rect.y = 300
        ball.change_x = -6
        ball.change_y = 6
    screen.fill(WHITE)
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render(str(player.score), True, BLACK)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [350, 50])

    all_sprite_list.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
