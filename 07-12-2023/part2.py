import sys
import argparse

def main():

    parser = argparse.ArgumentParser(description="Day 7 part 2 solver")
    parser.add_argument("--input", required=False, default="input.txt", help="Day 7 input as txt file, default of input.txt")
    args = parser.parse_args()
    input_path = args.input
    
    try:
        with open(input_path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError as e:
        print("Input file not found")
        sys.exit(1)
    
    lines = [tuple(line.strip("\n").split(" ")) for line in lines]
    
    ranks = {
        "five": 0,
        "four": 1,
        "full": 2,
        "three": 3,
        "two pair": 4,
        "pair": 5,
        "high": 6,
        }
    
    #New rule J is weakest, hence J maps to 1
    card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    
    hands = {}
    for line in lines:
        cards = line[0]
        cards = sorted(cards)
        cards.append(None)
        
        #Count and remove Js
        Js = []
        for i, c in enumerate(cards):
            if c == "J":
                Js.append(i)
        Js.reverse()
        for i in Js:
            cards.pop(i)
        Js = len(Js)
        
        #Get Runs
        runs = []
        run = 0
        prev = None
        for card in cards:
            run += 1
            if card == prev:
                continue
            else:
                prev = card
                runs.append(run)
                run = 0
        if runs != []:
            runs.pop(0)
        runs.sort(reverse=True)
        
        #Add Jokers back in
        if runs != []:
            runs[0] = runs[0]+Js
        else:
            runs.append(0 + Js)
        
        #Count hands as before
        if runs == [5]:
            hand = ranks["five"]
        elif runs == [4,1]:
            hand = ranks["four"]
        elif runs == [3,2]:
            hand = ranks["full"]
        elif runs == [3,1,1]:
            hand = ranks["three"]
        elif runs == [2,2,1]:
            hand = ranks["two pair"]
        elif runs == [2,1,1,1]:
            hand = ranks["pair"]
        elif runs == [1,1,1,1,1]:
            hand = ranks["high"]
        if line in hands:
            print("duplicate")
        else:
            hands.update({line: hand})
    
    #This section should be fine for part 2 after reducing J's value to 1
    ordering = [ [], [], [], [], [], [], [] ]
    [ordering[rank].append(line) for line, rank in hands.items()]
    
    key = lambda x: [card_values[card] for card in x[0]]
    ordering = [sorted(o, key=key) for o in ordering]
    ordering.reverse()
    
    O = []
    for o in ordering:
        O = O + o
    
    total = 0
    for i, hand in enumerate(O):
        r = i+1
        total += r * int(hand[1])
    
    output = total
    return output
        
    
if __name__ == "__main__":
    output = main()
    print(f"Output: {output}")
    sys.exit(0)

