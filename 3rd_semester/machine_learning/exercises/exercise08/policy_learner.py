import numpy as np

# variables
gamma = 0.9
eta = 0.5

left_a = np.random.uniform(0,1, size = [4,5])
right_a = np.random.uniform(0,1, size = [4,5])
up_a = np.random.uniform(0,1, size = [4,5])
down_a = np.random.uniform(0,1, size = [4,5])
reward_a = np.zeros((4,5), dtype = 'int')
reward_a[0,4] = 100
direction_arr = np.empty([4,5], dtype = 'str')

best_directions = np.empty([4,5], dtype = 'int')
result_values = np.empty([4,5], dtype = 'float')

def check_for_action_values(x, y):
    """
    Given coordinates decide where agent can step and value for step is
    """
    values = []
    added_steps = []
    if y < 4:
        values.append(right_a[x,y])
        added_steps.append('r')
    if y > 0:
        values.append(left_a[x,y])
        added_steps.append('l')
    if x > 0:
        values.append(up_a[x,y])
        added_steps.append('u')
    if x < 3 :
        values.append(down_a[x,y])
        added_steps.append('d')
    return np.array(values), np.array(added_steps)

def make_step(x, y, direction, action_value):
    """
    Given coordinates and direction take step
    Update corresponding step array as it should be
    """
    if direction == 'l':
        action_values, directions = check_for_action_values(x, y - 1)
        reward = reward_a[x, y - 1]
        next_action_value = np.max(action_values)
        left_a[x,y] = action_value + eta *(reward + gamma * next_action_value - action_value) 
        print(f"we went left to coordinates {x}, {y - 1}")
        return x, y - 1

    elif direction == 'r':
        action_values, directions = check_for_action_values(x, y + 1)
        reward = reward_a[x, y + 1]
        next_action_value = np.max(action_values)
        right_a[x,y] = action_value + eta *(reward + gamma * next_action_value - action_value) 
        print(f"we went right to coordinates {x}, {y + 1}")
        return x, y + 1

    elif direction == 'u':
        action_values, directions = check_for_action_values(x - 1, y)
        reward = reward_a[x - 1, y]
        next_action_value = np.max(action_values)
        up_a[x,y] = action_value + eta *(reward + gamma * next_action_value - action_value) 
        print(f"we went up to coordinates {x - 1}, {y}")
        return x - 1, y

    else:
        action_values, directions = check_for_action_values(x + 1, y)
        reward = reward_a[x + 1, y]
        next_action_value = np.max(action_values)
        down_a[x,y] = action_value + eta *(reward + gamma * next_action_value - action_value) 
        print(f"we went down to coordinates {x + 1}, {y}")
        return x + 1, y

def best_actions():
    """
    For all possible position pick best step
    """
    left_a[:, 0] = 0
    right_a[:, -1] = 0
    up_a[0, :] = 0
    down_a[-1, :] = 0
    map_for_action = {'0': 'left', '1': 'right', '2': 'up', '3': 'down'}
    for x in range(0, 4):
        for y in range(0,5):
            result_values[x, y] = np.max(np.array([left_a[x,y], right_a[x,y], up_a[x,y], down_a[x,y]]))
            best_directions[x, y] = np.argmax(np.array([left_a[x,y], right_a[x,y], up_a[x,y], down_a[x,y]]))
    print(best_directions)
    print(result_values)


if __name__ == "__main__":
    step_count = 0
    
    for _epsilon in np.linspace(1, 0, 100):
        step_count += 1
        #pick random state
        x, y = np.random.randint(0,4), np.random.randint(0,5)

        # trying to make sure we start from original state as well
        if step_count % 20 == 0:
            x, y = 3, 0
            print(f"new epsilon: {_epsilon}") # just to keep track of epsilon every 20th occasion
        
        step_number = 0
        while True:
            step_number += 1
            if x == 0 and y == 4 or step_number >= 1000: # do not want to stay in maze forever
                break
            
            # look for possible steps and their values
            action_values, directions = check_for_action_values(x, y)
            best_action_value = np.max(action_values)
            best_action = directions[np.argmax(action_values)]
            print(f"{action_values}, {directions}")
            
            # depending on _epsilon we pick best action or random
            if np.random.uniform(0, 1) < _epsilon:
                action = np.random.choice(directions)
                print(f"random choice: {action}")
            else: 
                action = best_action
                print(f"best action: {action}")
            chosen_action_value = action_values[np.where(directions == action)[0][0]]

            # take step and return next indices
            x, y  = make_step(x, y, action, chosen_action_value)
    
    # once done print best action array and all action values
    best_actions()
    print(f"left_a\n: {left_a}")
    print(f"right_a\n: {right_a}")
    print(f"up_a\n: {up_a}")
    print(f"down_a\n: {down_a}")
