#1 FOR EMPTY SPACE
#2 FOR RED CHIP
#3 FOR YELLOW CHIP
#j is row
#i is column
def state_children(state, val):
    children = []
    for i in range(0,7):
        for j in range(0,6):
            if get_chip(state[i],j) == 1:
                child = set_chip(state, i, j, val)
                children.append(child)
                break
    return children

def detect_four_vertically(column, val):
        k = 4
        for j in range(0,6):
            if get_chip(column,j) == val:
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


def detect_four_horizontally(state,row,val):
    k = 4
    for i in range(0, 7):
        if get_chip(state[i],row) == val:
            k -= 1
            if k == 0:
                return 1
        else:
            k = 4

def horizontal_count(state, val):
    count = 0
    for j in range(0,6):
        if detect_four_horizontally(state, j, val):
            count += 1
    return count


def detectDiagonalLtoR(state,val):
    k=l=m=n=o=p=4
    count = 0
    for i in range(0, 6):
        if get_chip(state[i],i) == val:
            k -= 1
            if k == 0:
                count +=1
    for i in range(1,7):
        if get_chip(state[i],i+1) == val:
            l-=1
            if l==0 :
                count +=1
    for i in range(2,7):
        if get_chip(state[i],i+1) == val:
            m-=1
            if m==0 :
                count +=1
    for i in range(3,7):
        if get_chip(state[i],i+1) == val:
            n-=1
            if n==0 :
                count +=1
    for i in range(0,4):
        if get_chip(state[i+1],i) == val:
            o-=1
            if o==0 :
                count +=1
    for i in range(0,3):
        if get_chip(state[i+2],i) == val:
            p-=1
            if p==0 :
                count +=1
    return count

def detectDiagonalRtoL(state,val):
    k=l=m=n=o=p=4
    count = 0
    for i in range(5, 0,-1):
        if get_chip(state[i],i) == val:
            k -= 1
            if k == 0:
                count +=1
    for i in range(6,1,-1):
        if get_chip(state[i],i+1) == val:
            l-=1
            if l==0 :
                count +=1
    for i in range(6,2,-1):
        if get_chip(state[i],i+1) == val:
            m-=1
            if m==0 :
                count +=1
    for i in range(6,3,-1):
        if get_chip(state[i],i+1) == val:
            n-=1
            if n==0 :
                count +=1
    for i in range(3,0,-1):
        if get_chip(state[i+1],i) == val:
            o-=1
            if o==0 :
                count +=1
    for i in range(3,0,-1):
        if get_chip(state[i+2],i) == val:
            p-=1
            if p==0 :
                count +=1
    return count



def red_score(state):
    return horizontal_count(state, 2) + vertical_count(state, 2) + detectDiagonalLtoR(state, 2) + detectDiagonalRtoL(state,2)


def yellow_score(state):
    return horizontal_count(state, 3) + vertical_count(state, 3) + detectDiagonalLtoR(state, 3) + detectDiagonalRtoL(state,3)

def evaluate(state):
    return red_score(state)-yellow_score(state)

def terminal_test(state):
    for i in range(0, 7):
        for j in range(0, 6):
            if get_chip(state[i], j) == 1:
                return 0
    return 1

def maximize(state):
    if terminal_test(state):
        return (None, evaluate(state))
    (maxChild, maxUtility) = (None, -500)
    for child in state_children(state,2):
        (temp, utility) = minimize(child)
        if utility > maxUtility:
            (maxChild,maxUility) = (child, utility)

    return (maxChild, maxUtility)

def minimize(state):
    if terminal_test(state):
        return (None, evaluate(state))
    (minChild, minUtility) = (None, 500)
    for child in state_children(state,3):
        (temp, utility) = maximize(child)
        if utility < minUtility:
            (minChild, minUility) = (child, utility)

    return (minChild, minUtility)

def decision(state):
    (child,temp) = maximize(state)
    return child

def get_chip(column, j):
    return int(column/(10**(5-j))%10)

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

def set_chip(state, i , j, val):
   new_state = state.copy()
   x = split(str(new_state[i]))
   x[j] = str(val)
   new_state[i] = int(listToString(x))
   return new_state

def print_board(state):
    for j in range(5, -1, -1):
        print(get_chip(state[0], j), get_chip(state[1], j), get_chip(state[2], j), get_chip(state[3], j),
              get_chip(state[4], j), get_chip(state[5], j), get_chip(state[6], j))

state = [222221, 222231, 232331, 223211, 322221, 322331, 323231]

#state = ['000200','000000','000000','000000','000000','000000','000000']

list1 = state_children(state,3)
print(red_score(state))
print(yellow_score(state))

print_board(state)
print('\n')
state = decision(state)
print_board(state)
print('\n')
state = decision(state)
print_board(state)
print('\n')
state = decision(state)
print_board(state)
print('\n')
state = decision(state)
print_board(state)
print('\n')
state = decision(state)
print_board(state)
print('\n')
state = decision(state)
print_board(state)
print('\n')
state = decision(state)
print_board(state)
print('\n')
state = decision(state)
print_board(state)
print('\n')
print(red_score(state))
print(yellow_score(state))

