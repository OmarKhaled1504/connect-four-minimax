#1 FOR EMPTY SPACE
#2 FOR RED CHIP
#3 FOR YELLOW CHIP

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
    return horizontal_count(state, 2) + vertical_count(state, 2) + diagonal_count(state, 2)


def yellow_score(state):
    return horizontal_count(state, 3) + vertical_count(state, 3) + diagonal_count(state, 3)


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


state = [222221, 222211, 232111, 221111, 322221, 322111, 323211]

#state = ['000200','000000','000000','000000','000000','000000','000000']

list1 = state_children(state,3)
print(red_score(state))
print(yellow_score(state))
#print(horizontal_count(state, 2))
#print(vertical_count(state, 2))
for j in range(5,-1,-1):
    print(get_chip(state[0],j),get_chip(state[1],j),get_chip(state[2],j),get_chip(state[3],j),get_chip(state[4],j),get_chip(state[5],j),get_chip(state[6],j))




