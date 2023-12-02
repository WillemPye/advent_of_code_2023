import sys
import argparse
import numpy as np

def max_(l):
    if len(l) == 0:
        return 0
    else:
        return int(max(l))

def get_rgb(subgame):
    subgame = subgame.split(",")
    items = [item.strip(" \n").split(" ") for item in subgame]

    rgb = {"red": [], "green": [], "blue": [],}
    for item in items:
        try:
            rgb[item[1]].append(item[0])
        except KeyError as e:
            print(f"KeyError: {e}")
    
    rgb = [max_(rgb["red"]), max_(rgb["green"]), max_(rgb["blue"])]
    return rgb

def parse_line(line):
    line = line.split(":",1)

    id = int(line[0].split(" ")[1])

    subgames = line[1].split(";")

    rgb_arr = []
    [rgb_arr.append(get_rgb(subgame)) for subgame in subgames]
    rgb_arr = np.array(rgb_arr)

    rgb = [rgb_arr[:,i].max() for i in range(3)]
    
    info = {"Game id": id, "red": rgb[0], "green": rgb[1], "blue": rgb[2]}
    return info

def main():

    parser = argparse.ArgumentParser(description="Day 2 part 2 solver")
    parser.add_argument("--input", required=False, default="input.txt", help="Day 2 input as txt file, default of input.txt")
    args = parser.parse_args()
    input_path = args.input
    
    try:
        with open(input_path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError as e:
        print("Input file not found")
        sys.exit(0)
    
    games_info = [parse_line(line) for line in lines if line != ""]

    running_total = 0
    for game in games_info:
        r = game["red"]
        g = game["green"]
        b = game["blue"]
        rgb = r*g*b
        running_total += rgb
    
    output = running_total
    return output

if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)
