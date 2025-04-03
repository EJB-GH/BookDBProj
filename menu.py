import pyfiglet
from input_handling import *
#from PIL import Image dont need at the moment


#menu doesnt need to really be its own class, should fold it into
#the query. This is overly complex for no reason
class menu():
    def __init__(self):
        self.selection = None
        self.header = "Lady's Library"
        self.t_options = ['Totals', 'Searches', 'Exit']
        self.sub_opt1 = ['Books', 'Authors', 'Books By Authors', 'Books By Genre']
        self.sub_opt2 = ['Author', 'Title', 'Series']

    def top_menu(self):
        print(f"{pyfiglet.figlet_format(self.header)}")
        print('---------------------------------------------------------')
        print("What would you like to do:\n")

    
    def find_query(self):

        #move through type of query selection
        for i in range(len(self.t_options)):
            print(f"\t{self.t_options[i]} - Enter {i + 1}\n")
        self.selection = choice(1, 3)

        #exit chosen, close program
        if self.selection == 3:
            print('Closing..\n')
            exit()
        if self.selection == 1:
            self.totaling()
        else:
            self.searching()

    def totaling(self):
        print("Totaling Options:\n")
        for i in range(len(sub_opt1)):
            print(f"\t*{sub_opt1[i]} - Enter {i + 1}\n")
        self.selection = choice(1, len(sub_opt1))

    def searching(self):
        print("Searches.:\n")
        for i in range(len(sub_opt2)):
            print(f"\t*{sub_opt2[i] - {i + 1}}\n")
        self.selection = choice(1, len(sub_opt2))