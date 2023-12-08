import sys
import argparse

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

    lr_to_idx = {"L":0, "R":1}
    directions = [lr_to_idx[letter] for letter in directions]
    
    count = 0
    node = "AAA"
    while True:
        for direction in directions:
            count+=1
            node = map_[node][direction]
            if node == "ZZZ":
                return count
            

if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)
