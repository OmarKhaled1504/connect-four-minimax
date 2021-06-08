# 0 FOR EMPTY SPACE
# 1 FOR RED CHIP
# 2 FOR YELLOW CHIP
# j is row
# i is column
import math


class Game:
    def __init__(self):
        self.red_score = 0
        self.yellow_score = 0
        self.board = []

    def start(self):
        board = ['000000', '000000', '000000', '000000', '000000', '000000', '000000']
        return board

    # def over(self):
    #     if terminal_test(board):
    #         return 1
    #     else:
    #         return 0
    def winner(self):
        if self.red_score > self.yellow_score:
            return 1
        elif self.red_score < self.yellow_score:
            return 2
        else:
            return 0


# TAKES AN INPUT STATE AND GENERATES ALL POSSIBLE MOVES FROM THIS STATE
def state_children(state, val):
    children = []
    indices = []
    for i in range(0, 7):
        for j in range(0, 6):
            if get_chip(state[i], j) == '0':
                child = set_chip(state, i, j, val)
                index = (i, j)
                children.append(child)
                indices.append(index)
                break

    return (children, indices)


def detect_four_vertically(column, val):
    k = 4
    for j in range(0, 6):
        if get_chip(column, j) == val:
            k -= 1
            if k == 0:
                return 1
        else:
            k = 4


def vertical_count(state, val):
    count = 0
    for column in state:
        if detect_four_vertically(column, val):
            count += 1
    return count


def detect_four_horizontally(state, row, val):
    k = 4
    for i in range(0, 7):
        if get_chip(state[i], row) == val:
            k -= 1
            if k == 0:
                return 1
        else:
            k = 4


def horizontal_count(state, val):
    count = 0
    for j in range(0, 6):
        if detect_four_horizontally(state, j, val):
            count += 1
    return count


def detectDiagonalLtoR(state, val):
    k = l = m = n = o = p = 4
    count = 0
    for i in range(0, 6):
        if get_chip(state[i], i) == val:  # state[0] gets row of index 0, 2nd arg column gets coordinates of chip
            k -= 1
            if k == 0:
                count += 1
        else:
            k = 4
    for i in range(1, 7):
        if get_chip(state[i], i + 1) == val:
            l -= 1
            if l == 0:
                count += 1
        else:
            l = 4
    for i in range(2, 7):
        if get_chip(state[i], i + 1) == val:
            m -= 1
            if m == 0:
                count += 1
        else:
            m = 4
    for i in range(3, 7):
        if get_chip(state[i], i + 1) == val:
            n -= 1
            if n == 0:
                count += 1
        else:
            n = 4
    for i in range(0, 4):
        if get_chip(state[i + 1], i) == val:
            o -= 1
            if o == 0:
                count += 1
        else:
            o = 4
    for i in range(0, 3):
        if get_chip(state[i + 2], i) == val:
            p -= 1
            if p == 0:
                count += 1
        else:
            p = 4
    return count


def detectDiagonalRtoL(state, val):
    k = l = m = n = o = p = 4
    count = 0
    for i in range(5, 0, -1):
        if get_chip(state[i], i) == val:
            k -= 1
            if k == 0:
                count += 1
    for i in range(6, 1, -1):
        if get_chip(state[i], i + 1) == val:
            l -= 1
            if l == 0:
                count += 1
    for i in range(6, 2, -1):
        if get_chip(state[i], i + 1) == val:
            m -= 1
            if m == 0:
                count += 1
    for i in range(6, 3, -1):
        if get_chip(state[i], i + 1) == val:
            n -= 1
            if n == 0:
                count += 1
    for i in range(3, 0, -1):
        if get_chip(state[i + 1], i) == val:
            o -= 1
            if o == 0:
                count += 1
    for i in range(3, 0, -1):
        if get_chip(state[i + 2], i) == val:
            p -= 1
            if p == 0:
                count += 1
    return count

#
# def diagonal_count(state, val):
#     count = 0
#     for k in range(0, 6 + 7 - 2 + 1):
#         fourinrow = 4
#         for j in range(0, k + 1):
#             i = k - j
#             if i < 6 and j < 7:
#                 if get_chip(state[j], i) == val:
#                     # print(get_chip(state[j],i))
#                     fourinrow -= 1
#                     if fourinrow == 0:
#                         count += 1
#                 else:
#                     fourinrow = 4
#
#     # for k in range(0,12):
#     #     fourinrow = 4
#     #     for i in range(0,k+1):
#     #         j = 6 + i
#     #         if i > -1 and j < 7:
#     #             print(i, j)
#     #             if get_chip(state[j], i) == val:
#     #                 #print(get_chip(state[j],i))
#     #
#     #                 fourinrow -= 1
#     #                 if fourinrow == 0:
#     #                     count += 1
#     #             else:
#     #                 fourinrow = 4
#     #     print('\n')
#     return count


def downtoup_diagonal_count(state, value):
    connected_fours = 0
    for j in range(4):
        for i in range(3):
            jd = j
            id = i
            count = 0
            four_in_a_row = True
            while count < 4:
                if state[jd][id] != value:
                    four_in_a_row = False
                    break
                count += 1
                jd += 1
                id += 1
            if four_in_a_row:
                connected_fours += 1
    return connected_fours


