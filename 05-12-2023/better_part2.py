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

    parser = argparse.ArgumentParser(description="Day 5 part 2 solver")
    parser.add_argument("--input", required=False, default="input.txt", help="Day 5 input as txt file, default of input.txt")
    args = parser.parse_args()
    input_path = args.input
    
    with open(input_path, "r") as f:
        input_text = f.read()
    
    categories = input_text.split("\n\n")

    
    seed_ranges = categories[0].split(":")[1].strip("\n ").split(" ")
    print(f"Seed ranges: {seed_ranges}")
    
    maps = {k[:-4]: np.array([[int(i) for i in item.split(" ")] for item in v.strip("\n").split("\n")]) for cat in categories[1:] for k, v in [cat.split(":")]}
    print(maps)
    
    map_funcs = {}
    for k, v in maps.items():
        map_funcs[k] = make_map(v)
    
#    seeds = seed_ranges
    seed_ranges = np.array([int(i) for i in seed_ranges]).reshape((-1,2))
    seed_ranges = [range(start, start + l) for start, l in seed_ranges]

    for r in seed_ranges:
        print(r)
#        list_r = list(r)
#        print("range converted to list")
        for arr in maps.values():
            outputs = []
            for dr, sr, l in arr:
                if sr in r:
                    if sr+l-1 in r:
                        outputs.append(range(dr, dr+l))
                    else:
                        outputs.append(range(dr,max(r)))
            print(outputs)
            break
        
        
            
    

    
#    output = min_loc
#    return output
    

if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)

