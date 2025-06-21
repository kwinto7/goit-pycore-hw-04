import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def parse_folder(path: Path, space: str=""):
    try:
        for element in path.iterdir():
            if element.is_dir():
                print(f"{space}{Fore.BLUE}{element.name}/")
                parse_folder(element, space + "    ")
            else:
                print(f"{space}{Fore.GREEN}{element.name}")
    except PermissionError:
        print(f"{space}{Fore.RED}[Access Denied]")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED} Please enter the directory path as follows: python main_task3.py \"path to the folder\"")
        return

    root = Path(sys.argv[1])

    if not root.exists():
        print(f"{Fore.RED} The inputed folder path does not exist")
        return
    
    if not root.is_dir():
        print(f"{Fore.RED} The inputed path is not a folder")
        return
    
    print(f"{Fore.BLUE}{root.name}/")
    parse_folder(root, space="    ")
    

if __name__ == "__main__":
    main()
