import sys
import os 
from pathlib import Path 
from colorama import init, Fore, Style

init(autoreset=True)

def visualize_directory(directory_path, prefix=''):
    try:
        if not directory_path.exists():
            print(f"Помилка: Директорія {directory_path} не існує.")
            return
        
        if not directory_path.is_dir():
            print(f'Помилка: {directory_path} не є директорією.')
            return
        
        items  = sorted(directory_path.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            if is_last:
                branch = "┗ "
                new_prefix = prefix + " "
            else:
                branch = "┣ "
                new_prefix = prefix + "┃ "
                
            if item.is_dir():
                print(f'{prefix}{branch}{Fore.BLUE}{Style.RESET_ALL}{Fore.CYAN}{item.name}{Style.RESET_ALL}')
                visualize_directory(item, new_prefix)
            else:
                print(f'{prefix}{branch}{Fore.GREEN}{Style.RESET_ALL}{Fore.YELLOW}{item.name}{Style.RESET_ALL}')
                
    except Exception as e:
        print(f'Помилка: {e}')
                
def main():
    if len(sys.argv) != 2:
        print('Використання: python main.py /Users/vladislavkavunec/Desktop/goit-pycore-hw-04/picture')

        sys.exit(1)
        
    directory_path = Path(sys.argv[1])
    
    if not directory_path.exists():
        print(f'Помилка: Директорія {directory_path} не існує.')
        sys.exit(1)
        
    if not directory_path.is_dir():
            print(f'Помилка: {directory_path} не є директорією.')
            return
    
    print(f'{Fore.BLUE}{directory_path.name}{Style.RESET_ALL}')
    visualize_directory(directory_path)
    
if __name__ == "__main__":
    main()
        