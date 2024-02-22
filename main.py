from splash import splashScreen
from gui import InputBox, InputLine, Button
import pygame
import sys

# pygame setup
pygame.init()
desktop = pygame.display.Info()
screen = pygame.display.set_mode((desktop.current_w-10, desktop.current_h-50))
clock = pygame.time.Clock()

#Screen coordinates
X = int(screen.get_width())
Y = int(screen.get_height())

# Initializing Color
red = (128, 23, 23)
green = (17, 122, 13)

#title setup
def title():
    font = pygame.font.Font('freesansbold.ttf', 32)
    title = font.render('Edit Current Game', True, ("white"), ("black"))
    textRect = title.get_rect()
    textRect.center = (X // 2, textRect.bottom)
    return screen.blit(title, textRect)

def textBox(input, bg, textColor, x, y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(input, True, (textColor), (bg))
    textRect = text.get_rect()
    textRect.center = (x, y)
    return screen.blit(text, textRect)

#Event function
def events(input_boxes, idCheck):
    # Check for events
    for event in pygame.event.get():
        for i, box in enumerate(input_boxes):
            box.handle_event(event)
        idCheck.handle_event(event)
        # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_F11:
                # Toggle fullscreen mode
                pygame.display.toggle_fullscreen()
                background()
            if event.key == pygame.K_F12:
                input_boxes = inputBoxLoad()
    return input_boxes
def background():
    #Wiping after logo
    pygame.display.set_caption('Player Selection')
    screen.fill("black")
    title()
    redX = X/2 - 100 - 400 - 100  # middle of screen, 100 left of box, 400 for width of boxes, 100 right of boxes
    redY = 75
    redW = 100+400+100            #100 left of box, 400 for width of boxes, 100 right of boxes
    redH = 720
    greenX = X/2
    greenY = 75
    greenW = 100 + 400 + 100
    greenH = 720
    # Setup player selection environment
    pygame.draw.rect(screen, red, pygame.Rect(redX, redY, redW, redH))
    pygame.draw.rect(screen, green, pygame.Rect(greenX, greenY, greenW, greenH))
    textBox("ID", red, "white", redX+100+100, redY+30)
    textBox("ID", green, "white", greenX+100+100, greenY+30)
    textBox("Name", red, "white", redX+redW-100-100, redY+30)
    textBox("Name", green, "white", greenX+greenW-100-100, greenY+30)

def inputBoxLoad():
    inputBoxes = []
    numberBoxes = 15
    startY = 140
    boxHeight = 32
    boxWidth = 200
    endHeight = numberBoxes * boxHeight + startY
    redBoxX = X/2-100-400
    greenBoxX = X/2+100
    for i in range(startY,endHeight,boxHeight): # range(starting y, ending y, increment y)
        temp = InputLine(redBoxX, i, boxWidth, boxHeight) # X, Y, W, H
        inputBoxes.append(temp)
    for i in range(startY,endHeight,boxHeight): # range(starting y, ending y, increment y)
        temp = InputLine(greenBoxX, i, boxWidth, boxHeight) # X, Y, W, H
        inputBoxes.append(temp)
    return inputBoxes

def addPlayer():
    print('Add Player pressed')
    print('Id Field ' + idField.getText())

def onStart():
    print('Start pressed')

def game():
    running = True
    splashScreen()
    screen = pygame.display.set_mode((desktop.current_w, desktop.current_h))
    X = int(screen.get_width())
    Y = int(screen.get_height())
    background()
    input_boxes = inputBoxLoad()
    # Player ID input
    idField = InputBox(X/2-100, Y/2+150, 200, 32)
    # Add Player button
    addPlayerButton = Button(X/2-64, Y/2+200, 128, 32, 'Add Player', idField.getText())
    # Start button
    startButton = Button(X/2-35, Y/2+250, 70, 32, 'Start', onStart)

    # Main loop
    while running:
        background()
        for box in input_boxes:
            box.draw(screen)
        idField.draw(screen)
        addPlayerButton.process(screen)
        startButton.process(screen)
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
        input_boxes = events(input_boxes, idField)

# Run Game
game()
