import sys
import argparse
import numpy as np

def check(dist, t_time, h_time):
    return True if get_dist(t_time, h_time) > dist else False


def get_dist(t_time, h_time):
    return h_time*(t_time-h_time)

def main():

    parser = argparse.ArgumentParser(description="Day 6 part 2 solver")
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
    t = int(lines[0][1].replace(" ",""))
    d = int(lines[1][1].replace(" ",""))

    print(t,d)

    # a+b = t
    # a = t - b
    # a*b = d
    # (t-b)b =d
    # tb - b^2 -d = 0
    # (-t +- sqrt(t^2-4d)))/-2

    disc = (t**2) - (4*d)
    _disc = np.sqrt(disc)
    sol1 = (t-_disc)/2
    sol2 = (t+_disc)/2
    print(sol1,sol2)
    output = round(sol2 - sol1) + 1
    return output


if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)