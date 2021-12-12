raw_data = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
def read_data(): 
    with open("input.txt") as f: 
        raw_data = f.read().strip()

    data = []
    for elem in raw_data.split("\n"): 
        start, end = elem.split(" -> ")
        #coords are reverse from how I interpret them, x is cols, y is rows
        start = [int(char)  for char in reversed(start.split(","))]
        end = [int(char) for char in reversed(end.split(","))]

        data.append((start, end))

    return data


def pt_1(): 

    data = read_data()
    vent_map = {}

    for start, end in data: 
        #horiz traversal
        if start[0] == end[0]: 
            for col in range(min(start[1], end[1]), max(start[1] +1,end[1]+1)): 
                row = start[0]
                if (row, col) in vent_map: 
                    vent_map[(row, col)] += 1 
                else: 
                    vent_map[(row, col)] = 1 
        #vertical trav
        elif start[1] == end[1]:
            for row in range(min(start[0], end[0]), max(start[0] +1,end[0]+1)): 
                    col = start[1]
                    if (row, col) in vent_map: 
                        vent_map[(row, col)] += 1 
                    else: 
                        vent_map[(row, col)] = 1 
    
    total = 0 
    for cord, occ in vent_map.items(): 
        if occ >= 2: 
            total += 1 

    print(f'Total: ', total)

def pt_2(): 

    data = read_data()
    vent_map = {}

    for start, end in data: 
        #horiz traversal
        if start[0] == end[0]: 
            for col in range(min(start[1], end[1]), max(start[1] +1,end[1]+1)): 
                row = start[0]
                if (row, col) in vent_map: 
                    vent_map[(row, col)] += 1 
                else: 
                    vent_map[(row, col)] = 1 
        #vertical trav
        elif start[1] == end[1]:
            for row in range(min(start[0], end[0]), max(start[0] +1,end[0]+1)): 
                    col = start[1]
                    if (row, col) in vent_map: 
                        vent_map[(row, col)] += 1 
                    else: 
                        vent_map[(row, col)] = 1 
        #diag travel 
        else: 
            row, col = start 
            while row != end[0] and col != end[1]: 
                if (row, col) in vent_map: 
                    vent_map[(row, col)] += 1 
                else: 
                    vent_map[(row, col)] = 1 

                if row - end[0] > 0: 
                    row -= 1 
                else: 
                    row += 1 

                if col - end[1] > 0: 
                    col -= 1 
                else: 
                    col += 1 

            if (end[0], end[1]) in vent_map: 
                vent_map[(end[0], end[1])] += 1 
            else: 
                vent_map[(end[0], end[1])] = 1 
                
                    
    
    #print(vent_map)
    total = 0 
    for cord, occ in vent_map.items(): 
        if occ >= 2: 
            total += 1 

    print(f'Total with diag: ', total)



if __name__ == "__main__": 
    pt_1()

    pt_2()
