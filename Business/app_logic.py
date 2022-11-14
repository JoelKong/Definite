if __name__ != '__main__':
    from Data_Access.db_query import *
import random
import sys
import datetime
import os
import requests
import json

if __name__ != '__main__':
    conn = create_connection()


def account_info(firstname,lastname,email,password,accid):
    query = """\
        Insert into dbo.Account_information2 values
        ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """ .format(str(accid), firstname + ' ' + lastname, password, email,'0','NULL','NULL','0','Bronze','0','No')
    execute_query_commit(conn, query)

def login(email,password):
    query = """\
            select Email,Password,Account_name
            from dbo.Account_information2
            where Email = '{}' AND Password = '{}'
            """.format(email,password)

    checkinfo = execute_read_query(conn, query)

    for checkeligible in checkinfo:
        if (checkinfo[0][0] in checkeligible[0]) and (checkinfo[0][1] in checkeligible[1]):
            return (True)

def checksameemailpass(email,password):
    query = """\
        select Email,Password
        from dbo.Account_information2
        where Email = '{}' or Password = '{}'
        """.format(email,password)
    append = execute_read_query(conn,query)
    return append

def checksameemailpassoptionemail(email):
    query = """\
        select Email
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query)
    return append

def checksameemailpassoptionpassword(password):
    query = """\
        select Password
        from dbo.Account_information2
        where Password = '{}'
        """.format(password)
    append = execute_read_query(conn,query)
    return append

def homesaver(email):
    query1 = """\
        select Tier_level
        from Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query1)
    return append

def checkname(email,password):
    query = """\
            select Email,Password,Account_name
            from dbo.Account_information2
            where Email = '{}' AND Password = '{}'
            """.format(email,password)

    checkinfo = execute_read_query(conn, query)

    for checkeligible in checkinfo:
        if (checkinfo[0][0] in checkeligible[0]) and (checkinfo[0][1] in checkeligible[1]):
            return checkeligible[2]

def savertoken(email,password):
    query = """\
            select Account_balance,Saver_points
            from dbo.Account_information2
            where Email = '{}' AND Password = '{}'
            """.format(email,password)

    checkinfo = execute_read_query(conn, query)
    return checkinfo

def wgcreation(wgname,walletid,email):
    query = """\
        select Account_id
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    checkcorrect = execute_read_query(conn, query)
    checkfilter = checkcorrect[0][0]

    query = """\
        UPDATE dbo.Account_information2
        SET WalletGroup_name ='{}', Walletgroup_id ='{}'
        where Account_id = '{}'
        """ .format(wgname,walletid,checkfilter)
    execute_query_commit(conn, query)

def detectaccountid(email):
    query = """\
        select Account_id
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    checkcorr = execute_read_query(conn, query)
    checkfilter2 = checkcorr[0][0]
    return checkfilter2

def appendlist(email):
    query = """\
            select Walletgroup_id
            from dbo.Account_information2
            where Email = '{}'
            """.format(email)

    append = execute_read_query(conn, query)

    for checkappend in append:
        return (checkappend[0].strip())

def appendlistname(email):
    query = """\
            select Walletgroup_name
            from dbo.Account_information2
            where Email = '{}'
            """.format(email)

    append = execute_read_query(conn, query)
    for checkappend in append:
        return (checkappend[0].strip())

def transfertoanothertable(walletid,walletname,email,goal,description):
    query = """\
        select Account_id,Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    checkcorrect = execute_read_query(conn, query)

    query2 = """\
        Insert into dbo.Wallet_group values
        ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(checkcorrect[0][0], checkcorrect[0][1],walletname,walletid,goal,'NULL',description,'0','NULL','NULL')
    execute_query_commit(conn, query2)

