import sys
import os
import argparse

def main():

    parser = argparse.ArgumentParser(description="Day 1 part 1 solver")
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
        digits = []
        for char_ in item:
            #I think this could be done faster by reading from the start and end of string simultaneously, but for code aesthetics i have done it like this.
            if char_.isdigit():
                digits.append(char_)
#        info.update({"first digit": digits[0], "last digit": digits[-1]})
        calibration_value = digits[0] + digits[-1]
        calibration_values.append(calibration_value)
#        info.update({"Calibration Value": calibration_value})
#        print(info)
    
    calibration_values = [int(v) for v in calibration_values]
    sum_ = sum(calibration_values)
    return sum_
            
        


if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)
