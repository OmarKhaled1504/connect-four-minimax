import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

block_color = (53, 115, 255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()




def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('You Crashed')


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        # print(mouse)

        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, red, (150, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (150, 450, 100, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("GO!", smallText)
        textRect.center = ((150 + (100 / 2)), (450 + (50 / 2)))
        gameDisplay.blit(textSurf, textRect)

        pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

        pygame.display.update()
        clock.tick(15)
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()



# import pygame
# from pygame.locals import *
#
# pygame.init()
#
# screen_width = 600
# screen_height = 600
#
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Button Demo')
#
# font = pygame.font.SysFont('Constantia', 30)
#
# # define colours
# bg = (204, 102, 0)
# red = (255, 0, 0)
# black = (0, 0, 0)
# white = (255, 255, 255)
#
# # define global variable
# clicked = False
# counter = 0
#
#
# class button():
#     # colours for button and text
#     button_col = (255, 0, 0)
#     hover_col = (75, 225, 255)
#     click_col = (50, 150, 255)
#     text_col = black
#     width = 180
#     height = 70
#
#     def __init__(self, x, y, text):
#         self.x = x
#         self.y = y
#         self.text = text
#
#     def draw_button(self):
#
#         global clicked
#         action = False
#
#         # get mouse position
#         pos = pygame.mouse.get_pos()
#
#         # create pygame Rect object for the button
#         button_rect = Rect(self.x, self.y, self.width, self.height)
#
#         # check mouseover and clicked conditions
#         if button_rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0] == 1:
#                 clicked = True
#                 pygame.draw.rect(screen, self.click_col, button_rect)
#             elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
#                 clicked = False
#                 action = True
#             else:
#                 pygame.draw.rect(screen, self.hover_col, button_rect)
#         else:
#             pygame.draw.rect(screen, self.button_col, button_rect)
#
#         # add shading to button
#         pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
#         pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
#         pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
#         pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
#
#         # add text to button
#         text_img = font.render(self.text, True, self.text_col)
#         text_len = text_img.get_width()
#         screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
#         return action
#
#
# again = button(75, 200, 'Play Again?')
# quit = button(325, 200, 'Quit?')
# run = True
# while run:
#
#     screen.fill(bg)
#     if again.draw_button():
#         counter = 0
#     if quit.draw_button():
#         print('Quit')
#
#
#
#     counter_img = font.render(str(counter), True, red)
#     screen.blit(counter_img, (280, 450))
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     pygame.display.update()
#
# pygame.quit()