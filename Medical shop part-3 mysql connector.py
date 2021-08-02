import mysql.connector as sqltor
def AddRecord():
    connection = sqltor.connect(host='localhost',database='prady',user='root',password='admin')
    cursor = connection.cursor()
    if connection.is_connected():
        print('COnnected')
    
    mnum =int(input('Enter  Medicine Number :'))
    name=input('Enter Medicine Name: ')
    price=int(input('Enter Price :'))
    qty=int(input('Enter Quantity:'))
    
    detail=(name,price,qty,mnum)
    mySql_insert_query = """INSERT INTO medicine (name_of_medicine,price,quantity,sno) 
                                VALUES (%s,%s,%s,%s) """

    recordTuple = (detail)
    cursor.execute(mySql_insert_query, recordTuple)
    connection.commit()
    print("Record inserted successfully into table")
#----------------------------------------------------------------------------------------------
def Display():
    connection = sqltor.connect(host='localhost',database='prady',user='root',password='admin')
    cursor = connection.cursor()
        
    sql_select_Query = "select * from medicine"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
        print(row[3],row[0],row[1],row[2], sep="\t")
#----------------------------------------------------------------------------------------------
def DelRecord():
    connection = sqltor.connect(host='localhost',database='prady',user='root',password='admin')
    cursor = connection.cursor()
    name=input("Enter the medicine name to be deleted")
    detail=(name,)
    mySql_delete_query = "delete from medicine where name_of_medicine=%s" 
    recordTuple = (detail)
    cursor.execute(mySql_delete_query, recordTuple)
    connection.commit()
    print("Record deleted successfully into table")                          

#----------------------------------------------------------------------------------------------
def UpdateRecord():
    connection = sqltor.connect(host='localhost',database='prady',user='root',password='admin')
    cursor = connection.cursor()
    print("---------- Sub Menu----------------------")
    print("           1 Price")
    print("           2 Quantity")
    print("           3 Medicine")
    print("--------------------------------------------")
    ch=int(input("enter your  choice :"))
    name=input("Enter the medicine name :")
    if ch==1 :
        p=int(input("enter the new price of medicine:"))
        detail=(p,name)
        mySql_update_query = "update medicine set price=%s where  name_of_medicine=%s" 
        recordTuple = (detail)
        cursor.execute(mySql_update_query, recordTuple)
        connection.commit()
    
       
    elif ch==2 :
        q=int(input("Enter the quantity of medicne"))
        detail2=(q,name)
        mySql_update_query="update medicine set quantity=%s where name_of_medicine=%s"
        recordTuple1 = (detail2)
        cursor.execute(mySql_update_query, recordTuple1)
        connection.commit()
        
    elif ch==3:
        name2=input("Enter correct name of the medicine")
        detail3=(name2,name)
        mysql_update_query="update medicine set name_of_medicine=%s where name_of_medicine=%s"
        recordTuple2 = (detail3)
        cursor.execute(mySql_update_query, recordTuple2)
        connection.commit()
    ques=input("Do you want to continue or not(y/n):")
    while ques == 'y':
        continue
    
    print("Record update successfully into table")  
#----------------------------------------------------------------------------------------------
def finalprice():
    connection = sqltor.connect(host='localhost',database='prady',user='root',password='admin')
    cursor = connection.cursor()
    name=input("Enter the name of the medicine you want to buy")
    quantity=int(input("Enter the uantity of medicine you wat to buy")





                 
    detail=(name,)
               
        
    sql_select_Query = "select price from medicine where name=%s"
    recordTuple
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    
#-------------------------MAIN-------------------------------------------------------------    
print("""

                                 ..........................................................................................................................................
                                 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                 ....................WELCOME TO THIS MEDI-SHOP SOFTWARE.................................
                                 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                 <<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                 ..........................................................................................................................................

""")
##the main loop starts
ans='y'
while(ans=='y'):

    print("""
             1=ADD MEDICINE
             2=SELL MEDICINE
             3=DETAILS OF OLD STOCK
             4=DELETE MEDICINE(NOTE:YOU CAN DELETE THOSE MEDICINES THAT ARE EXPIRED OR DAMAGED)
             5=EDIT MEDICINE DETAILS
             6=EXIT""")
    choice=int(input("enter your choice :"))
    if choice==1:
        AddRecord()
    elif choice==3:
        Display()
    elif choice==4:
        DelRecord()
    elif choice==5:
        UpdateRecord()
    elif choice==6:
        print("Thank you for using the program")
        break
    else:
        print("Invalid Choice, Valid is 1-6")
    ans=input("Wish to conitnue y/n :")
    

  
