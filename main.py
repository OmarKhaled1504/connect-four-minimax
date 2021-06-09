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
#THIS CLASS IS ONLY USED TO TRANSFER THE INDEX OF THE AI'S MOVE TO THE GUI
class Child:
    def __init__(self, state, index):
        self.state = state
        self.index = index

#TAKES AN INPUT STATE AND GENERATES ALL POSSIBLE MOVES FROM THIS STATE
def state_children(state, val):
    children = []
    indices = []
    for i in range(0, 7):
        for j in range(0, 6):
            if get_chip(state[i], j) == '0':
                temp = set_chip(state, i, j, val)
                index = (i, j)
                child = Child(temp, index)
                children.append(child)

                break


    return (children)


def detect_four_vertically(column, val):
    k = 4
    for j in range(0, 6):
        if get_chip(column, j) == val:
            k -= 1
            if k == 0:
                return 1
        else:
            k = 4
def detect_3_vertically(column, val):
    k = 3
    for j in range(0, 6):
        if get_chip(column, j) == val:
            k -= 1
            if k == 0 and j<=4 and get_chip(column, j+1) == '0':
                return 1
            elif k == 1 and j<=4 and get_chip(column, j+1) == '0':
                return 2
        else:
            k = 3

def vertical_4_count(state, val):
    count = 0
    for column in state:
        if detect_four_vertically(column, val):
            count += 1
    return count

def vertical_3_count(state, val):
    count3 = 0
    count2 = 0
    for column in state:
        x = detect_3_vertically(column,val)
        if x == 1:
            count3 += 1
        elif x ==2:
            count2 +=1

    return (count2, count3)


def detect_four_horizontally(state, row, val):
    k = 4
    for i in range(0, 7):
        if get_chip(state[i], row) == val:
            k -= 1
            if k == 0:
                return 1
        else:
            k = 4
def detect_three_horizontally(state, row, val):
    k = 3
    for i in range(0, 7):
        if get_chip(state[i], row) == val:
            k -= 1
            if k == 0 and i <= 5 and state[i+1][row] == '0' and i >= 3 and state[i-3][row] == '0':
                return 2
            elif k == 0 and i <=5 and state[i+1][row] == '0':

                return 1
            elif k == 0 and i >= 3 and state[i-3][row] == '0':
                return 1

        else:
            k = 3



def horizontal_4_count(state, val):
    count = 0
    for j in range(0, 6):
        if detect_four_horizontally(state, j, val):
            count += 1
    return count

def horizontal_3_count(state, val):
    count = 0
    for j in range(0, 6):
        if detect_three_horizontally(state, j, val) == 1:
            count += 1
        elif detect_three_horizontally(state, j, val) == 2:
            count += 2
    return count


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
                if state[jd][id] != value:
                    four_in_a_row = False
                    break
                count += 1
                jd += 1
                id -= 1
            if four_in_a_row:
                connected_fours += 1
    return connected_fours

def red_3_score(state):
    (x, y) = vertical_3_count(state, '1')
    return horizontal_3_count(state, '1') + y


def yellow_3_score(state):
    (x, y) = vertical_3_count(state, '2')
    return horizontal_3_count(state, '2') + y

def red_2_score(state):
    (x, y) = vertical_3_count(state, '1')
    return x


def yellow_2_score(state):
    (x, y) = vertical_3_count(state, '2')
    return x

def red_score(state):
    return horizontal_4_count(state, '1') + vertical_4_count(state, '1') + uptodown_diagonal_count(state, '1') + downtoup_diagonal_count(state, '1')


def yellow_score(state):
    return horizontal_4_count(state, '2') + vertical_4_count(state, '2') + uptodown_diagonal_count(state, '2') + downtoup_diagonal_count(state, '2')


def evaluate(state):
    x = yellow_score(state)*20
    y = red_score(state)*-20
    z = red_3_score(state)*-8
    a = yellow_3_score(state)*8
    d = red_2_score(state)*-5
    c = yellow_2_score(state)*5


    return x + y + z + a + d + c


def terminal_test(state):
    for i in range(0, 7):
        for j in range(0, 6):
            if get_chip(state[i], j) == '0':
                return 0
    return 1


# ********************************** MINIMAX WITH ALPHA BETA PRUNING ***************************************************

minimax_tree = []
def decisionwp(state):

    (child, temp, index) = maximizewp(state, -math.inf, math.inf, 6)
    return (child, index)


def minimizewp(state, alpha, beta, steps_count):
    if terminal_test(state):
        return (None, evaluate(state),None)
    if steps_count == 0:
        value = evaluate(state)
        minimax_tree.append(value)
        return (None, value,None)
    (minChild, minUtility, index) = (None, 500, None)
    steps_count -= 1

    for child in state_children(state, '1'):
        (temp, utility, temp2) = maximizewp(child.state, alpha, beta, steps_count)
        if utility < minUtility:
            (minChild, minUtility, index) = (child.state, utility, child.index)
        if minUtility <= alpha:
            break
        if minUtility < beta:
            beta = minUtility


    return (minChild, minUtility, index)


def maximizewp(state, alpha, beta, steps_count):
    if terminal_test(state):
        return (None, evaluate(state), None)
    if steps_count == 0:
        value = evaluate(state)
        minimax_tree.append(value)
        return (None, value, None)

    (maxChild, maxUtility, index) = (None, -500, None)
    steps_count -= 1
    for child in state_children(state, '2'):
        (temp, utility, temp2) = minimizewp(child.state, alpha, beta, steps_count)
        if utility > maxUtility:
            (maxChild, maxUtility, index) = (child.state, utility, child.index)
        if maxUtility >= beta:
            break
        if maxUtility > alpha:
            alpha = maxUtility


    return (maxChild, maxUtility, index)


#*************************************** MINIMAX *******************************************************

def maximize(state, steps_count):
    if terminal_test(state):
        return (None, evaluate(state), None)
    if steps_count == 0:
        return (None, evaluate(state), None)

    (maxChild, maxUtility, index) = (None, -500, None)
    steps_count -= 1
    for child in state_children(state, '2'):
        (temp, utility, temp2) = minimize(child.state,steps_count)
        if utility > maxUtility:
            (maxChild, maxUtility, index) = (child.state, utility, child.index)

    return (maxChild, maxUtility, index)


def minimize(state,steps_count):
    if terminal_test(state):
        return (None, evaluate(state), None)
    if steps_count == 0:
        return (None, evaluate(state), None)

    (minChild, minUtility, index) = (None, 500, None)
    steps_count -= 1
    for child in state_children(state, '1'):
        (temp, utility, temp2) = maximize(child.state, steps_count)
        if utility < minUtility:
            (minChild, minUtility, index) = (child.state, utility, child.index)

    return (minChild, minUtility, index)


def decision(state):
    (child, temp, index) = maximize(state, 5)
    return (child, index)


def get_chip(column, j):
    word = split(column)
    return word[j]


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
        print(get_chip(state[0], j), '', get_chip(state[1], j), '', get_chip(state[2], j), '', get_chip(state[3], j), '',
              get_chip(state[4], j), '', get_chip(state[5], j), '', get_chip(state[6], j))


# game = Game()
# board = game.start()
# print_board(board)
# (board , index) = decisionwp(board)
# print_board(board)
# (board , index) = decisionwp(board)
# print_board(board)
# (board , index) = decisionwp(board)
# print_board(board)
