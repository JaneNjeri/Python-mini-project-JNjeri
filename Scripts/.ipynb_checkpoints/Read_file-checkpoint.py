#! usr/bin/python

global path   
dikt = {}
dikt.update({1:'1hab.pdb', 2:'3b3b.pdb', 3:'3k6h.pdb', 4:'4kty.pdb'})

def pdbfile_list():
    """ This function finds all loaded files in the appropriate folder. """
    import glob, os
    os.chdir("../Data")
    file_list = []
    for file in glob.glob("*.pdb"):
        file_list.append(file)
    return file_list


def add_file():
    """ This function adds loaded files to a list containing the loaded pdb files. """
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    fl_list = list(pdbfile_list())
    if filepath.endswith('.pdb'):
        fl_list.append(filepath)
    else:
        print('Enter a valid file.')
    return fl_list


def file_append_dikt():  #adding files that are loaded in a dictionary
    """This function appends pdb files to a dictionary with specific keys and values """
    import os
    dikt = {}
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    with open(filepath, 'r') as file:
        for i in file:
            line = i.split()
            if len(line) == 2:
                key, value = line[0], line[1]
                dikt[key] = value
    print(dikt)
    
def check_existence():    #checking if a file exists in the PDB_files directory
    """ This function checks if the pdb file exists and loads it to a specific dictionary """
    import os
    choice = input('Enter the name of the file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    
    if filepath in dikt.values():
        print("File %s is loaded, do you want to replace the file?" %infile)
        replace = input("Yes/No: ")
        outfile = infile
        replace = replace.upper()
        print(infile.replace(infile, outfile))
    else:
        print('File does not exist! Check file again.')
    Menu()

    

def Read_file():
    """ This function loads a pdb file and reads contents for analysis """
    
    choice = input('Enter name of pdb file: ')
    filepath = os.path.join('/home/njesh/python-mini-project-JaneNjeri/Data', choice)
    with open(filepath, 'r')as pdb:
        try:
            if filepath.endswith('.pdb'):
                file_added = file_append_dikt()
                add_file()
                print(file_added)
                print('File added!')
            else:
                if not filepath.endswith('.pdb'):
                    print(input('Not the right pdb format! Please re-enter: '))
                    check_existence()    
                        
            if filepath in dikt.values():
                print("File %s is loaded, do you want to replace the file?" %filepath)
                replace = input("Yes/No: ")
                outfile = filepath
                replace = replace.upper()
                print(filepath.replace(filepath, outfile))
                print('File replaced.')
            else:
                print('File does not exist! Check file again.') 
        except:
            print('File does not exist! Check file again.')
    Mainmenu()