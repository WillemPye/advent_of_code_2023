import sys
import argparse

def get_difs(series):
    difs = []
    prev_item = series[0]
    for item in series[1:]:
        difs.append(item-prev_item)
        prev_item = item
    return difs


def main():

    parser = argparse.ArgumentParser(description="Day 9 part 2 solver")
    parser.add_argument("--input", required=False, default="input.txt", help="Day 9 input as txt file, default of input.txt")
    args = parser.parse_args()
    input_path = args.input
    
    try:
        with open(input_path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Input file not found")
        sys.exit(1)
    lines = [line.strip("\n") for line in lines]
    series = [[int(i) for i in line.split(" ")] for line in lines]

    new_items = []
    for ser in series:
        #Create the differences lists (same as part 1)
        difs_list = [ser]
        idx = 0
        while True:
            difs = get_difs(difs_list[idx])
            idx += 1
            difs_list.append(difs)
            if [i for i in difs if i != 0] == []:
                break

        #Work back through differences get the prediction
        num_difs = len(difs_list)
        for i in range(num_difs):
            idx = num_difs - (i + 1)
            # print(difs_list[idx])
            if i == 0:
                difs_list[idx].insert(0,0)
                continue
            prev_val = difs_list[idx][0]-difs_list[idx+1][0]
            difs_list[idx].insert(0,prev_val)
        
        new_items.append(difs_list[0][0])

    output = sum(new_items)
    return output


if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)