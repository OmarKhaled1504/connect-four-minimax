import random
import numpy as connect4
import pygame
import sys
import math
import main
import time
from pygame import mixer

BLUE = (0, 0, 90)  # value for blue # color of board
BLACK = (0, 0, 0)  # value for black # color of background
RED = (240, 0, 0)  # value for red   # color of our 2oshat
YELLOW = (255, 255, 0)  # value for yellow  #color of ai 2oshat
SHADOW = (192, 192, 192)
green = (0, 200, 0)

bright_red = (255, 0, 180)
bright_green = (0, 255, 0)

ROW_COUNT = 6  # number of rows
COLUMN_COUNT = 7  # number of columns
square_size = 100  # size of square

player = 0
ai = 1

empty = 0
pl_piece = 1
ai_piece = 2

display_width = 800
display_height = 600

square_length = 4
pr = 0
# Setup pygame/window ---------------------------------------- #

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('game base')
gameDisplay = pygame.display.set_mode((display_width, display_height))
myfont = pygame.font.SysFont("monospace", 75)

# FUNCTION TO DRAW ON SCREEN

smallText = pygame.font.SysFont("comicsansms", 20)
mediumText = pygame.font.SysFont("monospace", 35)
largeText = pygame.font.SysFont("comicsansms", 115)


# function to add buttons
def message_display(text):
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((display_width / 2), 450)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def button(msg, x, y, w, h, ic, ac, action=None):
    global pr
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if msg == "START(P)":
                pr = 1

            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def text_objects(text, font):
    textsurface = font.render(text, True, BLACK)
    return textsurface, textsurface.get_rect()


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, BLACK)
    gameDisplay.blit(text, (0, 0))


# ---------------------------------------------------------------#

user_text = ''


def game_intro():
    intro = True

    global user_text
    input_rect = pygame.Rect((display_width / 2 - 30, 500, 50, 50))
    color_active = RED
    color_passive = bright_red
    color = color_passive
    active = False

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        gameDisplay.fill(SHADOW)

        TextSurf1, TextRect1 = text_objects("CONNECT 4", largeText)
        TextRect1.center = ((display_width / 2), (display_height / 4))
        gameDisplay.blit(TextSurf1, TextRect1)
        TextSurf2, TextRect2 = text_objects("ENTER THE MINIMAX DEPTH", smallText)
        TextRect2.center = ((display_width / 2), 450)
        gameDisplay.blit(TextSurf2, TextRect2)
        button("START", 200, 350, 100, 50, green, bright_green, game)
        button("START(P)", 500, 350, 120, 50, RED, bright_red, game)
        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(gameDisplay, color, input_rect, 2)
        text_surface = mediumText.render(user_text, True, BLACK)
        gameDisplay.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(30, text_surface.get_width() + 10)

        pygame.display.update()



def game():
    if user_text == '':
        z = 1
    else:
        z = int(user_text)



    if z > 7:
        z = 7
    elif z == 0:
        z = 1

    global runtime


    def create_board():
        board = connect4.zeros((ROW_COUNT, COLUMN_COUNT))  # matrix of zeros 6 x 7
        return board

    def drop_piece(board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(board, col):
        return board[ROW_COUNT - 1][col] == 0

    def get_next_open_row(board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def draw_board(board):
        for c in range(COLUMN_COUNT):  # drawing the rectangle of the board
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE,
                                 (c * square_size, r * square_size + square_size, square_size, square_size))
                pygame.draw.circle(screen, SHADOW, (
                    int(c * square_size + square_size / 2), int(r * square_size + square_size + square_size / 2)),
                                   RADIUS)  # drawing the circles inside rectangle of the board

        for c in range(COLUMN_COUNT):  # adds in the matrix updates list
            for r in range(ROW_COUNT):
                if board[r][c] == pl_piece:
                    pygame.draw.circle(screen, RED, (
                        int(c * square_size + square_size / 2), height - int(r * square_size + square_size / 2)),
                                       RADIUS)
                elif board[r][c] == ai_piece:
                    pygame.draw.circle(screen, YELLOW, (
                        int(c * square_size + square_size / 2), height - int(r * square_size + square_size / 2)),
                                       RADIUS)
        pygame.display.update()

    board = create_board()
    game_over = False
    width = COLUMN_COUNT * square_size
    height = (ROW_COUNT + 1) * square_size

    size = (width, height)
    RADIUS = int(square_size / 2 - 5)
    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    # turn = random.randint(player, ai)  # makes a random start of player or ai
    turn = 0
    # **************************************************
    game = main.Game()
    state = game.start()
    main.print_board(state)
    # ***************************************************

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, SHADOW, (0, 0, width, square_size))  # BETRG3HA shadow
                posx = event.pos[0]
                if turn == player:
                    pygame.draw.circle(screen, RED, (posx, int(square_size / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, SHADOW, (0, 0, width, square_size))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == player:
                    posx = event.pos[0]
                    col = int(math.floor(posx / square_size))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, pl_piece)
                        state = main.set_chip(state, col, row, '1')
                        # main.space_tracker[(col, row)] = 1
                        print("PLAYER TURN")
                        main.print_board(state)
                        print('\n')
                        turn += 1
                        turn = turn % 2
                        draw_board(board)
                # ########## ai Input
        if turn == ai and not game_over:

            col = random.randint(0, COLUMN_COUNT - 1)

            if is_valid_location(board, col):
                pygame.time.wait(100)
                row = get_next_open_row(board, col)
                if pr:
                    start_time = time.time()
                    (state, index) = main.decisionwp(state, z)
                    t2 = time.localtime()
                    runtime = (time.time() - start_time)
                    i = index[0]
                    j = index[1]
                    # main.space_tracker[(i, j)] = 1
                    drop_piece(board, j, i, ai_piece)
                else:
                    start_time = time.time()
                    main.minimax_tree.clear()
                    (state, index) = main.decision(state, z)
                    runtime = (time.time() - start_time)
                    i = index[0]
                    j = index[1]
                    # main.space_tracker[(i, j)] = 1
                    drop_piece(board, j, i, ai_piece)
                # *****************************************************************
                if main.terminal_test(state):
                    if main.red_score(state) < main.yellow_score(state):
                        label = mediumText.render(f"AI WINS!!  red ={main.red_score(state)} "
                                                  f" yellow ={main.yellow_score(state)}", True, BLACK)
                        screen.blit(label, (40, 10))
                        game_over = True
                    elif main.red_score(state) > main.yellow_score(state):
                        label = mediumText.render(f"PLAYER WINS!! yellow ={main.yellow_score(state)} "
                                                  f"red ={main.red_score(state)} ", True, BLACK)
                        screen.blit(label, (40, 10))
                        game_over = True
                    else:
                        label = mediumText.render(f"DRAW!!  red ={main.red_score(state)} "
                                                  f" yellow ={main.yellow_score(state)}", True, BLACK)
                        screen.blit(label, (40, 10))
                        game_over = True
                # print_board(board)
                draw_board(board)
                print("AI TURN")
                main.print_board(state)
                print('\n')
                print('NODES EXPANDED BY MINIMAX', main.nodes_expanded)
                print('RUNTIME: ', runtime)
                print('PLAYER SCORE= ', main.red_score(state), '   ', 'AI SCORE= ', main.yellow_score(state), '\n')
                #main.generate_tree(main.minimax_tree)
                # BET5ALY EL TURN YA 0 YA 1
                turn += 1
                turn = turn % 2
        if game_over:
            pygame.time.wait(4000)  # WAITS 4000 MILISECONDS
            sys.exit()


game_intro()
