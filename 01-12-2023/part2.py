import sys
import argparse

def process_item(item):
    bps = []
    for i, char_ in enumerate(item):
        if char_.isdigit():
            bps.append(i)
            bps.append(i+1)
    bps.insert(0,0)
    bps.append(None)
    
    substrings = [item[start:end] for start, end in zip(bps[:-1],bps[1:])]
    substrings = [sub for sub in substrings if sub != ""]
    
    digits = []
    for sub in substrings:
        slen=len(sub)
        if slen == 1:
            if sub.isdigit():
                digits.append(sub)
            continue
        elif slen < 3:
            continue
        for i in range(len(sub)):
            rem_len = len(sub[i:])
            for j in range(rem_len-2):
                k = sub[i:i+j+3]
                if k in digit_dict:
                    digits.append(digit_dict[k])
    return digits

def main():

    parser = argparse.ArgumentParser(description="Day 1 part 2 solver")
    parser.add_argument("--input", required=False, default="input.txt", help="Day 1 input as txt file, default of input.txt")
    args = parser.parse_args()
    input_path = args.input
    
    with open(input_path, "r") as f:
        input_text = f.read()
    
    data = input_text.split("\n")
    
    calibration_values = []
    
    for item in data:
        if item == "":
            continue
#        info = {"string": item}
        digits = process_item(item)
#        info.update({"first digit": digits[0], "last digit": digits[-1]})
        calibration_value = digits[0] + digits[-1]
        calibration_values.append(calibration_value)
#        info.update({"Calibration Value": calibration_value})
#        print(info)
    
    calibration_values = [int(v) for v in calibration_values]
    sum_ = sum(calibration_values)
    return sum_
            
        


if __name__ == "__main__":
    digit_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        }
    
    output = main()
    print(f"Output: {output}")
    sys.exit(0)
