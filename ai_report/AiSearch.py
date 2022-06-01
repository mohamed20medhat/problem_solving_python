

def dfs(initial_state, get_actions, get_state, isgoal):
    fringe = []
    visited = []
    fringe.append({
        'state': initial_state,
        'path': []
    })

    while len(fringe) > 0:
        current_node = fringe.pop()
        if current_node['state'] in visited:
            continue
        visited.append(current_node['state'])
        print(current_node)
        if isgoal(current_node['state']):
            return current_node['path'], len(visited)
        possible_actions = get_actions(current_node['state'])

        for action in possible_actions:
            next_node = {}
            next_node['state'] = get_state(current_node['state'], action)
            next_node['path'] = current_node['path'][:]
            next_node['path'].append(action)
            fringe.append(next_node)
    return 'failure'


def bfs(initial_state, get_actions, get_state, isgoal):
    fringe = []
    visited = []
    fringe.append({
        'state': initial_state,
        'path': []
    })

    while len(fringe) > 0:
        current_node = fringe.pop(0)
        if current_node['state'] in visited:
            continue
        visited.append(current_node['state'])
        print(current_node)
        if isgoal(current_node['state']):
            return current_node['path'], len(visited)
        possible_actions = get_actions(current_node['state'])

        for action in possible_actions:
            next_node = {}
            next_node['state'] = get_state(current_node['state'], action)
            next_node['path'] = current_node['path'][:]
            next_node['path'].append(action)
            fringe.append(next_node)
    return 'failure'


def ucs(initial_state, get_actions, get_state, is_goal, compute_cost, get_min):
    fringe = []
    visited = []
    inital_node = {}
    inital_node['state'] = initial_state
    inital_node['path'] = []
    inital_node['cost'] = 0
    fringe.append(inital_node)
    while len(fringe) > 0:
        current_node = fringe.pop(get_min(fringe, 'cost'))
        if current_node['state'] in visited:
            continue
        visited.append(current_node['state'])
        print(current_node)
        if is_goal(current_node['state']):
            solution = {}
            solution['solution'] = current_node['path']
            solution['cost'] = current_node['cost']
            solution['expanded_nodes'] = len(visited)
            return solution
        possible_actions = get_actions(current_node['state'])
        for action in possible_actions:
            next_state = get_state(current_node['state'], action)
            next_node = {}
            next_node['state'] = next_state
            next_node['path'] = current_node['path'][:]
            next_node['path'].append(action)
            next_node['cost'] = current_node['cost'] + \
                compute_cost(current_node['state'], action)
            fringe.append(next_node)
    return 'failure'


#! haven't made the heuristic function yet
def greedy(initial_state, get_actions, get_state, is_goal, get_min, heuristic):
    fringe = []
    visited = []
    inital_node = {}
    inital_node['state'] = initial_state
    inital_node['path'] = []
    # inital_node['h'] = heuristic(inital_node['state']) # no need to calculte the heurisitic function for it. cause it will get out of the fringe in the first iteration cause it's the inital node => it won't be compared to any other value. cause thier ain't another value
    inital_node['h'] = 0
    fringe.append(inital_node)
    while len(fringe) > 0:
        current_node = fringe.pop(get_min(fringe, 'h'))
        if current_node['state'] in visited:
            continue
        visited.append(current_node['state'])
        print(current_node)
        if is_goal(current_node['state']):
            solution = {}
            solution['solution'] = current_node['path']
            # no need to add h cause h = 0
            solution['expanded_nodes'] = len(visited)
            return solution
        possible_actions = get_actions(current_node['state'])
        for action in possible_actions:
            next_state = get_state(current_node['state'], action)
            next_node = {}
            next_node['state'] = next_state
            next_node['path'] = current_node['path'][:]
            next_node['path'].append(action)
            next_node['h'] = heuristic(next_state)
            fringe.append(next_node)
    return 'failure'


def astar(initial_state, get_actions, get_state, is_goal, compute_cost,heuristic):
    fringe = []
    visited = []
    inital_node = {}
    inital_node['state'] = initial_state
    inital_node['path'] = []
    inital_node['cost'] = 0
    # inital_node['f'] = inital_node['cost'] + inital_node['h']
    inital_node['f'] = 0
    
    fringe.append(inital_node)
    while len(fringe) > 0:
        current_node = fringe.pop(get_min(fringe, 'f'))
        if current_node['state'] in visited:
            continue
        visited.append(current_node['state'])
        print(current_node)
        if is_goal(current_node['state']):
            solution = {}
            solution['solution'] = current_node['path']
            solution['cost'] = current_node['cost']
            solution['expanded_nodes'] = len(visited)
            return solution
        possible_actions = get_actions(current_node['state'])
        for action in possible_actions:
            next_state = get_state(current_node['state'], action)
            next_node = {}
            next_node['state'] = next_state
            next_node['path'] = current_node['path'][:]; next_node['path'].append(action)
            next_node['cost'] = current_node['cost'] + compute_cost(current_node['state'], action) 
            # instead of storing h in the node. i can compute it and add it to the f directly
            next_node['f'] = next_node['cost'] + heuristic(next_node['state'])
            fringe.append(next_node)
    return 'failure'



def get_min(fringe, key):
    Min = 0
    for i in range(1, len(fringe)):
        if fringe[i][key] < fringe[Min][key]:
            Min = i
    return Min












