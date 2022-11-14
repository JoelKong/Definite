from Business.app_logic import *

#Joel
def inputoutput():
    main = False
    log_in = True
    home = False
    mytokens = False
    buytokens = False
    saverpoints = False
    settings = False
    walletgroupinterface = True
    notnewaccount = False
    goinginside = False
    goinginside2 = False
    paymentscreen = False
    navigater = True
    bronze = 0
    silver = 0.2
    gold = 0.5
    black = 0.75
    WalletList = []
    WGNList =[]
    collaboratelist = []
    invisiblecollaboratelist = []
    currentstakelist = []
    completedstakelist = []

    #Sign up and log in page
    print('Welcome to Definite. Curated for your financial goals')
    while log_in:
        create_or_login = input("Press 1 to log in, Press 2 to create new account ")
        if create_or_login == '1':
            email_login = input("Email: ")
            password_login = input("Password: ")
            if login(email_login,password_login):
                currency = input('What currency would you like to view the prices in? (Eg. JPY) ')
                print('Login Successful.')
                if appendlist(email_login) != 'NULL':
                    WalletList.append(appendlist(email_login))
                    WGNList.append(appendlistname(email_login))
                    invisibleid = WalletList[0].split(',')
                    invisiblename = WGNList[0].split(',')
                    WGNList = WGNList[0].split(',')

                else:
                    invisibleid = []
                    invisiblename = []
                log_in = False
                main = True
                home = True
            else:
                print("There is no such account. Please try again.")

        elif create_or_login == '2':
            firstname = input("First name: ")
            lastname = input("Last name: ")
            email = input("Email: ")
            password = input("Password: ")
            accid = "A" + str(random.randint(10000,99999))
            if checksameemailpass(email,password) == []:
                account_info(firstname, lastname,email, password,accid)
                print('Successful')
            else:
                print('Please choose a different email and password as what you have chosen has already been used.')
        else:
            print("Please choose a valid option")  

    while main:
        #Home page
        while home:
            print('Welcome ' + str(checkname(email_login,password_login)))
            print('You have ' + str(savertoken(email_login,password_login)[0][0]) + ' ' + 'tokens')
            print('You have ' + str(savertoken(email_login,password_login)[0][1]) + ' ' + 'saver points')
            if float(saverpointsspent(email_login)) < 200:
                updatetier(email_login, 'Bronze')
            elif float(saverpointsspent(email_login)) >= 200 and float(saverpointsspent(email_login)) < 800:
                updatetier(email_login,'Silver')
            elif float(saverpointsspent(email_login)) >=800 and float(saverpointsspent(email_login)) < 1000:
                updatetier(email_login,'Gold')
            else:
                updatetier(email_login,'Black')

            print('Your tier level is ' + homesaver(email_login)[0][0])
            if homesaver(email_login)[0][0] == 'Bronze':
                level = bronze
            elif homesaver(email_login)[0][0] == 'Silver':
                level = silver
            elif homesaver(email_login)[0][0] == 'Gold':
                level = gold
            elif homesaver(email_login)[0][0] == 'Black':
                level = black
            print('Your added interest is ' + '+' + str(level) + '%')
            print('Your account ID is ' + detectaccountid(email_login))

            navigation = True
            while navigation:
                navigate = input('Press 1 to look at your wallet groups. Press 2 to look at your saver points. Press 3 to access the QR code for your account and log out. Press 4 to upgrade your account. Press 5 to select other features ')
                #Wallet groups
                if navigate == '1':
                    print('These are your current wallet groups and number of collaborators')
                    if invisiblename == []:
                        print('No wallet groups available')
                    else:
                        print('My groups:')

                        for group in invisiblename:
                            if collabprint(email_login,group) != 'NULL':
                                invisiblecollaboratelist.clear()
                                invisiblecollaboratelist.append(collabprint(email_login,group))
                                invisiblecollaboratelist = invisiblecollaboratelist[0].split(',')
                                print(str(group) + ' + (' + str(len(invisiblecollaboratelist)) + ')')
                                invisiblecollaboratelist.clear()
                            else:
                                print(str(group) + ' + (0)')
                    print('')
                    print('These are the current wallet groups you are being added to')
                    print('Added to:')
                    loopthroughcollaborator(email_login)
                    notnewaccount = True
                    navigation = False
                    walletgroupinterface = True
                    navigater = True

                #Saverpoints 
                elif navigate == '2':
                    saverpoints = True
                    home = False
                    navigation = False
                    while saverpoints:
                        print('Welcome to My Saver Points')                        
                        if savertoken(email_login,password_login)[0][1] != '0':
                            print('You currently have ' + savertoken(email_login,password_login)[0][1] + ' saver points. Approximately ' + str(float(api('SGD',currency.upper(),float(savertoken(email_login,password_login)[0][1])/100))) + ' ' + str(currency.upper()))
                        else:
                            print('You currently have 0 saver points.')
                        
                        print('Current stakes in this month: ')
                        w = 0
                        currentstakelist.clear()
                        for data in gettokendurationinterest(email_login):
                            if int(gettokendurationinterest(email_login)[w][6]) > 0:
                                currentstakelist.append(gettokendurationinterest(email_login)[w][0] + ' tokens | ' + gettokendurationinterest(email_login)[w][2] + '% | Saver points awarded next month: ' + str(((float(gettokendurationinterest(email_login)[w][0]) * float(gettokendurationinterest(email_login)[w][2])) / 12) * (31 - float(getinitialminusone(email_login)[w][0]) / 31 )))
                                print(gettokendurationinterest(email_login)[w][0] + ' tokens | ' + gettokendurationinterest(email_login)[w][2] + '% | Saver points awarded next month: ' + str(round(((float(gettokendurationinterest(email_login)[w][0]) * float(gettokendurationinterest(email_login)[w][2])) / 12) * (31 - float(getinitialminusone(email_login)[w][0]) / 31 ))))
                                w += 1
                        tierbenefit = input('Press 1 to check your current tier benefits. Press 2 to go back. ')
                        #Tier benefits
                        if tierbenefit == '1':
                            print('Tier: ' + str(homesaver(email_login)[0][0]))
                            print('Benefit: +' + str(level) + '% ' + 'interest')
                            print('Total saver points spent: ' + str(saverpointsspent(email_login)))
                            print('Information of tier levels:')
                            print('Bronze: No added interest. 0 saver points required to be spent')
                            print('Silver: 0.2% ' + 'interest. 200 saver points required to be spent')
                            print('Gold: 0.5% ' + 'interest. 800 saver points required to be spent')
                            print('Black: 0.75% ' + 'interest. 1000 saver points required to be spent')
                            saverpointexchange = input('Press 1 to exchange your saver points. Press 2 to go back. ')
                            
                            #Exchange shop
                            if saverpointexchange == '1':
                                print('Welcome to the exchange shop!')
                                print(str(savertoken(email_login,password_login)[0][1]) + ' saver points available')
                                print('Options available for exchange:')
                                listofoptions = ['Credit to bank account','Credit to my cards','1 month spotify premium (1500 saver points)','1 month netflix subscription (1500 saver points)','$5 fairprice e-voucher (450 saver points)','$5 KLOOK app evoucher (450 saver points)']
                                listofoptionsprice = [0,0,1500,1500,450,450]
                                for option in listofoptions:
                                    print(option)
                                selectexchange = input('Select the item which you would like to exchange by keying in numbers corresponding to what you see on the screen. (Eg. Press 1 to credit to bank account) Key in "exit" to go back. ')
                                if selectexchange == 'exit':
                                    walletgroupinterface = False
                                    navigation = False
                                    home = True

                                else:
                                    confirmexchange = input('You are going to exchange for "' + str(listofoptions[int(selectexchange)-1]) + '". Confirm? (y/n) ')
                                    if confirmexchange == 'n':
                                        walletgroupinterface = False
                                        navigation = False
                                        home = True
                                    elif confirmexchange == 'y':
                                        if float(savertoken(email_login,password_login)[0][1]) >= int(listofoptionsprice[listofoptions.index(listofoptions[int(selectexchange)-1])]):
                                            updatedsaverpoints = float(savertoken(email_login,password_login)[0][1]) - int(listofoptionsprice[listofoptions.index(listofoptions[int(selectexchange)-1])])
                                            updatesaver(email_login,updatedsaverpoints,float(listofoptionsprice[listofoptions.index(listofoptions[int(selectexchange)-1])]) + float(saverpointsspent(email_login)))

                                            print('Successful')
                                            walletgroupinterface = False
                                            navigation = False
                                            home = True
                                        else:
                                            print('You do not have enough saver points to make this transaction')
                                            walletgroupinterface = False
                                            navigation = False
                                            home = True

                                    else:
                                        print('Invalid option. Please try again')
                                        navigation = False
                                        walletgroupinterface = False
                            elif saverpointexchange == '2':
                                walletgroupinterface = False
                                navigation = False
                                home = True
                            else:
                                print('Invalid option. Please try again')
                                navigation = False
                                walletgroupinterface = False
                                home = True
                        elif tierbenefit == '2':
                            walletgroupinterface = False
                            navigation = False
                            home = True
                        else:
                            print('Invalid option. Please try again')
                            navigation = False
                            walletgroupinterface = False
                            home = True

                        saverpoints = False
                
                #QR code for Collaborators and log out function
                elif navigate == '3':
                    print('Name: ' + str(checkname(email_login,password_login)))
                    print('Account ID: ' + detectaccountid(email_login))
                    print('People can scan your QR code below to add you into their wallet group')
                    print('*QR code')
                    logout = input('Press 1 to log out. Press 2 to return back to the home page. ')
                    if logout == '1':
                        walletgroupinterface = False
                        navigation = False
                        navigater = False
                        home = False
                        main = False
                        inputoutput()
                    elif logout == '2':
                        walletgroupinterface = False
                        navigation = False
                        navigater = False
                    else:
                        print('Invalid. Please try again.')
                        walletgroupinterface = False
                        navigation = False
                        navigater = False

                #Upgrade account
                elif navigate == '4':
                    print('Upgrading your account would cost ' + api('SGD',currency.upper(),3.99) + ' ' + currency.upper() + '/month and give you unlimited creations of wallet groups')
                    upgrade = input('Press 1 to upgrade. Press 2 to go back ')
                    if upgrade == '1' and checkupgrade(email_login)[0][0] != 'Upgrade':
                        choice = input('Press 1 to scan QR code. Press 2 to enter card details. ')
                        if choice == '1':
                            upgradeaccount(email_login,'Upgrade')
                            print('Successful')
                            walletgroupinterface = False
                            navigation = False
                            navigater = False
                        elif choice == '2':
                            number = input('Card Number: ')
                            name = input('Name on card: ')
                            expiry = input('Expiry date: ')
                            cvv = input('CVV: ')
                            upgradeaccount(email_login,'Upgrade')
                            print('Successful')
                            walletgroupinterface = False
                            navigation = False
                            navigater = False
                    elif upgrade == '2':
                        walletgroupinterface = False
                        navigation = False
                        navigater = False
                    else:
                        print('You might have already upgraded your account or entered an invalid option. Please try again.')
                        walletgroupinterface = False
                        navigation = False
                        navigater = False
                
                elif navigate == '5':
                    home = False
                    navigation = False
                    walletgroupinterface = False
                    navigater = False
                    interface = input('Press 1 for Home, 2 for My Tokens, 3 for Buy Tokens, 4 for Settings, 5 to exit app ')
                    if interface == '1':
                        home = True
                    elif interface == '2':
                        home = False
                        mytokens = True
                    elif interface == '3':
                        home = False
                        buytokens = True
                    elif interface == '4':
                        home = False
                        settings = True
                    elif interface == '5':
                        sys.exit()
                    else:
                        print('Command is invalid. Please try again')
                
                else:
                    print('Invalid. Please try again.')

            #Walletgroup(linked to top)
            while notnewaccount:
                navigater = True
                goinside = input('Which wallet group would you like to enter? Input the name of the wallet group of your choice. Press enter to go back ')
                collaboratelist.clear()
                invisiblecollaboratelist.clear()
                if goinside == '':
                    notnewaccount = False
                if checkifalreadygotcollaborators(email_login,goinside) != 'NULL':
                    collaboratelist.append(checkifalreadygotcollaborators(email_login,goinside))
                    invisiblecollaboratelist.append(checkifalreadygotcollaborators(email_login,goinside))
                    if invisiblecollaboratelist == 'None':
                        invisiblecollaboratelist = invisiblecollaboratelist[0].split(',')

                allwalletnamelist = []
                for original in invisiblename:
                    allwalletnamelist.append(original)
                for added in allowcollabtoaccess(email_login):
                    allwalletnamelist.append(added)
                for wallet_group_name in allwalletnamelist:
                    if goinside == wallet_group_name:
                        print('Wallet group name: ' + str(wallet_group_name))
                        if sameowner(email_login) in getowner(goinside,email_login):
                            print('You are: Owner')
                        else:
                            print('You are: Member')
                        if walletinformation(email_login,goinside)[0][2] != 'NULL':
                            if int(walletinformation(email_login,goinside)[0][2]) >= int(walletinformation(email_login,goinside)[0][0]):
                                print('Congratulations. You have achieved your goal of ' + str(walletinformation(email_login,goinside)[0][0]) + ' tokens with a total of ' + str(walletinformation(email_login,goinside)[0][2]) + ' tokens.')
                            else:
                                print('Goal (in tokens): ' + str(walletinformation(email_login,goinside)[0][2]) + '/' + str(walletinformation(email_login,goinside)[0][0]))
                        else:
                            print('Goal (in tokens): ' + '0' + '/' + str(walletinformation(email_login,goinside)[0][0]))
                        print('Description: ' + walletinformation(email_login,goinside)[0][1])
                        print('Latest Transactions: ')
                        x = 0
                        for history in transactionhistory(goinside,email_login):
                            print(transactionhistory(goinside,email_login)[x][0] + ' contributed ' + transactionhistory(goinside,email_login)[x][1] + ' token(s) on ' + transactionhistory(goinside,email_login)[x][2].replace('  ',' '))
                            x +=1
                            if x == 3:
                                break

                        goinginside = True
                    else:
                        goinginside = False
                    while goinginside:
                        walletgroupinterface = True
                        gooutside = input('Press 1 to go back. Press 2 to view all transaction history. Press 3 to contribute tokens. Press 4 to edit wallet name. Press 5 to edit goal. Press 6 to edit description. Press 7 to view all collaborators. Press 8 to add collaborators (for owners only). Press 9 to chat with your collaborators. ')
                        if gooutside == '1':
                            break                        
                        #Transaction history
                        elif gooutside == '2':
                            y = 0
                            for history in transactionhistory(goinside,email_login):
                                print(transactionhistory(goinside,email_login)[y][0] + ' contributed ' + transactionhistory(goinside,email_login)[y][1] + ' token(s) on ' + transactionhistory(goinside,email_login)[y][2].replace('  ',' '))
                                y +=1
                        #Contribute tokens                            
                        elif gooutside == '3':
                            conttokens = input('How many tokens would you like to contribute? ' )  
                            if (int(conttokens) + int(walletinformation(email_login,goinside)[0][2]) >= int(walletinformation(email_login,goinside)[0][0])):       
                                print('You have already reached the goal. Tokens will not be added inside.')
                            else:
                                contributetokens(email_login,conttokens,goinside)
                        #Edit wallet name
                        elif gooutside == '4':
                            if (sameowner(email_login) in getowner(goinside,email_login)):
                                newname = input('Wallet group name: ')
                                invisiblename[invisiblename.index(goinside)] = newname
                                WGNList[WGNList.index(goinside)] = newname
                                ','.join(WGNList)
                                updateinlist(email_login,goinside,invisiblename)   
                                updatewalletname(newname,email_login,goinside)
                                print('Successful')
                                break
                            else:
                                print('You are just a member. You are not given permission to edit the wallet name')
                        #Edit goal
                        elif gooutside == '5':
                            newgoal = int(input('Goal (in tokens): '))
                            updategoals(newgoal,email_login,goinside)
                            print('Successful')
                        #Edit description
                        elif gooutside == '6':
                            newdescription = input('Description: ')
                            updatedescription(newdescription,email_login,goinside)
                            print('Successful')
                        #View all collaborators
                        elif gooutside == '7':
                            listofcollaboraters = collaboraterscell(goinside,email_login)[0][0].split(',')
                            listofcollaboraters.append(collaboraterscell(goinside,email_login)[0][1])
                            if listofcollaboraters[0] == 'NULL':
                                print("There are no collaborators yet")
                            else:
                                for view in listofcollaboraters:
                                    if acountnamebyemail(email_login) != view:
                                        print(view)
                        #Add collaborators    
                        elif gooutside == '8':
                            collaborate = input('Type in the account ID of the person you want to invite. ')
                            if (collaborators(collaborate)) and (checksame(email_login)[0] != collaborate):
                                if returnnameofperson(collaborate) not in invisiblecollaboratelist:
                                    if sameowner(email_login) in getowner(goinside,email_login):
                                        confirm = input('Press 1 to confirm. Press 2 to decline ')
                                        if confirm == '1':
                                            collaboratelist.append(findcollaborators(collaborate))
                                            collaboratelistconvert = ','.join(collaboratelist)
                                            addcollaborators(collaboratelistconvert, goinside,detectaccountid(email_login))
                                            invisiblecollaboratelist = collaboratelistconvert.split(',')
                                            print('Successful')
                                        elif confirm == '2':
                                            print('Successfully declined')
                                        else:
                                            print('Invalid option. Please try again')
                                    else:
                                        print('You are just a member. You are not given permission to add collaborators')
                                else:
                                    print('You tried to add a collaborator who is already inside. Please try again')
                            else:
                                print('Invalid account or you tried to add yourself. Please try again')

                        #Chat with collaborators
                        elif gooutside == '9':
                            datelist = []
                            textlist = []
                            datelist.clear()
                            textlist.clear()
                            if (retrievedatetext(email_login,goinside)[0][0] != 'NULL' and retrievedatetext(email_login,goinside)[0][1] != 'NULL'):                    
                                textlist.append(retrievedatetext(email_login,goinside)[0][1])
                                datelist.append(retrievedatetext(email_login,goinside)[0][0])
                                textlist = textlist[0].split(',')
                                datelist = datelist[0].split(',')
                                for textdate in textlist:
                                    print(datelist[textlist.index(textdate)])
                                    print(textdate)
                            else:
                                print('No chat history available')

                            text = input('Input text here. Press enter to exit. ')

                            if text == '':
                                notnewaccount = False
                            else:
                                textlist.append(str(getname(email_login)) + ': ' + str(text))
                                datelist.append('[Sent at ' + str(date()) + ']')
                                listtext2 = ','.join(textlist)
                                listdate2 = ','.join(datelist)
                                updatetextdate(email_login,goinside,listtext2,listdate2)
                    
                        else:
                            print('Invalid. Please try again.')            

            #Creation of Wallet groups
            while walletgroupinterface:
                navigater = True
                walletgroup = input("Do you want to create a wallet group? Press n to check out other features in our app (y/n) ")
                if walletgroup.lower() == 'n':
                    break
                elif walletgroup.lower() == 'y':
                    if checkupgrade(email_login)[0][0] == 'Upgrade':
                        wgid = 'w' + str(random.randint(10000,99999))
                        walletgroupname = input("Please enter your wallet group name. Disclaimer: Please note that you can only create 5 wallet groups without subscribing to Premium Definite. ")
                        goal = int(input('What is the amount of tokens needed for this goal? '))
                        description = input('What is the description of this wallet group? ')
                        WalletList.append(wgid)
                        WGNList.append(walletgroupname)
                        invisibleid.append(wgid)
                        invisiblename.append(walletgroupname)

                        walletid = ','.join(WalletList)
                        walletname = ','.join(WGNList)

                        transfertoanothertable(wgid, walletgroupname, email_login, goal, description)
                        wgcreation(str(walletname),str(walletid),email_login)

                    elif len(invisibleid) < 5:
                        wgid = 'w' + str(random.randint(10000,99999))
                        walletgroupname = input("Please enter your wallet group name. Disclaimer: Please note that you can only create 5 wallet groups without subscribing to Premium Definite. ")
                        goal = int(input('What is the amount of tokens needed for this goal? '))
                        description = input('What is the description of this wallet group? ')
                        WalletList.append(wgid)
                        WGNList.append(walletgroupname)
                        invisibleid.append(wgid)
                        invisiblename.append(walletgroupname)

                        walletid = ','.join(WalletList)
                        walletname = ','.join(WGNList)

                        transfertoanothertable(wgid, walletgroupname, email_login, goal, description)
                        wgcreation(str(walletname),str(walletid),email_login)
                        
                    else:
                        print("Please subscribe to our Premium Definite to access even more wallet groups")
                else:
                    print('Please select a valid option')

            while navigater:
                navigater = False
                interface = input('Press 1 for Home, 2 for My Tokens, 3 for Buy Tokens, 4 for Settings, 5 to exit app ')
                if interface == '1':
                    home = True
                elif interface == '2':
                    home = False
                    mytokens = True
                elif interface == '3':
                    home = False
                    buytokens = True
                elif interface == '4':
                    home = False
                    settings = True
                elif interface == '5':
                    sys.exit()
                else:
                    print('Command is invalid. Please try again')
            
        #My tokens    
        while mytokens:
            print('Welcome to My Tokens')
            print('Current Stakes: ')
            w = 0
            currentstakelist.clear()
            completedstakelist.clear()
            for data in gettokendurationinterest(email_login):
                if int(gettokendurationinterest(email_login)[w][6]) > 0:
                    currentstakelist.append(gettokendurationinterest(email_login)[w][0] + ' tokens | ' + gettokendurationinterest(email_login)[w][1] + ' days | ' + gettokendurationinterest(email_login)[w][2] + '% | Remaining days till completion: ' + str(gettokendurationinterest(email_login)[w][6]))
                    print(gettokendurationinterest(email_login)[w][0] + ' tokens | ' + gettokendurationinterest(email_login)[w][1] + ' days | ' + gettokendurationinterest(email_login)[w][2] + '% | Remaining days till completion: ' + str(gettokendurationinterest(email_login)[w][6]))
                if int(gettokendurationinterest(email_login)[w][6]) <= 0:
                    completedstakelist.append(gettokendurationinterest(email_login)[w][0] + ' tokens | ' + gettokendurationinterest(email_login)[w][1] + ' days | ' + gettokendurationinterest(email_login)[w][2] + '% | Maturity date: ' + convertdate(gettokendurationinterest(email_login)[w][5]))
                    if gettokendurationinterest(email_login)[w][6] == None:
                        if checkdate():
                            updatesaverinterest(email_login,(float(gettokendurationinterest(email_login)[w][2]) * 0.01 * int(gettokendurationinterest(email_login)[w][0])), gettokendurationinterest(email_login)[w][4])
                w += 1
            print('')
            print('Completed stakes: ')
            for datacompleted in completedstakelist:
                print(datacompleted)

            selection = input('Select the current stakes you like to view using numbers (starting at 1 for the top). Type "exit" to go back. Type "convert" to look at your completed stakes. ')
            if selection == 'exit':
                mytokens = False
            elif selection == 'convert':
                selectioncomplete = input('Select the completed stakes you like to view using numbers (starting at 1 for the top). Type "exit" to go back. ')
                if selectioncomplete == 'exit':
                    mytokens = False
                else:
                    print('Token Details: ' + str(completedstakelist[int(selectioncomplete) - 1]))
                    print('Amount of Tokens: ' + str(gettokendurationinterestcompleted(email_login)[int(selectioncomplete)-1][0]))
                    print('Duration of stake: ' + str(gettokendurationinterestcompleted(email_login)[int(selectioncomplete)-1][1]))
                    print('Interest awarded: ' + str(float(gettokendurationinterestcompleted(email_login)[int(selectioncomplete)-1][2]) - float(level)) + '%')
                    print('Current tier: ' + str(gettokendurationinterestcompleted(email_login)[int(selectioncomplete)-1][7]))
                    print('Tier benefit: ' + '+' + str(level) + '%')
                    print('Total interest per month : ' + str(gettokendurationinterestcompleted(email_login)[int(selectioncomplete)-1][2]) + '%')
                    print('Date purchased: ' + str(convertdate(gettokendurationinterestcompleted(email_login)[int(selectioncomplete)-1][3])))
                    print('Purchase ID : ' + str(gettokendurationinterestcompleted(email_login)[int(selectioncomplete)-1][4]))
                    print('*Interest will be credited to your account as saver points monthly')

            else:
                print('Token Details: ' + str(currentstakelist[int(selection) - 1]) + '/' + str(gettokendurationinterest(email_login)[int(selection)-1][1]))
                print('Amount of Tokens: ' + str(gettokendurationinterest(email_login)[int(selection)-1][0]))
                print('Duration of stake: ' + str(gettokendurationinterest(email_login)[int(selection)-1][1]))
                print('Interest awarded: ' + str(float(gettokendurationinterest(email_login)[int(selection)-1][2]) - float(level)) + '%')
                print('Current tier: ' + str(gettokendurationinterest(email_login)[int(selection)-1][7]))
                print('Tier benefit: ' + '+' + str(level) + '%')
                print('Total interest per month : ' + str(gettokendurationinterest(email_login)[int(selection)-1][2]) + '%')
                print('Date purchased: ' + str(convertdate(gettokendurationinterest(email_login)[int(selection)-1][3])))
                print('Purchase ID : ' + str(gettokendurationinterest(email_login)[int(selection)-1][4]))
                print('*Interest will be credited to your account as saver points monthly')
                premature = input('Press 1 to prematurely end stake. Press 2 to exit. ')
                if premature == '2':
                    mytokens = False
                elif premature == '1':
                    print('Warning! Premature ending of stakes will sell your tokens at a depreciated value of 1 token = ' + api('SGD', currency.upper(),0.8) + ' ' + currency.upper())
                    proceed = input('Are you sure you want to proceed(y/n) ')
                    if proceed == 'n':
                        mytokens = False
                    elif proceed == 'y':
                        deleterecord(email_login,gettokendurationinterest(email_login)[int(selection)-1][4],gettokendurationinterest(email_login)[int(selection)-1][0])
                        print('Successful')
                    else:
                        print('Invalid. Please try again.')
                else:
                    print('Invalid. Please try again.')

            interface = input('Press 1 for Home, 2 for My Tokens, 3 for Buy Tokens, 4 for Settings, 5 to exit app ')
            if interface == '1':
                home = True
                mytokens = False
            elif interface == '2':
                mytokens = True
            elif interface == '3':
                mytokens = False
                buytokens = True
            elif interface == '4':
                mytokens = False
                settings = True
            elif interface == '5':
                sys.exit()
            else:
                print('Command is invalid. Please try again')
                      
        #Buy Tokens
        while buytokens:
            print('Welcome to Buy Tokens')
            print('Tokens owned: ' + tokensowned(email_login)[0][0])
            print('Exchange rate: 1 Defi token = ' + api('SGD',currency.upper(),1) + ' ' + currency.upper())
            print('You can buy tokens of any amount in 1 SGD denominations, and stake(lock) it for a duration that you prefer. Interests will be credited per month. You would receive your principal at the end of the stake duration.')
            tokenbuy = input('Input the amount of tokens you wish to buy. Type "exit" if you wish to go back ')
            if tokenbuy == 'exit':
                buytokens = False
                paymentscreen = False

            else:
                durationstake = input('How long do you wish to stake these tokens(in days)? ')
                if homesaver(email_login)[0][0] == 'Bronze':
                    tierinterest = bronze
                elif homesaver(email_login)[0][0] == 'Silver':
                    tierinterest = silver
                elif homesaver(email_login)[0][0] == 'Gold':
                    tierinterest = gold
                elif homesaver(email_login)[0][0] == 'Black':
                    tierinterest = black
                
                if int(durationstake) > 9:
                    interestduration = (int(durationstake) * 0.001) + ((int(durationstake[0])) * 0.005)
                else: 
                    interestduration = (int(durationstake) * 0.001)

                intpermonth = round((interestduration + tierinterest),3)

                print('Interest per month: ' + str(intpermonth) + '%')
                print('Added interest : ' + str(tierinterest) + '% (' + str(homesaver(email_login)[0][0]) + ')')
                purchase = input('Confirm? (y/n) Warning: Premature termination of stake will result in a penalty of 1 token = ' + api('SGD',currency.upper(),0.8) + ' ' + currency.upper() + ' ')
                if purchase == 'n':
                    buytokens = False
                    home = True
                elif purchase == 'y':
                    print('Amount payable: ' + api('SGD',currency.upper(),tokenbuy) + ' ' + currency.upper())
                    print('Account No: ' + str(tokensowned(email_login)[0][1]))
                    print('You can scan this QR code using your bank application to purchase')
                    print('*QR code here. Please scan')
                    card = input('Alternatively, you can enter your card details here. Press 1 if you scanned the QR code. Press 2 if you want to enter your card details. ')
                    if card == '1':
                        buytokens = False
                        paymentscreen = True
                    elif card == '2':
                        cardnumber = input('Card Number: ')
                        nameoncard = input('Name on Card: ')
                        expirydate = input('Expiry Date: ')
                        cvv = input('CVV: ')
                        buytokens = False
                        paymentscreen = True
                    else:
                        print('Invalid option. Please try again')
                else:
                    print('Invalid option. Please try again')

            while paymentscreen:
                print('Payment Successful!')
                if tokensowned(email_login)[0][0] == 'NULL':
                    newtokens = int(tokenbuy)
                else:
                    newtokens = int(tokensowned(email_login)[0][0]) + int(tokenbuy)
                print('Tokens owned: ' + str(newtokens))
                print('Tokens credited in this transaction: ' + str(tokenbuy) + ' tokens')
                print('Duration of stake : ' + str(durationstake) + ' Days')
                print('Total interest awarded per month: ' + str(interestduration) + '% + ' + str(tierinterest) + '%')
                purchaseid = 'P' + str(random.randint(10000,99999))
                updatetoken(email_login,newtokens)
                insertpurchasetrans(purchaseid,tokenbuy,durationstake,intpermonth,email_login,homesaver(email_login)[0][0])
                print('Purchase ID: ' + selectpurchaseid(email_login)[0][0])
                print('Interest will be credited to your account as saver points monthly ')
                break

            interface = input('Press 1 for Home, 2 for My Tokens, 3 for Buy Tokens, 4 for Settings, 5 to exit app ')
            if interface == '1':
                home = True
                buytokens = False
            elif interface == '2':
                mytokens = True
                buytokens = False
            elif interface == '3':
                buytokens = True
            elif interface == '4':
                buytokens = False
                settings = True
            elif interface == '5':
                sys.exit()
            else:
                print('Command is invalid. Please try again')

        #Settings
        while settings:
            print('Welcome to Settings')
            print('Name: ' + (getinformation(email_login)[0][0]))
            print('Email Address: ' + (getinformation(email_login)[0][1]))
            print('Account Code: ' + (getinformation(email_login)[0][3]))
            print('Tier Level: ' + (homesaver(email_login)[0][0]))

            question = input('Do you want to edit personal information? (y/n) ')
            if question == 'n':
                interface = input('Press 1 for Home, 2 for My Tokens, 3 for Buy Tokens, 4 for Settings, 5 to exit app ')
                if interface == '1':
                    home = True
                    settings = False
                elif interface == '2':
                    mytokens = True
                    settings = False
                elif interface == '3':
                    buytokens = True
                    settings = False
                elif interface == '4':
                    settings = True
                elif interface == '5':
                    sys.exit()
                else:
                    print('Command is invalid. Please try again')
            
            elif question == 'y':
                print('Which personal information would you like to edit? ')
                which = input('Press 1 to change name. Press 2 to change email. Press 3 to change password ')
                if which == '1':
                    print('Name: ' + (getinformation(email_login)[0][0]))
                    old_name = getinformation(email_login)[0][0]
                    namechange = input('What would you like to change you account name to? ')
                    updateinformationname(namechange, (getinformation(email_login)[0][3]), old_name)
                    for x in updateinformationname(namechange, (getinformation(email_login)[0][3]), old_name):
                        if old_name in x[0]:
                            new = x[0].replace(old_name,namechange)
                            updatecollaborators(new, x[0])
                    for y in nameinchattext():
                        if y[0] != None:
                            if old_name in y[0]:
                                new2 = y[0].replace(old_name, namechange)
                                updatecollaborators2(new2, y[0])
                    print('Successfully updated')

                elif which == '2':
                    print('Your current email address: ' + (getinformation(email_login)[0][1]))
                    emailchange = input('What would you like to change you email to? ')
                    if checksameemailpassoptionemail(emailchange) == []:
                        updateinformationemail(emailchange, (getinformation(email_login)[0][3]))
                        email_login = emailchange
                        print('Successfully updated')
                    else:
                        print('Please choose a different email as what you have chosen has already been used.')

                elif which == '3':
                    print('Your current password: ' + (getinformation(email_login)[0][2]))
                    passwordchange = input('What would you like to change you password to? ')
                    if checksameemailpassoptionpassword(passwordchange) == []:
                        updateinformationpassword(passwordchange, (getinformation(email_login)[0][3]))
                        password_login = passwordchange
                        print('Successfully updated')
                    else:
                        print('Please choose a different password as what you have chosen has already been used. ')
            
            else:
                print('Invalid option. Try again')
