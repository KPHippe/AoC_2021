import numpy as np
def read_data(): 
    data = """\
16,1,2,0,4,2,7,1,2,14"""

    
    with open('input.txt') as f: 
        data = f.read()

    return [int(elem) for elem in data.strip().split(",")]


def pt_1(): 
    data = read_data() 
    
    start, end = min(data), max(data)

    res_mat = []
    for pos in data: 
        consumption_ranges = []

        for target_pos in range(start, end+1 ): 
            fuel = abs(pos - target_pos) 
            consumption_ranges.append(fuel)

        res_mat.append(consumption_ranges) 

    res_mat = np.array(res_mat) 
    
    sum_mat = np.sum(res_mat, axis=0) 
    

    res = np.argmin(sum_mat) 
    print(res)
    print(sum_mat[res])

def pt_2(): 
    data = read_data() 
    
    start, end = min(data), max(data)

    res_mat = []
    for pos in data: 
        consumption_ranges = []

        for target_pos in range(start, end+1 ): 
            delta = abs(pos - target_pos) 
            fuel  = (delta* (delta +1))//2
            consumption_ranges.append(fuel)

        res_mat.append(consumption_ranges) 

    res_mat = np.array(res_mat) 
    
    sum_mat = np.sum(res_mat, axis=0) 
    

    res = np.argmin(sum_mat) 
    print(res)
    print(sum_mat[res])



if __name__ == "__main__": 
    pt_1()
    pt_2()
