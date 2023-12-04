import sys
import argparse

def main():

    parser = argparse.ArgumentParser(description="Day 4 part 1 solver")
    parser.add_argument("--input", required=False, default="input.txt", help="Day 4 input as txt file, default of input.txt")
    args = parser.parse_args()
    input_path = args.input
    
    with open(input_path, "r") as f:
        lines = f.readlines()
    
    points_list = []
    for line in lines:
        line = line.strip("\n")
        line = line.replace("   "," ")
        line = line.replace("  "," ")
        if line == "":
            continue
        line = line.split(":")

        game_num = int(line[0].split(" ")[1])
        
        #Seperate winning numbers from card numbers
        values = line[1].split("|")
        #Remove leading and trailing spaces
        values = [item.strip(" ") for item in values]
        #Split into lists of numbers
        winning_numbers = values[0].split(" ")
        numbers = values[1].split(" ")

        
        #get matches
        matches = 0
        for num in numbers:
            if num in winning_numbers:
                matches += 1
        
        #Get points
        if matches == 0:
            points = 0
        else:
            points = 2**(matches-1)
        points_list.append(points)
        
    output = total_points = sum(points_list)
    return output
        
if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)
