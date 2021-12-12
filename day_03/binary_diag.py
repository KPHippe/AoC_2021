from copy import deepcopy
def read_data(): 
    with open('input.txt') as f: 
        data =  f.readlines() 
    return [elem.strip() for elem in data]

def pt_1(): 
    data = read_data() 
    gamma = []
    epsilon = []
    len_info = len(data[0])
    occurences = {i:0 for i in range(len_info)} 

    for elem in data: 
        for i, char in enumerate(elem): 
            if '1' in char : 
                occurences[i] += 1 

    for i, occ in occurences.items(): 
        if occ >= len(data)//2: 
            gamma.append("1")
            epsilon.append("0")
        else: 
            gamma.append("0")
            epsilon.append("1")
    
    power = int(''.join(gamma), 2) * int(''.join(epsilon), 2)

    return power 

def pt_2(): 
    data = read_data() 
        
    oxygen_data = deepcopy(data)
    co2_data = deepcopy(data)

    curbit = 0
    while len(oxygen_data) > 1: 

        zero_count, one_count = 0,0 
        for elem in oxygen_data: 
            if elem[curbit] == "1": 
                one_count += 1 
            elif elem[curbit] == "0": 
                zero_count += 1 
         
        most_common = "1" if one_count >= zero_count else  "0"
        to_del = []
        for elem in oxygen_data: 
            if elem[curbit ] != most_common: 
                to_del.append(elem)
        for elem in to_del: 
            oxygen_data.remove(elem)

        curbit += 1
    
    curbit = 0
    while len(co2_data) > 1: 

        zero_count, one_count = 0,0 
        for elem in co2_data: 
            if elem[curbit] == "1": 
                one_count += 1 
            elif elem[curbit] == "0": 
                zero_count += 1 
         
        least_common = "0" if zero_count <= one_count else  "1"
        to_del = []
        for elem in co2_data: 
            if elem[curbit ] != least_common: 
                to_del.append(elem)
        for elem in to_del: 
            co2_data.remove(elem)

        curbit += 1
    
    return int(''.join(oxygen_data), 2) * int(''.join(co2_data), 2)


if __name__ == "__main__": 
    print(f"{pt_1() = }") 
    
    print(f"{pt_2() = }")

