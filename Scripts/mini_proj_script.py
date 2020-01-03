#! usr/bin/python

""" This section initializes the program,and calls in the Mainmenu """

# No pdb file at start
pdb = "None"

# Importing the start module
from Menu import Mainmenu

# Initializing the program by calling the Mainmenu function
Mainmenu(option)


def Menu(pdb,option):
    """ This function prints the menu and then calls the Mainmenu function that outputs the various options.
        Arguments: pdb file and an option from the options given
    """
    
    from Mainmenu import Mainmenu
    
    # Available options
    space = (" ")
    a = " PDB ANALYSIS INTERFACE "
    b = " Please enter your choice: "
    c = " [R] = Enter name of a PDB file "
    d = " [S] = Search for PDB files "
    e = " [W] = Write out PDB files (Files in existence) "
    f = " [I] = Information on PDB files "
    g = " [A] = Alignment "
    h = " [H] = Help "
    i = " [Q] = Quit "

    # Creating the body head of the program with lines of length 70
    ln1 = (space+("#"*70))
    ln2 = (space+"#"+a+(space*(70-len(a)-2))+"#")
    ln3 = (space+("#"*70))
    ln4 = (space+"#"+b+(space*(70-len(b)-2))+"#")
    ln5 = (space+"#"+(space*68)+"#")
    ln6 = (space+"#"+space+c+(space*(70-len(c)-5-35))+(space*30)+space*5+"#")
    ln7 = (space+"#"+space+d+(space*(70-len(d)-5-35))+(space*30)+space*7+"#")
    ln8 = (space+"#"+space+e+(space*(70-len(e)-5-35))+(space*19)+"#")
    ln9 = (space+"#"+space+f+(space*(70-len(f)-5-35))+(space*30)+space*5+"#")
    ln10 = (space+"#"+space+g+(space*(70-len(g)-5-35))+(space*30)+space*7+"#")
    ln11 = (space+"#"+space+h+(space*(70-len(h)-5-35))+(space*30)+space*7+"#")
    ln12 = (space+"#"+space+i+(space*(70-len(i)-5-35))+(space*30)+space*7+"#")
    ln13 = (space+("#"*70))

    
    lines = [ln1,ln2,ln3,ln4,ln5,ln6,ln7,ln8,ln9,ln10,ln11,ln12,ln13]
    
    print("\n")
    # Read all lines to recreate menu
    for line in lines:
        print(line)
    
        
    # Selecting an option
    option = input("     :")
    option = option.upper()
    
    # Initializing the Mainmenu function
    Mainmenu(option)
         
    globals()['option'] = input()
    
    

#Options to analyze PDB files
#import sys allows you to use the sys.exit command to quit/logout of the program
import sys

def Mainmenu(option):
    """ This function provides different options for the user to select.
        Arguments: option
    """
    
    global path
    
    print("************MAIN MENU**************")

    choice = input(""" Please enter your choice: 
                        [R]: Enter name of a PDB file 
                        [S]: Search for PDB files
                        [W]: Write out PDB files (PDB files in existence) 
                        [I]: Information on PDB files
                        [A]: Alignment
                        [H]: Help
                        [Q]: Quit

                        """)

    if choice.upper() in ('R','S','W','I','A','H','Q'):
        if choice.upper() == "R":
            print('Enter name of pdb file: ')
        elif choice.upper() == 'S':
            print('Search for a pdb file: ')
        elif choice.upper() == 'W':
            print('Read in pdb files: ')
        elif choice.upper() == 'I':
            print('Give a list of pdb files: ')
        elif choice.upper() == 'A':
            print('Align sequences from two PDB files')
        elif choice.upper() == 'H':
            print('Lists all options and gives a brief description')
        elif choice.upper() == 'Q':
            sys.exit
    else:
        print('You must only enter R, S, W, I, A, H or Q. Please try again')
        choice = input('Please enter your choice: ')
        
        
global path   
dikt = {}
dikt.update({1:'1hab.pdb', 2:'3b3b.pdb', 3:'3k6h.pdb', 4:'4kty.pdb'})

""" This function finds all loaded files. """
def pdbfile_list():
    import glob, os
    os.chdir("../PDB_files")
    file_list = []
    count = 0
    for file in glob.glob("*.pdb"):
        file_list.append(file)
        count+=1
    return file_list, count

""" This function adds loaded files to a list containing the loaded pdb files. """
def add_file(infile):
    pdbfile_list = fl_list
    if infile.endswith('.pdb'):
        fl_list.append(infile)
    else:
        print('Enter a valid file.')

"""This function appends pdb files to a dictionary with specific keys and values """

def file_append_dikt(infile):  #adding files that are loaded in a dictionary
    dikt = {}
    with open(infile, 'r') as file:
        for i in file:
            line = i.split()
            if len(line) == 2:
                key, value = line[0], line[1]
                dikt[key] = value
    print(dikt)
                   

""" This function checks if the pdb file exists and loads it to a specific dictionary """

def check_existence(infile):    #checking if a file exists in the PDB_files directory       
    if infile in dikt.values():
        def file_path():               
            path = "/home/njesh/python-mini-project-JaneNjeri/PDB_files"
            for files in os.walk(path, onerror=None):
                for infile in files:
                    file_path = os.path.join(path, infile)
        print("File %s is loaded, do you want to replace the file?" %infile)
        replace = input("Yes/No: ")
        outfile = infile
        replace = replace.upper()
        print(infile.replace(infile, outfile))
    else:
        print('File does not exist! Check file again.')
    Menu()
        

""" This function loads a pdb file and reads contents for analysis """

def Read_file():
    
    from file_append_dikt import file_append_dikt
    from check_existence import check_existence
    
    if option.upper() in ('R','S','W','I','A','H','Q'):
        if option.upper() == 'R':
            infile = input(print("Enter name of pdb file: "))
            with open(infile, 'r')as pdb:
                try:
                    if infile.endswith('.pdb'):
                        file_added = file_append_dikt(infile)
                        print('Files entered %s' %infile)
                        print(file_added)
                        add_file(infile)
                    else:
                        if not infile.endswith('.pdb'):
                            print(input('Not the right pdb format! Please re-enter: '))
                            check_existence(infile)
                            print(check_existence(infile))    
                    if infile in dikt.values():
                        def file_path():
                            path = "/home/njesh/python-mini-project-JaneNjeri/PDB_files"
                            for files in os.walk(path, onerror=None):
                                for infile in files:
                                    file_path = os.path.join(path, infile)
                        print("File %s is loaded, do you want to replace the file?" %infile)
                        replace = input("Yes/No: ")
                        outfile = infile
                        replace = replace.upper()
                        print(infile.replace(infile, outfile))
                    else:
                        print('File does not exist! Check file again.')
                except:
                    print('File does not exist! Check file again.')
    Menu(infile)
                    

