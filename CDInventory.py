#------------------------------------------#
# Title: CDInventory.py
# Desc: Script CDInventory to store CD Inventory data
# Change Log: (Who, When, What)
# Rudolph Carvajal, 2020-Aug-11, Created File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
dicRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')

while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

# Process and Present Data
    if strChoice == 'x':
        # Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # Load existing data
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': lstRow[0], 'CD Title': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        
    elif strChoice == 'a':  
        # Add data to the table in a 2d-list each time the user wants to add data
        
        # Structured error handling to ensure user inputs an integer for an ID
        while True:
            strID = input('Enter an ID: ')
            try:
                intID = int(strID)
                break;
            except ValueError:
                print("This is not a number. Please enter a valid number")
                
        # Continue with rest of script once integer is entered        
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')         
        dicRow = {'ID': intID, 'CD Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        Tblsize = len(lstTbl)
        print('You have',Tblsize,'CD(s) in inventory\n',)
        
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist\n')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1]
            print(strRow)
            
    elif strChoice == 'd':
        # Deleting the entire entry in inventory based on CD Title
        delrow = input('Enter a CD Title to delete: ').lower()
        for row in range(len(lstTbl)):
            if delrow in lstTbl[row].values():
                del lstTbl[row]
                print('You deleted:',delrow,'from inventory')
            else: ""
        # Letting the user know that entry is not in inventory
        newsize = len(lstTbl)
        if Tblsize == newsize:
            print('That CD is not currently in inventory\n')
        else: ""
        
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        
    else:
        print('Please choose either l, a, i, d, s or x!')

