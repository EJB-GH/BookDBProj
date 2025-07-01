import pyfiglet
from queries import *
from input_handling import *

header = "Lady's Library"
t_options = ['Totals', 'Searches', 'Exit']
sub_opt1 = ['Books', 'Authors', 'Books By Authors', 'Books By Genre']
sub_opt2 = ['Author', 'Title', 'Series']

def top_menu() -> str:
    print(f"{pyfiglet.figlet_format(header)}")
    print('---------------------------------------------------------')
    print("What would you like to do:\n")
    return str(find_query())

    
def find_query() -> str:
    #move through type of query selection
    for i in range(len(t_options)):
        print(f"\t{t_options[i]} - Enter {i + 1}\n")
    selection = choice(1, 3)

    #exit chosen, close program
    if selection == 3:
        print('Closing..\n')
        exit()
    if selection == 1:
        return totaling()
    else:
        return searching()

def totaling() -> str:
    print("Totaling Options:\n")
    for i in range(len(sub_opt1)):
        print(f"\t*{sub_opt1[i]} - Enter {i + 1}\n")
    selection = str(sub_opt1[choice(1, len(sub_opt1)) - 1])
    return str(selection)

def searching() -> str:
    print("Searches.:\n")
    for i in range(len(sub_opt2)):
        print(f"\t*{sub_opt2[i] - {i + 1}}\n")
    return choice(1, len(sub_opt2))

def main():
    #run the top level menu
    #and find which query is needed
    db = query()

    search = top_menu()
    if search == 'Authors':
        db.total_authors()



if __name__ == "__main__":
    main()

