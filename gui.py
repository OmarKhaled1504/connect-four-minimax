import random
from pygame.locals import *
import numpy as connect4
import pygame
import sys
import math
import main

from pygame import mixer
BLUE = (0, 0, 128)  # value for blue # color of board
BLACK = (0, 0, 0)  # value for black # color of background
RED = (255, 100, 100)  # value for red   # color of our 2oshat
YELLOW = (255, 255, 0)  # value for yellow  #color of ai 2oshat
SHADOW = (192, 192, 192)

ROW_COUNT = 6  # number of rows
COLUMN_COUNT = 7  # number of columns
square_size = 100  # size of square

player = 0
ai = 1

empty = 0
pl_piece = 1
ai_piece = 2

square_length = 4

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((650, 500), 0, 32)
myfont = pygame.font.SysFont("monospace", 75)


# FUNCTION TO DRAW ON SCREEN
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# mixer.music.load("background.wav")
# mixer.music.play(-1)

click = False


# ---------------------------------------------------------------#


def main_menu():
    while True:
        pygame.display.set_caption('CONNECT 4 ')
        screen.fill(BLACK)
        draw_text('CONNECT FOUR', myfont, RED, screen, 40, 25)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(225, 400, 200, 50)

        text = myfont.render('quit', True, BLACK)
        if button_1.collidepoint((mx, my)):
            if click:
                game()

        pygame.draw.rect(screen, SHADOW, button_1)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


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

    def print_board(board):
        print(connect4.flip(board, 0))

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

    def get_valid_locations(board):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if is_valid_location(board, col):
                valid_locations.append(col)
        return valid_locations

    board = create_board()
    game_over = False
    width = COLUMN_COUNT * square_size
    height = (ROW_COUNT + 1) * square_size

    size = (width, height)
    RADIUS = int(square_size / 2 - 5)
    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    #turn = random.randint(player, ai)  # makes a random start of player or ai
    turn = 0
    game = main.Game()
    state = game.start()

    main.print_board(state)
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
                (state, index) = main.decisionwp(state)
                print(index)
                i = index[0]
                j = index[1]

                drop_piece(board, j, i, ai_piece)
                if main.terminal_test(state):
                    if main.red_score(state) <= main.yellow_score(state):
                        label = myfont.render("AI WINS!!", True, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True
                    else:
                        label = myfont.render("PLAYER WINS!!", True, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

                #print_board(board)
                draw_board(board)
                print("AI TURN")
                main.print_board(state)
                print('\n')
                # BET5ALY EL TURN YA 0 YA 1
                turn += 1
                turn = turn % 2
        if game_over:
            pygame.time.wait(5000)  # WAITS 3000 MILISECONDS
            sys.exit()


main_menu()