def walletinformation(email,wallet_name):
    query1 = """\
        select Account_id,Email,Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    checkemail = execute_read_query(conn,query1)
    
    query = """\
            select Goals,Description,Tokens_contributed
            from dbo.Wallet_group
            where (Account_id = '{}' AND Walletgroup_name = '{}') OR (Collaborators like '%{}%' AND Walletgroup_name = '{}')
            """.format(checkemail[0][0],wallet_name,checkemail[0][2],wallet_name)

    checkinfo = execute_read_query(conn, query)
    return checkinfo

def updategoals(newgoal,email,wallet_name):
    query1 = """\
        select Account_id,Email,Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    checkemail = execute_read_query(conn,query1)
    
    query = """\
        UPDATE dbo.Wallet_group
        SET Goals ='{}'
        where (Collaborators like '%{}%' AND Walletgroup_name = '{}') OR (Account_id = '{}' AND Walletgroup_name = '{}')
        """ .format(newgoal,checkemail[0][2],wallet_name,checkemail[0][0],wallet_name)
    execute_query_commit(conn, query)

def updatedescription(newdescription,email,wallet_name):
    query1 = """\
        select Account_id,Email,Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    checkemail = execute_read_query(conn,query1)
    
    query = """\
        UPDATE dbo.Wallet_group
        SET Description ='{}'
        where (Collaborators like '%{}%' AND Walletgroup_name = '{}') OR (Account_id = '{}' AND Walletgroup_name = '{}')
        """ .format(newdescription,checkemail[0][2],wallet_name,checkemail[0][0],wallet_name)
    execute_query_commit(conn, query)

def updatewalletname(newname,email,wallet_name):
    query1 = """\
        select Account_id,Email,Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    checkemail = execute_read_query(conn,query1)
    
    query = """\
        UPDATE dbo.Wallet_group
        SET Walletgroup_name ='{}'
        where (Collaborators like '%{}%' AND Walletgroup_name = '{}') OR (Account_id = '{}' AND Walletgroup_name = '{}')
        """ .format(newname,checkemail[0][2],wallet_name,checkemail[0][0],wallet_name)
    execute_query_commit(conn, query)

