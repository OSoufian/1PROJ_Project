import sys
import pygame

# Initializing
pygame.init()

# Create the screen
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Initialize constants
font = pygame.font.SysFont("comicsansms", 30)
smallfont = pygame.font.SysFont("comicsansms", 14)
slategrey = (112, 128, 144)
lightgrey = (165, 175, 185)
blackish = (10, 10, 10)

# Function to create a button
def create_button(x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height), border_radius=3)
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height))


def game_menu():
    startText = font.render("Start", True, blackish)

    while True:
        screen.fill("black")

        # button (left, top, width, height)
        startButton = create_button((screen_width / 2) - 100, int(screen_height * .33), 200, 50, lightgrey, slategrey)

        if startButton:
            new_game()

        # Start button text
        screen.blit(startText, ((screen_width / 2) - (startText.get_width() / 2), int(screen_height * .33)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def new_game():
    newUserName = ""
    userName = ""

    nameActive = False

    submit = font.render("Submit !", True, blackish)

    while True:
        screen.fill((0, 0, 0))

        # Create the text box
        userNameSurface = font.render(newUserName, True, "white")

        # Create the border around the text box with .Rect
        # left, top, width, height
        userNameBorder = pygame.Rect(((screen_width - userNameSurface.get_width()) / 2), screen_height * .20,
                                     userNameSurface.get_width() + 10, 50)

        # This is the text surface when the user types in their name
        screen.blit(userNameSurface, ((screen_width - userNameSurface.get_width()) / 2 + 4 , screen_height * .20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if userNameBorder.collidepoint(event.pos):
                    nameActive = True
                else:
                    nameActive = False

            if event.type == pygame.KEYDOWN:
                if nameActive:
                    if event.key == pygame.K_BACKSPACE:
                        newUserName = newUserName[:-1]
                    else:
                        newUserName += event.unicode

        # Handles the click events by swtiching from white, slategrey, and black
        if nameActive:
            pygame.draw.rect(screen, "white", userNameBorder, 2, border_radius=10)
            userNamePrompt = font.render("Enter your first and last name here", True, "white")
        else:
            pygame.draw.rect(screen, slategrey, userNameBorder, 2, border_radius=10)
            userNamePrompt = font.render("Enter your first and last name here", True, slategrey)

        screen.blit(userNamePrompt, ((screen_width - userNamePrompt.get_width()) / 2,
                                     (screen_height * .20) + userNameSurface.get_height()))

        submitButtton = create_button((screen_width / 2) - (submit.get_width() / 2) - 5, screen_height * .9,
                                      submit.get_width() + 10, submit.get_height(), lightgrey, slategrey)

        screen.blit(submit, ((screen_width / 2) - (submit.get_width() / 2), int(screen_height * .9)))

        if submitButtton:
            if newUserName != "":
                userName = newUserName
            first_screen(userName)

        pygame.display.update()


def load_screen(userName):
    submit = font.render("Submit !", True, blackish)

    profileBorder = pygame.Rect(15, 60, 300, 100)

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        welcomeName = font.render(userName, True, slategrey)
        pygame.draw.rect(screen, "black", profileBorder, 2)

        screen.blit(welcomeName, (20, 60))

        submitButtton = create_button((screen_width / 2) - (submit.get_width() / 2) - 5, screen_height * .9,
                                      submit.get_width() + 10, submit.get_height(), lightgrey, slategrey)

        screen.blit(submit, ((screen_width / 2) - (submit.get_width() / 2), int(screen_height * .9)))

        if submitButtton:
            first_screen(userName)

        pygame.display.update()


def first_screen(userName):

    # Declare Variables
    welcomeName = font.render("Hello, " + userName + ".", True, slategrey)

    while True:
        screen.fill((0, 0, 0))
        screen.blit(welcomeName, (20, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


# Game loop
while True:
    game_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