def uptodown_diagonal_count(state, value):
    connected_fours = 0
    for j in range(4):
        for i in range(3, 6):
            jd = j
            id = i
            count = 0
            four_in_a_row = True
            while count < 4:
                print(jd,id)
                if state[jd][id] != value:
                    four_in_a_row = False
                    break
                count += 1
                jd += 1
                id -= 1
            if four_in_a_row:
                connected_fours += 1
    return connected_fours

def red_score(state):
    return horizontal_count(state, '1') + vertical_count(state, '1') + uptodown_diagonal_count(state,'1') + downtoup_diagonal_count(state,'1')


def yellow_score(state):
    return horizontal_count(state, '2') + vertical_count(state, '2') + uptodown_diagonal_count(state,'2') + downtoup_diagonal_count(state,'2')


def evaluate(state):
    return red_score(state) - yellow_score(state)


def terminal_test(state):
    for i in range(0, 7):
        for j in range(0, 6):
            if get_chip(state[i], j) == '0':
                return 0
    return 1


# minimax with alpha beta pruning#########################
def decisionwp(state):
    (child, temp, index) = maximizewp(state, -math.inf, math.inf, 8)
    return (child, index)


def minimizewp(state, alpha, beta, steps_count):
    if terminal_test(state):
        return (None, evaluate(state), None)
    if steps_count == 0:
        return (None, evaluate(state), None)
    (minChild, minUtility, index) = (None, 500, None)
    steps_count -= 1
    (children, indices) = state_children(state, '2')
    i = 0
    for child in children:
        (temp, utility, index) = maximizewp(child, alpha, beta, steps_count)
        if utility < minUtility:
            (minChild, minUtility, index) = (child, utility, indices[i])
        if minUtility <= alpha:
            break
        if minUtility < beta:
            beta = minUtility
        i += 1
    return (minChild, minUtility, index)


def maximizewp(state, alpha, beta, steps_count):
    if terminal_test(state):
        return (None, evaluate(state), None)
    if steps_count == 0:
        return (None, evaluate(state), None)

    (maxChild, maxUtility, index) = (None, -500, None)
    steps_count -= 1
    (children, indices) = state_children(state, '2')
    i = 0
    for child in children:
        (temp, utility, index) = minimizewp(child, alpha, beta, steps_count)
        if utility > maxUtility:
            (maxChild, maxUtility, index) = (child, utility, indices[i])
        if maxUtility >= beta:
            break
        if maxUtility > alpha:
            alpha = maxUtility
        i += 1
    return (maxChild, maxUtility, index)


#########################################################

def maximize(state, steps_count):
    if terminal_test(state):
        return (None, evaluate(state))
    if steps_count == 0:
        return (None, evaluate(state))

    (maxChild, maxUtility) = (None, -500)
    steps_count -= 1
    for child in state_children(state, '2'):
        (temp, utility) = minimize(child, steps_count)
        if utility > maxUtility:
            (maxChild, maxUtility) = (child, utility)

    return (maxChild, maxUtility)


def minimize(state, steps_count):
    if terminal_test(state):
        return (None, evaluate(state))
    if steps_count == 0:
        return (None, evaluate(state))

    (minChild, minUtility) = (None, 500)
    steps_count -= 1
    for child in state_children(state, '1'):
        (temp, utility) = maximize(child, steps_count)
        if utility < minUtility:
            (minChild, minUtility) = (child, utility)

    return (minChild, minUtility)


def decision(state):
    (child, temp) = maximize(state, 5)
    return child


def get_chip(column, j):
    word = split(column)
    return word[j]
    # return int(column / (10 ** (5 - j)) % 10)


def split(word):
    return [char for char in word]


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
        # return string
    return str1


def set_chip(state, i, j, val):
    new_state = state.copy()
    x = split(new_state[i])
    x[j] = str(val)
    new_state[i] = listToString(x)
    return new_state


def print_board(state):
    for j in range(5, -1, -1):
        print(get_chip(state[0], j), '', get_chip(state[1], j), '', get_chip(state[2], j), '', get_chip(state[3], j),
              '',
              get_chip(state[4], j), '', get_chip(state[5], j), '', get_chip(state[6], j))


# while not terminal_test(board):
#     print('ENTER YOUR MOVE\n')
#     j = int(input('ROW: '))
#     i = int(input('\nCOLUMN: '))
#     board = set_chip(board, i, j, '1')
#     print("YOUR MOVE\n")
#     print_board(board)
#     (board, index) = decisionwp(board)
#     print("BOTS'S MOVE\n")
#     print_board(board)


state = ['111111', '111111', '111111', '111111', '000000', '000000', '000000']
(children, indices) = state_children(state, '1')
print_board(state)
print(downtoup_diagonal_count(state,'1'))

# for item in children:
#     print_board(item)
#     print('\n')
# print(indices)
#
# print_board(state)
# print('\n')
# state = decisionwp(state)
# print_board(state)
# print('\n')
#
# state = decisionwp(state)
# print_board(state)
# print('\n')
#
# state = decisionwp(state)
# print_board(state)
# print('\n')
#
# state = decision(state)
# print_board(state)
# print('\n')