def getowner(wallet_name,email):
    query1 = """\
        select Account_id,Email,Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    checkemail = execute_read_query(conn,query1)    

    query = """\
        select Account_name 
        from dbo.Wallet_group
        where Collaborators not like '%{}%' AND Walletgroup_name = '{}'
        """ .format(checkemail[0][2],wallet_name)
    check = execute_read_query(conn, query)
    if check == []:
        getownerlist = []
        return (getownerlist)
    else:
        y = 0
        getownerlist = []
        getownerlist.clear()
        for x in check:
            getownerlist.append(check[y][0])
            y += 1
        return(getownerlist)

def sameowner(email):
    query = """\
            select Email,Password,Account_name
            from dbo.Account_information2
            where Email = '{}'
            """.format(email)
    check = execute_read_query(conn, query)
    return (check[0][2])

def collaborators(person):
    query = """\
            select Account_id, Account_name
            from dbo.Account_information2
            where Account_id = '{}'
            """.format(person)

    checkinfo = execute_read_query(conn, query)

    for checkeligible in checkinfo:
        if (checkinfo[0][0] in checkeligible[0]):
            print("You are going to invite " + str(checkeligible[1]))
            return True

def checksame(email):
    query = """\
            select Account_id
            from dbo.Account_information2
            where Email = '{}'
            """.format(email)

    checkinfo = execute_read_query(conn, query)
    for checkeligible in checkinfo:
            return checkeligible

def findcollaborators(personadded):
    query1 = """\
        select Account_name
        from dbo.Account_information2
        where Account_id = '{}'
        """.format(personadded)
    checkemail = execute_read_query(conn,query1)
    return(checkemail[0][0])

def addcollaborators(currentlist,walletname,senderaccid):
    query = """\
        UPDATE dbo.Wallet_group
        SET Collaborators ='{}'
        where Walletgroup_name = '{}' and Account_id = '{}'
        """ .format(currentlist,walletname,senderaccid)
    execute_query_commit(conn, query)  

def checkifalreadygotcollaborators(email,walletname):
    query = """\
            select Account_id
            from dbo.Account_information2
            where Email = '{}'
            """.format(email)
    append = execute_read_query(conn, query)

    query2 = """\
            select Collaborators
            from dbo.Wallet_group
            where Walletgroup_name = '{}' and Account_id = '{}'
            """.format(walletname, append[0][0])
    append2 = execute_read_query(conn, query2)
    for checkappend in append2:
        return (checkappend[0].strip())    

def returnnameofperson(person):
    query = """\
            select Account_id, Account_name
            from dbo.Account_information2
            where Account_id = '{}'
            """.format(person)

    checkinfo = execute_read_query(conn, query)
    return (checkinfo[0][1])

def collabprint(email,wallet_name):
    query = """\
            select Account_id
            from dbo.Account_information2
            where Email = '{}'
            """.format(email)
    append = execute_read_query(conn, query)

    query2 = """\
            select Collaborators
            from dbo.Wallet_group
            where Account_id = '{}' and Walletgroup_name = '{}'
            """.format(append[0][0],wallet_name)
    append2 = execute_read_query(conn, query2)
    for checkappend in append2:
        return (checkappend[0]) 

def updateinlist(email,goinside,invisiblename):

    invisiblename = ','.join(invisiblename)

    query2 = """\
            select Account_id, Account_name
            from dbo.Account_information2
            where Email = '{}'
            """.format(email)
    checkemail2 = execute_read_query(conn,query2)

    query1 = """\
            select Account_id
            from dbo.Wallet_group
            where (Collaborators like '%{}%' AND Walletgroup_name = '{}') OR (Account_id = '{}' AND Walletgroup_name = '{}')
            """.format(checkemail2[0][1], goinside, checkemail2[0][0], goinside)
    checkemail = execute_read_query(conn,query1)
    
    query = """\
        UPDATE dbo.Account_information2
        SET Walletgroup_name ='{}'
        where Account_id = '{}'
        """ .format(invisiblename,checkemail[0][0])
    execute_query_commit(conn, query)

def loopthroughcollaborator(email):
    printalllist = []
    query = """\
            select Account_name
            from dbo.Account_information2
            where Email = '{}'
            """.format(email)
    append = execute_read_query(conn, query)

    query3 = """\
        select Walletgroup_name,Collaborators
        from dbo.Wallet_group
        where Collaborators like '%{}%'
        """.format(append[0][0])
    append3 = execute_read_query(conn, query3)

    x = 0
    for printall in append3:
        printalllist = append3[x][1].split(',')
        number = len(printalllist)
        print(str(append3[x][0]) +  ' + (' + str(number) + ')')
        x += 1
    
def allowcollabtoaccess(email):
    listadded = []
    query = """\
            select Account_name
            from dbo.Account_information2
            where Email = '{}'
            """.format(email)
    append = execute_read_query(conn, query)

    query3 = """\
        select Walletgroup_name
        from dbo.Wallet_group
        where Collaborators like '%{}%'
        """.format(append[0][0])
    append3 = execute_read_query(conn, query3)

    for allow in append3:
        listadded.append(allow[0])
    return(listadded)

def contributetokens(email,amount,wallet_name):
    query = """\
            select Account_name,Account_id,Account_balance
            from dbo.Account_information2
            where Email = '{}'
            """.format(email)
    append = execute_read_query(conn, query)   

    if int(amount) > int(append[0][2]):
        print('You do not have enough tokens to contribute this amount. Please try again.')
    else:
        query1 = """\
            select Tokens_contributed,Walletgroup_id
            from dbo.Wallet_group
            where (Account_id = '{}' and Walletgroup_name = '{}') or (Collaborators like '%{}%' AND Walletgroup_name = '{}')
            """.format(append[0][1], wallet_name, append[0][0], wallet_name)
        append2 = execute_read_query(conn, query1)
        
        if append2[0][0] == 'NULL':
            x = int(0)
        else:
            x = int(append2[0][0])

        query2 = """\
            UPDATE dbo.Wallet_group
            Set Tokens_contributed = '{}'
            where (Account_id = '{}' and Walletgroup_name = '{}') or (Collaborators like '%{}%' AND Walletgroup_name = '{}') 
            """.format(int(x) + int(amount),append[0][1], wallet_name, append[0][0], wallet_name)
        append3 = execute_query_commit(conn, query2)

        query3 = """\
            UPDATE dbo.Account_information2
            Set Account_balance = '{}'
            where Email = '{}'
            """.format(int(append[0][2])-int(amount),email)
        append4 = execute_query_commit(conn,query3)
        print('Successful')

        query4 = """\
            Insert into dbo.Transaction_history2 values
            ('{}','{}','{}','{}','{}',GETDATE())
            """ .format(wallet_name,append2[0][1],append[0][1],append[0][0],amount)
        execute_query_commit(conn, query4)

def transactionhistory(walletname,email):
    query1 = """\
        Select Account_name,Account_id
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query1)

    query2 = """\
        Select Walletgroup_id
        from dbo.Wallet_group
        where (Walletgroup_name = '{}' and Account_name = '{}') or (Collaborators like '%{}%' AND Walletgroup_name = '{}')
        """.format(walletname,append[0][0],append[0][0],walletname)
    append2 = execute_read_query(conn,query2)

    query3 = """\
            Select Account_name,Tokens_contributed,Transaction_datetime
            from dbo.Transaction_history2
            where Walletgroup_id = '{}'
            order by Transaction_datetime DESC
            """.format(append2[0][0])
    append3 = execute_read_query(conn,query3)
    return append3

