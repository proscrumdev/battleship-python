

class BColors:
    CYAN = '\033[36m'
    BLACK = '\033[31m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    ENDC = '\033[0m'

def print_with_color(text: str, color: BColors):
    #print in bash with colours following: https://stackoverflow.com/a/287944
    print(f"{color}{text}{BColors.ENDC}")