def read_data(): 
    data = """\
3,4,3,1,2"""
    
    with open('input.txt') as f: 
        data = f.read() 

    return [int(elem) for elem in data.strip().split(',') ]


def solve(target_day): 
    data = read_data() 

    fish_dict = {i:0 for i in range(9)}
    
    for timer in data: 
        fish_dict[timer] += 1 

    for day in range(target_day):
        reproductively_viable = fish_dict[0]

        for i in range(0, 8): 
            fish_dict[i] =  fish_dict[i+1]

        fish_dict[8]= reproductively_viable 
        fish_dict[6] += reproductively_viable
    
    return sum(fish_dict.values())
    
if __name__ == "__main__": 
    print(f"Part one: {solve(80)}")
    print(f"Part two: {solve(256)}")
    