def collaboraterscell(walletname,email):
    query1 = """\
        Select Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query1)

    query2 = """\
        Select Walletgroup_id
        from dbo.Wallet_group
        where (Walletgroup_name = '{}' and Account_name = '{}') or (Collaborators like '%{}%' AND Walletgroup_name = '{}')
        """.format(walletname,append[0][0],append[0][0],walletname)
    append2 = execute_read_query(conn,query2)

    query3 = """\
            Select Collaborators,Account_name
            from dbo.Wallet_group
            where Walletgroup_id = '{}'
            """.format(append2[0][0])
    append3 = execute_read_query(conn,query3)
    return append3

def tokensowned(email):
    query = """\
        Select Account_balance, Account_id
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query)
    return append

def updatetoken(email,token):
    query = """\
        UPDATE dbo.Account_information2
        Set Account_balance = '{}'
        where Email = '{}'
        """.format(token,email)
    append = execute_query_commit(conn,query)

def insertpurchasetrans(purchaseid,token,durationstake,intpermonth,email,level):
    query1 = """\
        Select Account_id,Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query1)

    query2 = """\
        Insert into dbo.Token_purchase values
        ('{}','{}','{}','{}',GETDATE(),'{}',dateadd(day,convert(int,'{}'),getdate()),'{}',NULL,'{}')
        """ .format(append[0][0],append[0][1],purchaseid,token,durationstake,durationstake,intpermonth,level)
    execute_query_commit(conn, query2)    

def selectpurchaseid(email):
    query = """\
        Select Account_id
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query)

    query2 = """\
        Select Purchase_id
        from dbo.Token_purchase
        where Account_id = '{}' and dateadd(second,5,Initial_stake_date) >= getdate()
        """.format(append[0][0])
    append2 = execute_read_query(conn,query2)
    return append2

def gettokendurationinterest(email):
    query1 = """\
        Select Account_id
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query1)

    query2 = """\
        Select Tokens_staked, Duration_of_stake,Total_interest_per_month,Initial_stake_date,Purchase_id,Ending_stake_date,datediff(day,replace(convert(date,getdate()),'-','/'),replace(convert(date,Ending_stake_date),'-','/')),Tier_level_when_stake
        from dbo.Token_purchase
        where Account_id = '{}'
        order by Ending_stake_date DESC
        """.format(append[0][0])
    append2 = execute_read_query(conn,query2)
    return append2

def remainingdays2(purchaseid):
    query2 = """\
        select datediff(day,replace(convert(date,getdate()),'-','/'),replace(convert(date,Ending_stake_date),'-','/'))
        from Token_purchase
        where Purchase_id = '{}' 
        """.format(purchaseid)
    append2 = execute_read_query(conn,query2)
    return append2

def remainingdays(email):
    query1 = """\
        select Account_id
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query1)

    query2 = """\
        select datediff(day,replace(convert(date,getdate()),'-','/'),replace(convert(date,Ending_stake_date),'-','/'))
        from dbo.Token_purchase
        where Account_id = '{}' 
        """.format(append[0][0])
    append2 = execute_read_query(conn,query2)
    return append2

def convertdate(date):
    query = """\
        select datename(dd,'{}'),datename(mm,'{}'),datename(yy,'{}')
        """.format(date,date,date)
    query = execute_read_query(conn,query)
    return str(query[0][0]) + ' '+ str(query[0][1]) + ' ' + str(query[0][2])

