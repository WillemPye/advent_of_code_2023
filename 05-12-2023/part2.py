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
    
    maps = {k[:-4]: np.array([item.split(" ") for item in v.strip("\n").split("\n")]) for cat in categories[1:] for k, v in [cat.split(":")]}
    
    map_funcs = {}
    for k, v in maps.items():
        map_funcs[k] = make_map(v)
    
#    seeds = seed_ranges
    seed_ranges = np.array([int(i) for i in seed_ranges]).reshape((-1,2))
    seed_ranges = [range(start, start + l) for start, l in seed_ranges]
    lrang = [len(r) for r in seed_ranges]
    tot = sum(lrang)
    print(tot)
    pertot = [round(i*100/tot) for i in lrang]
    print(pertot)
    print(seed_ranges[0][0])
    tr = seed_ranges[0][0]
    for v in map_funcs.values():
        tr = (v(tr))
    f_loc = tr

    
    
    min_loc = f_loc
    cnt = 0
    for seeds in seed_ranges:
        for seed in seeds:
            trace = int(seed)
            for v in map_funcs.values():
                trace = (v(trace))
            if trace < min_loc:
                min_loc = trace
                print("overwrite")
            cnt += 1
            if cnt % 1000000 == 999999:
                print(cnt)
        print("range complete")
    
    output = min_loc
    return output
    

if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)

