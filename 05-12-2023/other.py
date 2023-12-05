import sys
import argparse
import numpy as np
import time

def trace(value, maps):
#    cnt.incr()
    for m in maps:
        value = m(value)
    

    return value
        
def make_map(ranges):
    def _map(source):
        for dr, sr, l in ranges:
            diff = source - sr
            if diff >= 0 and diff < l:
                destination = dr + diff
                return destination
        return source
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
#    print(maps)
    map_funcs = {}
    for k, v in maps.items():
        map_funcs[k] = make_map(v)
    _maps = list(map_funcs.values())
    
#    seeds = seed_ranges
    seed_ranges = np.array([int(i) for i in seed_ranges]).reshape((-1,2))
    seed_ranges = [range(start, start + l) for start, l in seed_ranges]
    seed_ranges.insert(0,range(0,5000000))
    
    class Count():
        def __init__(self):
            self.cnt = 0
            self.time = time.time()
        def incr(self):
            self.cnt += 1
            if self.cnt % 1000000 == 999999:
                print(self.cnt)
                print(time.time()-self.time)
    
    cnt = Count()
    out = []
    _time = time.time()
    seed_ranges.insert(0,range(2300000000,2310000000))
    for seeds in seed_ranges:
        a = [trace(seed, _maps) for seed in seeds]
        print("range complete",time.time()-_time)
        out.append(min(a))
        print(out)

        print(cnt.cnt)
    output = min(out)
    return output
    

if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)


