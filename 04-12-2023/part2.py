import sys
import argparse

def main():

    parser = argparse.ArgumentParser(description="Day 4 part 2 solver")
    parser.add_argument("--input", required=False, default="input.txt", help="Day 4 input as txt file, default of input.txt")
    args = parser.parse_args()
    input_path = args.input
    
    with open(input_path, "r") as f:
        lines = f.readlines()
    
    cards_dict = {}
    games = 0
    for line in lines:
        line = line.strip("\n")
        line = line.replace("   "," ")
        line = line.replace("  "," ")
        if line == "":
            continue
        line = line.split(":")

        game_num = int(line[0].split(" ")[1])
        games += 1
        
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
        
        #Make info dicts
        cards_dict[game_num] = {"name": game_num, "matches": matches, "copies": 1}
    
    #Iterate over info dicts
    for i in range(1, games+1):
        info = cards_dict[i]
        num = info["name"]
        matches = info["matches"]
        copies = info["copies"]

        if matches == 0:
            continue
        
        #Add copies
        for j in range(1,matches+1):
            if i+j > games:
                continue
            cards_dict[i+j]["copies"] = cards_dict[i+j]["copies"]+copies
    
    #Get total number of copies
    total = 0
    for i in range(1, games+1):
        copies = cards_dict[i]["copies"]
        total += copies
    
    return total
        
        
if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)

