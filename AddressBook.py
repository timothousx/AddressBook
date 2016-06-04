#Final
#Tim Hendersen

import csv

numList = []

def Mainprog():
#Main interface
    g = 0
    
    while g == 0:

        print('1) Create New Contact')
        print('2) Edit Contact')
        print('3) Delete Contact')
        print('4) Search for Contact')
        print('5) Exit')

        choice = input('Select an Option 1,2,3,4,5')

        if choice == '1':
            Inptnw()
        elif choice == '2':
            Edcnt()
        elif choice == '3':
            Delcnt()
        elif choice == '4':
            Srch()
        elif choice.capitalize() in {'5','E','EXIT','QUIT','Q'}:
            g = 1
        else:
            print('Please Try Again')

    exit()


'''
def initlst():

    try:
        r = open('pnums.csv','r',newline='')

        for line in r:
            wrline = []
            for word in line:
                if word == 'eol':
                    break
                else:
                    wrline.append(word)
            numList.append(wrline)
        r.close()
    except:
        pass

    return numList
'''
    
def Inptnw():
#Create contact using keyboard input
    control = input ("New Number? (y/n) ")

#    impcon = input ('Manual Entry or Import? (m/i) ')
#    if impcon.capitalize() in {'I','IMPORT'}:
 #       impfile() 

    if control == 'y':
        fnme = input ("\tInput First Name: ")
        lnme = input ('\tInput Last Name: ')
        pnum = input ('\tInput Phone Number: ')
        emal = input ('\tInput Email Address: ')
        adrs = input ('\tInput Address: ')
        city = input ('\tInput City: ')
        zcde = input ('\tInput ZipCode: ')
        
        numList.append((fnme,lnme,pnum,emal,adrs,city,zcde))

    return


def Edcnt():
#edit a contact
    Srch()

    cn = eval(input('Which Contact Number?: '))
    x = input("Edit what? (name, phone number,email\n\taddress, city, zipcode)")

    if x.capitalize() in {'N', 'NAME'}:
        f = input('New First Name: ')
        l = input('New Last Name: ')
        numList[cn] = (f,l,numList[cn][2],numList[cn][3],numList[cn][4],numList[cn][5],numList[cn][6])
    elif x.capitalize() in {'P','PHONE','PHONE NUMBER'}:
        p = input('New Phone Number: ')
        numList[cn] = (numList[cn][0],numList[cn][1],p,numList[cn][3],numList[cn][4],numList[cn][5],numList[cn][6])
    elif x.capitalize() in {'E','EMAIL'}:
        e = input('New Email: ')
        numList[cn] = (numList[cn][0], numList[cn][1], numList[cn][2],e, numList[cn][4], numList[cn][5], numList[cn][6])
    elif x.capitalize() in {'A','ADDRESS'}:
        a = input('New Address: ')
        numList[cn] = (numList[cn][0], numList[cn][1], numList[cn][2], numList[cn][3],a, numList[cn][5], numList[cn][6])
    elif x.capitalize() in {'C','CITY'}:
        c = input('New City: ')
        numList[cn] = (numList[cn][0], numList[cn][1], numList[cn][2], numList[cn][3], numList[cn][4],c, numList[cn][6])
    elif x.capitalize() in {'Z','ZIP','ZIPCODE'}:
        z = input('New Zipcode: ')
        numList[cn] = (numList[cn][0], numList[cn][1], numList[cn][2], numList[cn][3], numList[cn][4], numList[cn][5],z)

    print (numList[cn])

    return


def Delcnt():
#delete a contact
    Srch()

    cn = eval(input('Which Contact Number?: '))
    print(numList[cn][0:1])
    d = input('Are You Sure You Want to Delete? (Y/N)')
    if d.capitalize() in {'Y','YES'}:
        del numList[cn]
        print('Deleted')

    return

def Srch():
#find a contact
    lnct = 0
    lnctls = []
    srcht = input('Search Term: ')
    for line in numList:
        if srcht in line:
            print("Name: {1}, {0}\nPhone Number: {2}\nEmail: {3}\nAddress: {4} {5}, {6}".format(line[0],line[1],line[2],line[3],line[4],line[5],line[6]))
            print('Contact no.',lnct)
            lnctls.append(lnct)
        lnct += 1

    return lnct
#def impfile():



Mainprog()
#run program