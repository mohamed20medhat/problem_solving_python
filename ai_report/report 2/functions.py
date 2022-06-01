import random

def print_puzzle(puzzle):
    s = ""
    for cell in puzzle:
        if cell != 0:
            s += str(cell)
        else:
            s += ' '

    # don't forget to add '+' after each line in the print. or it will print them sepreatly.
    # notice the space location in each string with '|'. used to create the grid
    print(
        '-'*13 + '\n' +
        '| ' + s[0] + ' | ' + s[1] + ' | ' + s[2] + ' |' + '\n' +
        '-'*13 + '\n' +
        '| ' + s[3] + ' | ' + s[4] + ' | ' + s[5] + ' |' + '\n' +
        '-'*13 + '\n'
        '| ' + s[6] + ' | ' + s[7] + ' | ' + s[8] + ' |' + '\n' +
        '-'*13 + '\n'
    )



def get_empty(puzzle):  # returns the index of the empty place
    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            return i


def possible_actions(puzzle):
    empty = get_empty(puzzle)
    actions = []
    if empty not in [0, 1, 2]:
        actions.append('^')  # > 2 || mot in the first row
    if empty not in [6, 7, 8]:
        actions.append('v')  # < 6 || not in the last row
    if empty not in [2, 5, 8]:
        actions.append('>')  # %3==2 || not in the last column
    if empty not in [0, 3, 6]:
        actions.append('<')  # %3==0 || not in the first column
    return actions


def apply_action(old_puzzle, action):
    # copying the actual data to another place in memory. insted of copying the pointer to it
    puzzle = old_puzzle[:]
    empty = get_empty(puzzle)
    if action == '>':  # move to the right. switch the item with the item next to it
        puzzle[empty], puzzle[empty+1] = puzzle[empty+1], puzzle[empty]
    if action == '<':  # move to the left. switch the item with the item before it
        puzzle[empty], puzzle[empty-1] = puzzle[empty-1], puzzle[empty]
    if action == '^':  # move up. switch the item with the item before it by 3
        puzzle[empty], puzzle[empty-3] = puzzle[empty-3], puzzle[empty]
    if action == 'v':  # move down. switch the item with the item after it by 3
        puzzle[empty], puzzle[empty+3] = puzzle[empty+3], puzzle[empty]
    return puzzle


def check_puzzle(puzzle):
    # notice that each item contains a number. -> the right solution to the puzzle is that. the numbers are sorted in there places and they look exactly like thier indcies. so. the number inside the item should equal it's index
    for i in range(len(puzzle)):
        if puzzle[i] != i:
            return False  # if the number is in it's index. then it's correctyly solved
    return True  # if the number is it's index. then return true


# takes the number of actions. and apply them randomly to the puzzle.
def shuffle(n):
    puzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # the actions that the shuffle take are not completly random. it must follow the game rulles during the shuffling process. that's why we will need to use generate actions. to know the avilable actions after each change => then we select one of the avilable actions randomly using the random module
    for _ in range(n):
        actions = possible_actions(puzzle)
        # the avilable actions comes in an array of options. that i want to choose one from it. but the array of avilable actions size changes. cause not all the actions are avilable "i can't go out of the boarder of the game" => that's why i get the length of the array of the avilable actions each time i want to take a step. and choose a number between 0 and the length of the avilable actions
        # len => returns the actual size of the array. => max_index + 1.
        random_index = random.randint(0, len(actions)-1)
        puzzle = apply_action(puzzle, actions[random_index])
    return puzzle


#! there is a bug. that if the random index made the initial puzzle already solved. then i need to find a way to cheack if it was solved before giving it to the human to solve it
def check_shuffled(n):
    # cheack if it's already solved. and keep shuffling till it get's a not alrady solved
    already_solved = True
    while already_solved == True:
        shuffled_puzzle = shuffle(n)
        if check_puzzle(shuffled_puzzle) == False:
            already_solved = False
            return shuffled_puzzle



def puzzle_cost(puzzle, action):
    # every action's cost is equal == 1 
    return 1 



