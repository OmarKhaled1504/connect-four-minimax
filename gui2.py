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
# down = button(75, 350, 'Down')
# up = button(325, 350, 'Up')
#
# run = True
# while run:
#
#     screen.fill(bg)
#
#     if again.draw_button():
#         print('Again')
#         counter = 0
#     if quit.draw_button():
#         print('Quit')
#     if up.draw_button():
#         print('Up')
#         counter += 1
#     if down.draw_button():
#         print('Down')
#         counter -= 1
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
# # import random
# #
# # import numpy as connect4
# # import pygame
# # import sys
# # import math
# #
# # BLUE = (0, 0, 128)  # value for blue # color of board
# # BLACK = (0, 0, 0)  # value for black # color of background
# # RED = (255, 100, 100)  # value for red   # color of our 2oshat
# # YELLOW = (255, 255, 0)  # value for yellow  #color of ai 2oshat
# # SHADOW = (192, 192, 192)
# #
# # ROW_COUNT = 6  # number of rows
# # COLUMN_COUNT = 7  # number of columns
# # square_size = 100  # size of square
# #
# # player = 0
# # ai = 1
# #
# # empty = 0
# # pl_piece = 1
# # ai_piece = 2
# #
# # square_length = 4
# #
# #
# # def screen2():
# #     def create_board():
# #         board = connect4.zeros((ROW_COUNT, COLUMN_COUNT))  # matrix of zeros 6 x 7
# #         return board
# #
# #     def drop_piece(board, row, col, piece):
# #         board[row][col] = piece
# #
# #     def is_valid_location(board, col):
# #         return board[ROW_COUNT - 1][col] == 0
# #
# #     def get_next_open_row(board, col):
# #         for r in range(ROW_COUNT):
# #             if board[r][col] == 0:
# #                 return r
# #
# #     def print_board(board):
# #         print(connect4.flip(board, 0))
# #
# #     def draw_board(board):
# #         for c in range(COLUMN_COUNT):  # drawing the rectangle of the board
# #             for r in range(ROW_COUNT):
# #                 pygame.draw.rect(screen, BLUE,
# #                                  (c * square_size, r * square_size + square_size, square_size, square_size))
# #                 pygame.draw.circle(screen, SHADOW, (
# #                     int(c * square_size + square_size / 2), int(r * square_size + square_size + square_size / 2)),
# #                                    RADIUS)  # drawing the circles inside rectangle of the board
# #
# #         for c in range(COLUMN_COUNT):  # adds in the matrix updates list
# #             for r in range(ROW_COUNT):
# #                 if board[r][c] == pl_piece:
# #                     pygame.draw.circle(screen, RED, (
# #                         int(c * square_size + square_size / 2), height - int(r * square_size + square_size / 2)),
# #                                        RADIUS)
# #                 elif board[r][c] == ai_piece:
# #                     pygame.draw.circle(screen, YELLOW, (
# #                         int(c * square_size + square_size / 2), height - int(r * square_size + square_size / 2)),
# #                                        RADIUS)
# #         pygame.display.update()
# #
# #     def get_valid_locations(board):
# #         valid_locations = []
# #         for col in range(COLUMN_COUNT):
# #             if is_valid_location(board, col):
# #                 valid_locations.append(col)
# #         return valid_locations
# #
# #     board = create_board()
# #     game_over = False
# #     pygame.init()
# #     width = COLUMN_COUNT * square_size
# #     height = (ROW_COUNT + 1) * square_size
# #
# #     size = (width, height)
# #     RADIUS = int(square_size / 2 - 5)
# #     screen = pygame.display.set_mode(size)
# #     draw_board(board)
# #     pygame.display.update()
# #
# #     myfont = pygame.font.SysFont("monospace", 75)
# #
# #     turn = random.randint(player, ai)  # makes a random start of player or ai
# #     while not game_over:
# #
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 sys.exit()
# #
# #             if event.type == pygame.MOUSEMOTION:
# #                 pygame.draw.rect(screen, BLACK, (0, 0, width, square_size))  # BETRG3HA BLACK
# #                 posx = event.pos[0]
# #                 if turn == player:
# #                     pygame.draw.circle(screen, RED, (posx, int(square_size / 2)), RADIUS)
# #             pygame.display.update()
# #
# #             if event.type == pygame.MOUSEBUTTONDOWN:
# #                 pygame.draw.rect(screen, BLACK, (0, 0, width, square_size))
# #                 # print(event.pos)
# #                 # Ask for Player 1 Input
# #                 if turn == player:
# #                     posx = event.pos[0]
# #                     col = int(math.floor(posx / square_size))
# #
# #                     if is_valid_location(board, col):
# #                         row = get_next_open_row(board, col)
# #                         drop_piece(board, row, col, pl_piece)
# #
# #                         # if main.red_score(board)>>main.yellow_score(board):
# #                         #     label = myfont.render("Player 1 wins!!", 1, RED)
# #                         #     screen.blit(label, (40, 10))
# #                         #     game_over = True
# #                         turn += 1
# #                         turn = turn % 2
# #                         print_board(board)
# #                         draw_board(board)
# #                 # # ai Input
# #         if turn == ai and not game_over:
# #
# #             col = random.randint(0, COLUMN_COUNT - 1)
# #             # hot hena el functions ely hatnady 3aleha
# #             if is_valid_location(board, col):
# #                 pygame.time.wait(300)
# #                 row = get_next_open_row(board, col)
# #                 drop_piece(board, row, col, ai_piece)
# #
# #                 # if main.red_score(board)<<main.yellow_score(board):
# #                 #     label = myfont.render("Player 2 wins!!", 1, YELLOW)
# #                 #     screen.blit(label, (40, 10))
# #                 #     game_over = True
# #
# #                 print_board(board)
# #                 draw_board(board)
# #                 # BET5ALY EL TURN YA 0 YA 1
# #                 turn += 1
# #                 turn = turn % 2
# #         if game_over:
# #             pygame.time.wait(3000)  # WAITS 3000 MILISECONDS
# #
# #
# # screen2()
