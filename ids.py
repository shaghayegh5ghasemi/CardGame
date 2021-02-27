import copy


#info
total_node = 0
expanded_node = 0

class game:
    def __init__(self, ground_list):
        self.ground_list = ground_list
        self.parent = "-"

    def valid_actions(self):
        valid = []
        for i, section in enumerate(self.ground_list):
            for j, section2 in enumerate(self.ground_list):
                if (section == []):
                    pass
                elif (section2 == []):
                    valid.append([i, j])
                elif (section[-1].number < section2[-1].number):
                    valid.append([i, j])
                else:
                    pass
        return valid

    def action(self, valid):
        temp = self.ground_list[valid[0]].pop()
        self.ground_list[valid[1]].append(temp)

    def child_node(self, a):
        child = copy.deepcopy(self)
        child.parent = self
        child.action(a)
        child.myaction = a
        return child


class card:
    def __init__(self, number, color):
        self.color = color
        self.number = int(number)

    def __str__(self):
        return str(self.color + "  " + str(self.number))

#calculate depth and the actions that has been done to achieve the state
def action_list(finalState):
    temp = finalState
    listOfActions = []
    while(temp.parent != "-"):
        listOfActions.append(temp.myaction)
        temp = temp.parent
    return listOfActions

# define the final state
def goal_test(s):
    for i in s.ground_list:
        if len(i) != 0:
            temp_color = i[0].color
            temp_number = i[0].number
            for j in i:
                if j.color != temp_color or j.number > temp_number:
                    return False
        else:
            pass
    return True


# search

#return: result or 0 as cutoff or 1 as failure
def recursive_dls(node_state, limit):
    global total_node
    global expanded_node
    if goal_test(node_state):
        return node_state
    else:
        if limit == 0:
            return 0
        else:
            cutoff_occured = False
            for a in node_state.valid_actions():
                child = node_state.child_node(a)
                total_node = total_node + 1
                result = recursive_dls(child, limit - 1)
                if result == 0:
                    cutoff_occured = True
                else:
                    if result != 1:
                        return result
            expanded_node = expanded_node + 1
            if cutoff_occured: return 0
            else: return 1


def depth_limited_serch(node_state, limit):
    return recursive_dls(node_state, limit)

def iterative_deepening_search(gameSate, depth):
    while(1):
        result = depth_limited_serch(gameSate, depth)
        depth = depth + 1
        if result != 0:
            return result



# get the initial state
k, m, n = input("").split(' ')
myinput = []
grounds = []
listOfCards = []
for i in range(int(k)):
    myinput = input("").split(' ')
    for j in range(len(myinput)):
        if myinput[0] == "#":
            listOfCards = []
        else:
            listOfCards.append(card(myinput[j][0:len(myinput[j]) - 1], myinput[j][-1]))

    grounds.append(listOfCards)
    listOfCards = []

depth = input()
mygame = game(grounds)

res = iterative_deepening_search(mygame, int(depth))
if res != 1:
    print("Total node: ")
    print(total_node)
    print("Expanded node:")
    print(expanded_node)
    print("Number of actions: ")
    listac = action_list(res)
    print(len(listac))
    print("Actions: ")
    for action in reversed(listac):
        print("From " + str(action[0]) + " To " + str(action[1]))
    print("Solution: ")
    for g in res.ground_list:
        for c in g:
            print(str(c.number) + c.color, end=" ")
        print("")
else:
    print("Failure")