def gettokendurationinterestcompleted(email):
    query1 = """\
        Select Account_id
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query1)

    query2 = """\
        Select Tokens_staked, Duration_of_stake,Total_interest_per_month,Initial_stake_date,Purchase_id,Ending_stake_date,Completed_date,Tier_level_when_stake
        from dbo.Token_purchase
        where Account_id = '{}' and convert(date,getdate()) >= convert(date,Ending_stake_date)
        order by Ending_stake_date DESC
        """.format(append[0][0])
    append2 = execute_read_query(conn,query2)
    return append2

def deleterecord(email,id,tokens):
    query = """\
        Delete from dbo.Token_purchase
        where Purchase_id = '{}'
        """.format(id)
    execute_query_commit(conn,query)

    query2 = """\
        select Account_balance
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append1 = execute_read_query(conn,query2)

    query3 = """\
        UPDATE dbo.Account_information2
        Set Account_balance = '{}'
        where Email = '{}'
        """.format((int(append1[0][0]) - int(tokens)), email)
    execute_query_commit(conn,query3)

def updatesaverinterest(email,saverpoints,purchaseid):
    query1 = """\
        Select Account_id,Saver_points
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query1)

    query2 = """\
        Update dbo.Token_purchase
        Set Completed_date = GETDATE()
        where Account_id = '{}' and Purchase_id = '{}'
        """.format(append[0][0],purchaseid)
    execute_query_commit(conn,query2)

    if append[0][1] != 'NULL':
        query3 = """\
            Update dbo.Account_information2
            Set Saver_points = '{}'
            where Account_id = '{}'
            """.format(saverpoints + float(append[0][1]),append[0][0])
        execute_query_commit(conn,query3)
    else:
        query4 = """\
            Update dbo.Account_information2
            Set Saver_points = '{}'
            where Account_id = '{}'
            """.format(saverpoints,append[0][0])
        execute_query_commit(conn,query4)

def checkdate():
    query = """\
        select DAY(getdate())
        """
    append = execute_read_query(conn, query)

    if append[0][0] == 1:
        return(True)
    else:
        return(False)

def getinitialminusone(email):
    query = """\
        Select Account_id
        from Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query)

    query2 = """\
        Select DAY(Initial_stake_date) - 1
        from dbo.Token_purchase
        where Account_id = '{}'
        """.format(append[0][0])

    append2 = execute_read_query(conn,query2)
    return append2

def saverpointsspent(email):
    query = """\
        select Saver_points_spent
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query)
    return append[0][0]

def updatesaver(email,amount,amountspent):
    query = """\
        Update dbo.Account_information2
        Set Saver_points_spent = '{}',Saver_points = '{}'
        where Email = '{}'
        """.format(amountspent,amount,email)
    execute_query_commit(conn,query)

def updatetier(email,tier):
    query = """\
        Update dbo.Account_information2
        Set Tier_level = '{}'
        where Email = '{}'
        """.format(tier,email)
    execute_query_commit(conn,query)

def getinformation(email):
    query = """\
        select Account_name, Email, Password, Account_id
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query)
    return (append)

def updateinformationemail(changed_email, accountid):
    query = """\
        Update dbo.Account_information2
        Set Email = '{}'
        where Account_id = '{}'
        """.format(changed_email, accountid)
    execute_query_commit(conn, query)

def updateinformationpassword(change_password, accountid):
    query = """\
        Update dbo.Account_information2
        Set Password = '{}'
        where Account_id = '{}'
        """.format(change_password, accountid)
    execute_query_commit(conn, query)

def updateinformationname(change_name, accountid, oldname):
    query = """\
        Update dbo.Account_information2
        Set Account_name = '{}'
        where Account_id = '{}'
        """.format(change_name, accountid)
    execute_query_commit(conn, query)

    query1 = """\
        Update dbo.Token_purchase
        Set Account_name = '{}'
        where Account_name = '{}'
        """.format(change_name,oldname)
    execute_query_commit(conn, query1)

    query2 = """\
        Update dbo.Transaction_history2
        Set Account_name = '{}'
        where Account_name = '{}'
        """.format(change_name,oldname)
    execute_query_commit(conn, query2)

    query3 = """\
        Update dbo.Wallet_group
        Set Account_name = '{}'
        where Account_name = '{}'
        """.format(change_name,oldname)
    execute_query_commit(conn, query3)

    query4 = """\
        select Collaborators
        from dbo.Wallet_group
        """
    append4 = execute_read_query(conn, query4)
    return(append4)

