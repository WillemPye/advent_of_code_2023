import sys
import argparse
import numpy as np

def check(dist, t_time, h_time):
    return True if get_dist(t_time, h_time) > dist else False


def get_dist(t_time, h_time):
    return h_time*(t_time-h_time)

def main():

    parser = argparse.ArgumentParser(description="Day 6 part 1 solver")
    parser.add_argument("--input", required=False, default="input.txt", help="Day 6 input as txt file, default of input.txt")
    args = parser.parse_args()
    input_path = args.input
    
    try:
        with open(input_path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError as e:
        print("Input file not found")
        sys.exit(1)

    lines = [line.strip("\n").split(":") for line in lines]
    times = lines[0][1]
    distances = lines[1][1]
    times = [int(t) for t in times.strip().split()]
    distances = [int(d) for d in distances.strip().split()]
    print(times,distances)

    combos = []
    for t, d in zip(times, distances):
        split = round(t/2)
        cnt = 0
        print(split)
        if check(d, t, split):
            cnt+=1
        else:
            continue
        split -= 1
        while check(d,t,split):
            print(split)
            cnt += 2
            split -= 1
        combos.append(cnt)
    print(combos)
    output = np.product(combos)
    return output


if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)