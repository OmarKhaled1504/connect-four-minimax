import random
import numpy as connect4
import pygame
import sys
import math
import main
import time
from pygame import mixer

BLUE = (0, 0, 128)  # value for blue # color of board
BLACK = (0, 0, 0)  # value for black # color of background
RED = (255, 100, 100)  # value for red   # color of our 2oshat
YELLOW = (255, 255, 0)  # value for yellow  #color of ai 2oshat
SHADOW = (192, 192, 192)
green = (0, 200, 0)

bright_red = (255, 0, 0)
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
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


# function to add buttons
def button(msg, x, y, w, h, ic, ac, action=None):
    global pr
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if msg == "PRUNING":
                pr = 1

            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
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


# mixer.music.load("background.wav")
# mixer.music.play(-1)

# click = False


# ---------------------------------------------------------------#


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(SHADOW)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("CONNECT 4", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("START", 150, 450, 100, 50, green, bright_green, game)
        # SHEEL GAME WE HOT BEL MINIMAX
        button("PRUNING", 550, 450, 100, 80, RED, bright_red, game)

        pygame.display.update()


def game():
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
    #**************************************************
    game = main.Game()
    state = game.start()
    main.print_board(state)
    #***************************************************

    while not game_over:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, square_size))  # BETRG3HA BLACK
                posx = event.pos[0]
                if turn == player:
                    pygame.draw.circle(screen, RED, (posx, int(square_size / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, square_size))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == player:
                    posx = event.pos[0]
                    col = int(math.floor(posx / square_size))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, pl_piece)
                        state = main.set_chip(state, col, row, '1')
                        print("PLAYER TURN")
                        main.print_board(state)
                        print('\n')
                        turn += 1
                        turn = turn % 2
                        draw_board(board)
                # # ai Input
        if turn == ai and not game_over:

            col = random.randint(0, COLUMN_COUNT - 1)
            # hot hena el functions ely hatnady 3aleha
            if is_valid_location(board, col):
                pygame.time.wait(100)
                row = get_next_open_row(board, col)
                print(pr)
                if pr:
                    (state, index) = main.decisionwp(state)
                    i = index[0]
                    j = index[1]
                    drop_piece(board, j, i, ai_piece)
                # else:
                #     (state, index) = main.decision(state)
                #     print(index)
                #     i = index[0]
                #     j = index[1]
                #     drop_piece(board, j, i, ai_piece)
                # *****************************************************************
                if main.terminal_test(state):
                    if main.red_score(state) <= main.yellow_score(state):
                        label = myfont.render("AI WINS!!", True, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True
                    else:
                        label = myfont.render("PLAYER WINS!!", True, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

                # print_board(board)
                draw_board(board)
                print("AI TURN")
                main.print_board(state)
                print('\n')
                #print(main.minimax_tree,'\n')
                print('PLAYER SCORE= ',main.red_score(state),'   ','AI SCORE= ',main.yellow_score(state),'\n')
                # BET5ALY EL TURN YA 0 YA 1
                turn += 1
                turn = turn % 2
        if game_over:
            pygame.time.wait(5000)  # WAITS 3000 MILISECONDS
            sys.exit()


game_intro()
