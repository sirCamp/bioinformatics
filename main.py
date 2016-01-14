from algorithm import *
import sys
import string
import os
import errno


# Main definition - constants
menu_actions  = {}

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')

    print "Welcome,\n"
    print "Please choose the menu you want to start:"
    print "[1] Genome insert length"
    print "[2] Sequence coverage"
    print "[3] Physical coverage"
    print "\n"
    print "[0]. Quit"
    choice = raw_input(">>  ")
    obj = run(choice)

    return obj

# Execute menu
def run(choice):

    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            if int(ch) > 0 and int(ch) <9:
                return menu_actions[ch]
            else:
                menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return


# Back to main menu
#def back():
#    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': "FirstAlgorithm",
    '2': "SequenceCoverageAlgorithm",
    '3': "PhysicalCoverageAlgorithm",
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

if len(sys.argv) < 2:
	print("You must pass the path of sam file")
	sys.exit(0)
else:

    if(os.path.exists(sys.argv[1])):

        algorithm = main_menu()
        obj = eval(algorithm)(algorithm,sys.argv[1])
        obj.run()
        print "Algorithm "+algorithm+" started"
    else:
        print("file not exists")

