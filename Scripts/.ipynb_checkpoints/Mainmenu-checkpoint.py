#! usr/bin/python

#Options to analyze PDB files
#import sys allows you to use the sys.exit command to quit/logout of the program

def Mainmenu():
    """ This function provides different options for the user to select. """
    
    from Read_file import Read_file
    from Search_file import Search_file
    from Write_file import Write_file
    from Infor_file import Infor_file
    from Align_2files import Align_2files
    from Help_file import Help_file
    
    import sys
    global path
    
    m = ''
    while m == '':
        print("************MAIN MENU**************")

        print(""" Available options 
                [R]: Enter name of a PDB file 
                [S]: Search for PDB files
                [W]: Write out PDB files (PDB files in existence) 
                [I]: Information on PDB files
                [A]: Alignment
                [H]: Help
                [Q]: Quit
            """)
    
        choice = input('Please enter your choice: ')
        if choice.upper() == 'R':
            m = Read_file()
        elif choice.upper() == 'S':
            m = Search_file()
        elif choice.upper() == 'W':
            m = Write_file()
        elif choice.upper() == 'I':
            m = Infor_file()
        elif choice.upper() == 'A':
            m = Align_2files()
        elif choice.upper() == 'H':
            m = Help_file()
        elif choice.upper() == 'Q':
            sys.exit
        else:
            print('You must only enter R, S, W, I, A, H or Q. Please try again')
            choice = input('Please enter your choice: ')
    return m