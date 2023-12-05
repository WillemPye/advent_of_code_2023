import sys
import argparse
import numpy as np

def make_map(ranges):
    def _map(source):
        for r in ranges:
            dr, sr, l = r
            diff = source - int(sr)
            if diff >= 0 and diff < int(l):
                destination = int(dr) + diff
                return destination
        
        destination = source
        return destination
    return _map
        

def main():

    parser = argparse.ArgumentParser(description="Day 5 part 1 solver")
    parser.add_argument("--input", required=False, default="input.txt", help="Day 5 input as txt file, default of input.txt")
    args = parser.parse_args()
    input_path = args.input
    
    with open(input_path, "r") as f:
        input_text = f.read()
    
    categories = input_text.split("\n\n")

    
    seeds = categories[0].split(":")[1].strip("\n ").split(" ")
    print(f"Seeds: {seeds}")
    
    maps = {k[:-4]: np.array([item.split(" ") for item in v.strip("\n").split("\n")]) for cat in categories[1:] for k, v in [cat.split(":")]}
    
    map_funcs = {}
    for k, v in maps.items():
        map_funcs[k] = make_map(v)
    
    locations = []
    for seed in seeds:
        trace = int(seed)
        for v in map_funcs.values():
            trace = (v(trace))
        print(trace)
        locations.append(trace)
    
    output = min(locations)
    return output
    

if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)
