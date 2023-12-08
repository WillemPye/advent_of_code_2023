import sys
import argparse
import math

def product(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] * product(numbers[1:])

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def recursive_lcm(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return lcm(numbers[0], recursive_lcm(numbers[1:]))
def main():

    parser = argparse.ArgumentParser(description="Day 8 part 1 solver")
    parser.add_argument("--input", required=False, default="input.txt", help="Day 8 input as txt file, default of input.txt")
    args = parser.parse_args()
    input_path = args.input
    
    try:
        with open(input_path, "r") as f:
            text = f.read()
    except FileNotFoundError as e:
        print("Input file not found")
        sys.exit(1)
    
    directions, nodes = text.split("\n\n")
    nodes = nodes.strip("\n").split("\n")
    map_ = {}
    for node in nodes:
        cur, next = node.split(" = ")
        next = tuple(next.strip("()").split(", "))
        map_[cur] = next
    
    A_nodes = []
    for key in map_.keys():
        if key[-1] == "A":
            A_nodes.append(key)
    print(A_nodes)

    lr_to_idx = {"L":0, "R":1}
    directions = [lr_to_idx[letter] for letter in directions]
    l_dir = len(directions)
    
    first_Zs = []
    for A_node in A_nodes:
        node = A_node
        cnt = 0
        while cnt<1000000:
            direction = directions[cnt%l_dir]
            cnt+=1
            node = map_[node][direction]
            if node[-1]=="Z":
                print(cnt,node)
                first_Z = cnt
                break
        first_Zs.append(first_Z)
    print(first_Zs)
    [print(z%l_dir) for z in first_Zs]
    print(product(first_Zs))
    print(recursive_lcm(first_Zs))
        

if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)

