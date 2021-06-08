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

def diagonal_count(state, val):
    count = 0
    for k in range(0,6+7-2+1):
        fourinrow = 4
        for j in range(0,k+1):
            i = k - j
            if i<6 and j<7:
                if get_chip(state[j], i) == val:
                    #print(get_chip(state[j],i))
                    fourinrow -= 1
                    if fourinrow == 0:
                        count += 1
                else:
                    fourinrow = 4

    # for k in range(0,12):
    #     fourinrow = 4
    #     for i in range(0,k+1):
    #         j = 6 + i
    #         if i > -1 and j < 7:
    #             print(i, j)
    #             if get_chip(state[j], i) == val:
    #                 #print(get_chip(state[j],i))
    #
    #                 fourinrow -= 1
    #                 if fourinrow == 0:
    #                     count += 1
    #             else:
    #                 fourinrow = 4
    #     print('\n')
    return count

def red_score(state):
    return horizontal_count(state, '1') + vertical_count(state, '1') + diagonal_count(state,'1')



def yellow_score(state):
    return horizontal_count(state, '2') + vertical_count(state, '2') + diagonal_count(state, '2')


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

    (child, temp, index) = maximizewp(state, -math.inf, math.inf, 7)
    return (child, index)


def minimizewp(state, alpha, beta, steps_count):
    if terminal_test(state):
        return (None, evaluate(state),None)
    if steps_count == 0:
        return (None, evaluate(state),None)
    (minChild, minUtility, index) = (None, 500, None)
    steps_count -= 1

    for child in state_children(state, '2'):
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
        return (None, evaluate(state), None)

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
#########################################################

def maximize(state, steps_count):
    if terminal_test(state):
        return (None, evaluate(state))
    if steps_count == 0:
        return (None, evaluate(state))

    (maxChild, maxUtility) = (None, -500)
    steps_count -= 1
    for child in state_children(state, '2'):
        (temp, utility) = minimize(child,steps_count)
        if utility > maxUtility:
            (maxChild, maxUtility) = (child, utility)

    return (maxChild, maxUtility)


def minimize(state,steps_count):
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
#
# while not terminal_test(board):
#     print('\nENTER YOUR MOVE\n')
#     j = int(input('ROW: '))
#     i = int(input('\nCOLUMN: '))
#     board = set_chip(board, i, j, '1')
#     print("YOUR MOVE")
#     print_board(board)
#     (board, index) = decisionwp(board)
#     print(index)
#     print("\nBOTS'S MOVE")
#     print_board(board)





# state = ['121212', '122222', '120000', '100000', '120000', '100000', '111000']
# (children, indices) = state_children(state, '1')





