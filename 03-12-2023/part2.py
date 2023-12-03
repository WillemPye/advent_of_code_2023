import sys
import argparse
import numpy as np

def get_co_to_check(ndigs, i, j, gridsize):
    max_i = gridsize[0]-1
    max_j = gridsize[1]-1
    co_ords = []
    #Add co-ords to left of first digit
    if j > 0:
        co_ords.append((i,j-1))
        if i > 0:
            co_ords.append((i-1,j-1))
        if i < max_i:
            co_ords.append((i+1,j-1))
    
    #For each digit add co-ords above and below
    for _ in range(ndigs):
        if i > 0:
            co_ords.append((i-1, j+_))
        if i < max_i:
            co_ords.append((i+1, j+_))
    
    #Add co-ords to right of last digit
    if j + ndigs < max_j:
        co_ords.append((i,j+ndigs))
        if i > 0:
            co_ords.append((i-1,j+ndigs))
        if i < max_i:
            co_ords.append((i+1,j+ndigs))

    return co_ords
        

def main():

    parser = argparse.ArgumentParser(description="Day 3 part 2 solver")
    parser.add_argument("--input", required=False, default="input.txt", help="Day 3 input as txt file, default of input.txt")
    args = parser.parse_args()
    input_path = args.input
    
    try:
        with open(input_path, "r") as f:
            lines = f.readlines()
        grid = np.array([list(line.strip("\n")) for line in lines])
        with open(input_path, "r") as f:
            text = f.read()
    except FileNotFoundError as e:
        print("Input file not found")
        sys.exit(1)
    
    gridsize = grid.shape
    stars = {}
    #i is row, j is col
    for i in range(gridsize[0]):
        for j in range(gridsize[1]):
            if grid[i,j].isdigit():

                #if item to left is also a number skip
                if j != 0 and grid[i,j-1].isdigit():
                    continue
                
                #Get chain of digits to left
                digs = []
                cnt = 0
                while j + cnt <140 and grid[i,j+cnt].isdigit():
                    digs.append(grid[i,j+cnt])
                    cnt += 1
                
                ndigs = len(digs)
                num = int("".join(digs))

                #Get list of co-ords to check for symbols
                co_ords = get_co_to_check(ndigs, i, j, gridsize)

                #Check symbol adjency
                for co_ord in co_ords:
                    if grid[co_ord[0],co_ord[1]] == "*":
                        if co_ord in stars:
                            stars[co_ord].append(num) 
                        else:
                            stars[co_ord] = [num]
                
    values = []
    for value in stars.values():
        if len(value) == 2:
            val = value[0]*value[1]
            values.append(val)
                
    total = sum(values)
    output = total
    return output


if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)