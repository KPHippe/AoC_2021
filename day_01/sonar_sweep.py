def read_data(): 
    with open('input.txt') as f: 
        data = f.read()

    data = [int(elem.strip()) for elem in data.split()] 
    return data 

def pt_1(): 
    increasing = 0 

    prev = data[0]
    for elem in data[1:]:
        if elem > prev: 
            increasing += 1

        prev = elem 

    return increasing

def pt_2(): 
    increasing = 0 

    orig_window = sum(data[:2])
    for i in range(len(data[1:-2])): 
        new_window = sum(data[i:i+3])

        if new_window > orig_window : 
            increasing += 1

        orig_window = new_window
    
    return increasing


if __name__ == "__main__":
    data = read_data()
    print(f"Strictly increasing: {pt_1()}")

    print(f"Window increasing: {pt_2()}")
