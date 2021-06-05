#1 FOR EMPTY SPACE
#2 FOR RED CHIP
#3 FOR YELLOW CHIP

def state_children(state,val):
    children = []
    for i in range(0,7):
        for j in range(0,6):
            if get_chip(state[i],j) == 1:
                child = set_chip(state,i,j,val)
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


#
# def red_score(state):
#
# def yellow_score(state):

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
   #print(new_state)
   #print('\n')
   return new_state


state = [222211, 222211, 211111, 221111, 322221, 321111, 321111]

#state = ['000200','000000','000000','000000','000000','000000','000000']

list1 = state_children(state,3)
print(horizontal_count(state, 2))
print(vertical_count(state, 2))
for j in range(5,-1,-1):
    print(get_chip(state[0],j),get_chip(state[1],j),get_chip(state[2],j),get_chip(state[3],j),get_chip(state[4],j),get_chip(state[5],j),get_chip(state[6],j))




