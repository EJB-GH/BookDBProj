def name_input(): #an input checker specifically for author names
    while True:
        try:
            string = input()
            if len(string) > 150:
                raise ValueError("Input surpassed size allowance.")
            if string == '':
                raise ValueError("Input cannot be blank")
            if any(char.isdigit() for char in string):
                print("Please enter characters only.")
                continue
            return string
        except ValueError as e:
            print(f"An input error has occurred. {e}")

def title_input(): #an input checker specifically for titles
    #modified to allow for numeric inputs
    #requires testing to see if anything else should be checked
    while True:
        try:
            string = input()
            if len(string) > 150:
                raise ValueError("Input surpassed size allowance.")
            if string == '':
                raise ValueError("Input cannot be blank")
            
                continue
            return string
        except ValueError as e:
            print(f"An input error has occurred. {e}")


def choice(low,high):
    choice = 0
    try:
        choice = check_choice()
        while choice < low or choice > high:
            print("Please enter a valid option: ")
            choice = check_choice()
    except ValueError as e:
        print(f"An input error has occurred. {e}")
    except Exception as e:
        print(f"An unknown error has occurred. {e}")

    print()
    return choice

def check_choice():
    while True:
        try:
            option = input("Enter choice from the options: ")
            if len(option) > 9:
                raise ValueError("Input surpassed size allowance.")
            if any(char.isalpha() for char in option):
                print("Please retry.")
                continue
            choice = int(option)
            return choice
        except ValueError as e:
            print(f"An input error has occurred. {e}")