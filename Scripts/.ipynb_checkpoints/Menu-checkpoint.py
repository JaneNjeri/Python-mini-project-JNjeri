#! usr/bin/python

#Options to analyze PDB files
#import sys allows you to use the sys.exit command to quit/logout of the program

def Menu():
    """ This function prints the menu and then calls the Mainmenu function that outputs the various options.
        Arguments: pdb file and an option from the options given
    """
    
    from Mainmenu import Mainmenu
    
    space = (" ")
    a = " PDB ANALYSIS INTERFACE "
    b = " Pick your choice from below "
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
        
    # Initializing the Mainmenu function
    Mainmenu()
         
    globals()['option'] = input()
    
