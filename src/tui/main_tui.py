from colorama import Fore, Back, Style, init


def run():
    """
    :returns: status code for menu choices
    """
    init(autoreset=True)

    print_val = """
What do you want to do?
1) create new layout
2) print current layout
3) load layout
4) start soundpad
5) list layouts
6) edit layouts

Enter number (1-6) to select option to run: 
"""

    # Check if input is valid
    while True:
        val = input(print_val)

        # Check if input is a number
        try:
            val = int(val)
        except:
            print(f"{Fore.RED} You need to enter a whole number.")

        if val < 7 and val > 0:
            return val

if __name__ == "__main__":
    print(run())