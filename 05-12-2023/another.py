import sys
import argparse
import numpy as np
import time

class Count():
    def __init__(self):
        self.cnt = 0
        self.time = time.time()
    def incr(self):
        self.cnt += 1
        if self.cnt % 1000000 == 999999:
            print(self.cnt)
            print(time.time()-self.time)
                
def trace(value, maps, cnt):
    cnt.incr()
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
    seed_ranges = [int(i) for i in seed_ranges]
    seed_ranges = [[seed_ranges[i], seed_ranges[i+1]] for i in range(len(seed_ranges)) if i%2 == 0]
    
    seed_ranges.sort()
    seed_ranges = [(start, start + l) for start, l in seed_ranges]
#    print(f"Seed ranges: {seed_ranges}")
    
    maps = [[[int(i) for i in item.split(" ")] for item in cat.split(":")[1].strip(" \n").split("\n")] for cat in categories[1:]]
    
    maps_ = []
    for m in maps:
        m = sorted(m, key= lambda x: x[0])
        m = np.array(m)
        maps_.insert(0,m)
        print(m)

    row_num = 1
    for row in maps_[0]:
        choice = 0
        print("-----")
        start = row[0]
        length = row[2]
        for m in maps_:
            for dr, sr, l in m:
                if dr>start:
                    continue
                elif dr<=start and start<dr+l:
                    print(dr,sr,l)
                    start = start - dr + sr

                    if start + length <= sr+l:
                        length = length
                    else:
                        length = sr+l-start
                    end = start + length
                    print(start, end, length)
                    break
                    
            print(start, length)
        
        print(seed_ranges)
        for s, e in seed_ranges:
            if e < start:
                continue
            elif end < s:
                continue
            else:
                print(s,e)
                choice = max(start,s)
                print("choice",choice)
        if choice >0:
            break


    map_funcs = []
    for m in maps:
        map_funcs.append(make_map(m))
    cnt = Count()
    print("tracing",choice)
    output = trace(choice, map_funcs, cnt)
#
#    _maps = map_funcs
#    
#
#    seed_ranges = np.array([int(i) for i in seed_ranges]).reshape((-1,2))
#    seed_ranges = [range(start, start + l) for start, l in seed_ranges]
##    seed_ranges.insert(0,range(0,5000000))
#    
#
#    
#
#    out = []
#    _time = time.time(cnt)
#    for seeds in seed_ranges:
#        a = [trace(seed, _maps) for seed in seeds]
#        print("range complete",time.time()-_time)
#        out.append(min(a))
#        print(out)
#
#        print(cnt.cnt)
#    output = min(out)
    return output
    

if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)



