def read_input(): 
    with open('input.txt') as f: 
        data = f.readlines()

    return data


def pt_1(data): 
    pos = {'horiz': 0, 'vert': 0}
    
    for instruction in data: 
        instruction = instruction.split()
        
        if 'forward' in instruction[0]: 
            pos['horiz'] += int(instruction[1])
        elif 'down' in instruction[0]: 
            #reverse of what we expect by problem instruction 
            pos['vert'] += int(instruction[1])
        else: #  'up' instruction 
            #reverse of what we expect by problem instruction
            pos['vert'] -= int(instruction[1])
    
    return pos['vert'] * pos['horiz']

def pt_2(data):
    pos = {'horiz': 0, 'vert': 0, 'aim': 0}
    
    for instruction in data: 
        instruction = instruction.split()
        command, val = instruction[0], int(instruction[1])
        if 'forward' in command: 
            pos['horiz'] += val
            pos['vert'] += val * pos['aim']
        elif 'down' in command: #only changes aim 
            #reverse of what we expect by problem instruction 
            pos['aim'] += val
        else: #  'up' instruction, only changes aim this time
            #reverse of what we expect by problem instruction
            pos['aim'] -= val 
    
    return pos['vert'] * pos['horiz']


if __name__ == "__main__": 
    data = read_input()
    
    print(f"Pt1: {pt_1(data)}")

    print(f"Pt2: {pt_2(data)}")
