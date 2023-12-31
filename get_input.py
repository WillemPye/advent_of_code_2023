import sys
import os
import argparse
import json
import csv
import requests
import hashlib
import base64
from cryptography.fernet import Fernet


def make_cache(cookies, key):
    try:
        if key is not None:
            key = base64.b64encode(hashlib.sha256(key.encode()).hexdigest().encode())[-45:-1]
            fernet = Fernet(key)
            cookies = fernet.encrypt(cookies.encode()).decode()

        with open(".cookies_cache","w") as f:
            f.write(cookies)
    except Exception as e:
        print(f"Caching cookies failed: {e}")

def read_cache(key):
    try:
        with open(".cookies_cache","r") as f:
            cookies = f.read()
        
        if key is not None:
            key = base64.b64encode(hashlib.sha256(key.encode()).hexdigest().encode())[-45:-1]
            fernet = Fernet(key)
            cookies = fernet.decrypt(cookies).decode()
        
        return cookies
    
    except Exception as e:
        print(f"Reading cookies failed: {e}")
        cookies = input("Enter cookies manually\n")
        if cookies == "":
            sys.exit(1)
        key = input("Enter password to encrypt cache with optional")
        if key == "":
            key = None
        make_cache(cookies, key)
        return cookies

def create_directories(path):
    try:
        os.makedirs(path)
        print(f"Directories created at: {path}")
    except FileExistsError:
        print(f"Directories already exist at: {path}")

def txt(r, saveloc):
    try:
        data = r.text
        with open(f"{saveloc}.txt", "w") as f:
            f.write(data)
    except Exception as e:
        print(f"Error: {e}")
        print("Program failed. Exiting now...")
        sys.exit(1)
    else:
        print("Success. Exiting now...")
        sys.exit(0)

def _json(r, saveloc):
    try:
        data = r.json()
    except:
        _txt = input("Failed to load as json.\n Would you like to attempt to save as txt? 'n' for No, anything else for Yes\n")
        if _txt == "n":
            print("Program failed. Exiting now...")
            sys.exit(1)
        else:
            print("Trying as .txt")
            txt(r, saveloc)
            return
    try:
        with open(f"{saveloc}.json", "w") as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error: {e}")
        print("Program failed. Exiting now...")
        sys.exit(1)
    else:
        print("Success. Exiting now...")
        sys.exit(0)

def _csv(r, saveloc, sep=",", row_sep="\n"):
    try:
        rows = [row.split(sep) for row in r.text.split(row_sep)]
    except:
        reattempt = input("CSV seperation failed, try again with different seperators? 'n' for No, anything else for Yes\n")
        if reattempt != "n":
            row_sep = input("Enter row seperator\n")
            sep = input("Enter item seperator\n")
            csv(r, saveloc, sep=sep, row_sep=row_sep)
            return
        _txt = input("Try to save as .txt? 'n' for No, anything else for Yes\n")
        if _txt == "n":
            print("Program failed. Exiting now...")
            sys.exit(1)
        else:
            print("Trying as .txt")
            txt(r, saveloc)
            return
    try:
        with open(f"{saveloc}.csv","w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    except Exception as e:
        print(f"Error: {e}")
        print("Program failed. Exiting now...")
        sys.exit(1)
    else:
        print("Success. Exiting now...")
        sys.exit(0)


def main():
    routes = {"json": _json, "txt": txt, "csv": _csv, "jsn": json}

    #set up arg parser
    parser = argparse.ArgumentParser(description="Get daily advent of code inputs")
    parser.add_argument("--day", required=True, help="Day of data you want")
    parser.add_argument("--save_loc", required=False, help="Save name, without file extension.")
    parser.add_argument("--cookies", required=False, help="Cookies argument for authentication, copy and paste from chrome dev tools")
    parser.add_argument("--format", required=False, help="Output format .txt, .json or .csv")
    parser.add_argument("--key", required=False, help="passcode for reading cookies cache")

    # Parse the command line arguments
    args = parser.parse_args()
    day = args.day
    save_loc = args.save_loc
    cookies = args.cookies
    key = args.key
    
    format = "txt" if args.format is None else args.format
    url = f"https://adventofcode.com/2023/day/{day}/input"

    if save_loc is None:
        save_loc = f"day{day}{os.path.sep}input"
    
    name_len = len(save_loc.split(os.path.sep)[-1])
    dir = save_loc[:-name_len]
    create_directories(dir)

    #Handle cookies
    if cookies is None:
        cookies = read_cache(key)
    else:
        _cache = input("Cache cookies? 'n' for No, anything else for Yes\n")
        if _cache != "n":
            make_cache(cookies, key)
    
    cookies = cookies.replace(" ","")
    cookies = cookies.split(";")
    cookies = {k:v for cookie in cookies for k,v in [cookie.split("=",1)]}

    #Send request
    r = requests.get(url, cookies=cookies)

    func = routes.get(format, txt)

    func(r, save_loc)

if __name__=="__main__":
    main()