def updatecollaborators(change_name, oldname):
    query5 = """\
        Update dbo.Wallet_group
        Set Collaborators = '{}'
        where Collaborators = '{}'
        """.format(change_name, oldname)
    execute_query_commit(conn, query5)

def nameinchattext():
    query = """\
        select Chat_text
        from dbo.Wallet_group
        """
    append = execute_read_query(conn, query)
    return (append)

def updatecollaborators2(change_name, oldname):
    query2 = """\
        Update dbo.Wallet_group
        Set Chat_text = '{}'
        where Chat_text = '{}'
        """.format(change_name, oldname)
    execute_query_commit(conn, query2)

def acountnamebyemail(email):
    query = """\
        select Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn, query)
    return append[0][0]

def date():
    query = """\
        select convert(datetime,getdate())
        """
    append = execute_read_query(conn,query)
    return append[0][0]

def getname(email):
    query = """\
        select Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query)
    return append[0][0]

def retrievedatetext(email,walletname):
    query = """\
        select Account_id,Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query)

    query2 = """\
        select Chat_date,Chat_text
        from dbo.Wallet_group
        where (Account_id = '{}' and Walletgroup_name = '{}') or (Collaborators like '%{}%' AND Walletgroup_name = '{}')
        """.format(append[0][0],walletname,append[0][1],walletname)
    append2 = execute_read_query(conn,query2)
    return append2

def updatetextdate(email,wallet_name,text,date):
    query = """\
        select Account_id,Account_name
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query)

    query2 = """\
        Update dbo.Wallet_group
        Set Chat_date = '{}'
        where (Account_id = '{}' and Walletgroup_name = '{}') or (Collaborators like '%{}%' AND Walletgroup_name = '{}')
        """.format(date,append[0][0],wallet_name,append[0][1],wallet_name)
    execute_query_commit(conn,query2)

    query3 = """\
        Update dbo.Wallet_group
        Set Chat_text = '{}'
        where (Account_id = '{}' and Walletgroup_name = '{}') or (Collaborators like '%{}%' AND Walletgroup_name = '{}')
        """.format(text,append[0][0],wallet_name,append[0][1],wallet_name)
    execute_query_commit(conn,query3)

def upgradeaccount(email,upgrade):
    query = """\
        Update dbo.Account_information2
        Set Upgrade_account = '{}'
        where Email = '{}'
        """.format(upgrade,email)
    execute_query_commit(conn,query)

def checkupgrade(email):
    query = """\
        select Upgrade_account
        from dbo.Account_information2
        where Email = '{}'
        """.format(email)
    append = execute_read_query(conn,query)
    return append

#API(local testing)
if __name__ == '__main__':
    url = "https://currency-converter5.p.rapidapi.com/currency/convert"
    querystring = {"format":"json","from":"SGD","to":"JPY","amount":"10"}

    headers = {
        'x-rapidapi-host': "currency-converter5.p.rapidapi.com",
        'x-rapidapi-key': "a57fa5904dmsh9afc0d45af51316p191bd4jsn172333859512"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    results = response.json()
    print(str(results['amount']) + ' ' + str(results['base_currency_name']) + '(s) equals to ' + str(results['rates']['JPY']['rate_for_amount']) + ' ' + str(results['rates']['JPY']['currency_name']))

#API(to be used in presentation layer)
def api(base,converto,amount):
    url = "https://currency-converter5.p.rapidapi.com/currency/convert"
    querystring = {"format":"json","from":base,"to":converto,"amount":amount}

    headers = {
        'x-rapidapi-host': "currency-converter5.p.rapidapi.com",
        'x-rapidapi-key': "a57fa5904dmsh9afc0d45af51316p191bd4jsn172333859512"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    results = response.json()
    return results['rates'][converto]['rate_for_amount']
    