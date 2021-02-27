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
        for i,section in enumerate(self.ground_list):
            for j,section2 in enumerate(self.ground_list):
                if(section==[]):
                    pass
                elif(section2==[]):
                    valid.append([i, j])
                elif(section[-1].number<section2[-1].number):
                    valid.append([i, j])
                else:
                    pass
        return valid

    def action(self, valid):
        temp=self.ground_list[valid[0]].pop()
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

#define the final state
def goal_test(s):
    for i in s.ground_list:
        if len(i) != 0:
            temp_color = i[0].color
            temp_number = i[0].number
            for j in i:
                if j.color != temp_color or j.number > temp_number:
                    return False
        else: pass
    return True


#search
def breadth_first_search(gameState):
    if goal_test(gameState):
        return gameState
    frontier = [gameState]
    explored = []
    while(1):
        if(len(frontier) == 0):
            return False
        else:
            node = frontier.pop(0)
            explored.append(node)
            for a in node.valid_actions():
                child = node.child_node(a)
                isinfrontier = False
                isinexplored = False
                #check if node is in frontire or not
                for element in frontier:
                    list1 = element.ground_list
                    list2 = child.ground_list
                    flag1 = False
                    for i in range(len(list1)):
                        #chek if list1[i]=list2[i]
                        if(len(list1[i])==len(list2[i])):
                            for j in range(len(list1[i])):
                                if list1[i][j].number!=list2[i][j].number or list1[i][j].color!=list2[i][j].color:
                                    flag1 = True
                        else:
                            #they are not equal
                            flag1 = True
                    if(flag1 == False):
                        isinfrontier = True

                    # check if node is in frontire or not
                for element in explored:
                    list1 = element.ground_list
                    list2 = child.ground_list
                    flag1 = False
                    for i in range(len(list1)):
                        # chek if list1[i]=list2[i]
                        if (len(list1[i]) == len(list2[i])):
                            for j in range(len(list1[i])):
                                if list1[i][j].number != list2[i][j].number or list1[i][j].color != list2[i][j].color:
                                    flag1 = True
                        else:
                            # they are not equal
                            flag1 = True
                    if (flag1 == False):
                        isinexplored = True

                if isinexplored == False and isinfrontier == False:
                    if goal_test(child):
                        global total_node
                        global expanded_node
                        total_node = len(frontier) + len(explored)
                        expanded_node = len(explored)
                        return child
                    frontier.append(child)







#get the initial state
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
            listOfCards.append(card(myinput[j][0:len(myinput[j])-1], myinput[j][-1]))

    grounds.append(listOfCards)
    listOfCards=[]
mygame = game(grounds)

res = breadth_first_search(mygame)
if res != False:
    print("Toral node: ")
    print(total_node)
    print("Expanded node: ")
    print(expanded_node)
    print("Number of actions: ")
    listac = action_list(res)
    print(len(listac))
    print("Actions: ")
    for action in reversed(listac):
        print("From " + str(action[0]) + " To " + str(action[1]))
    print("Solution:")
    for g in res.ground_list:
        for c in g:
            print(str(c.number) + c.color, end=" ")
        print("")
else: print("Failure")