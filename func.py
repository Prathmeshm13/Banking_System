import mysql.connector
from datetime import date

def clear():
    for _ in range(65):
        print()

def account_status(Account_No):
    conn = mysql.connector.connect(
        host='localhost', database='bankdb', user='sqluser', password='Prathmesh@13')
    cursor = conn.cursor()
    sql = "SELECT Status, Balance FROM customer WHERE Account_No = %s"
    cursor.execute(sql, (Account_No,))
    result = cursor.fetchone()
    conn.close()
    return result

def deposit_amount():
    conn = mysql.connector.connect(
        host='localhost', database='bankdb', user='sqluser', password='Prathmesh@13')
    cursor = conn.cursor()
    clear()
    Account_No = input('Enter Account No.: ')
    Amount = input('Enter Amount: ')
    today = date.today()
    result = account_status(Account_No)
    if result and result[0] == 'Active':
        sql1 = "UPDATE customer SET Balance = Balance + %s WHERE Account_No = %s AND Status = 'Active'"
        sql2 = 'INSERT INTO transaction (Amount, Transaction_Type, Account_No, Date_Of_Transaction) VALUES (%s, "deposit", %s, %s)'
        cursor.execute(sql2, (Amount, Account_No, today))
        cursor.execute(sql1, (Amount, Account_No))
        conn.commit()
        print('\n\nAmount Deposited')
    else:
        print('\n\nClosed or Suspended Account....')
    wait = input('\n\nPress any key to continue')
    conn.close()

def withdraw_amount():
    conn = mysql.connector.connect(
        host='localhost', database='bankdb', user='sqluser', password='Prathmesh@13')
    cursor = conn.cursor()
    clear()
    Account_No = input('Enter Account No: ')
    Amount = input('Enter Amount: ')
    today = date.today()
    result = account_status(Account_No)
    if result and result[0] == 'Active' and int(result[1]) >= int(Amount):
        sql1 = "UPDATE customer SET Balance = Balance - %s WHERE Account_No = %s AND Status = 'Active'"
        sql2 = 'INSERT INTO transaction (Amount, Transaction_Type, Account_No, Date_Of_Transaction) VALUES (%s, "withdraw", %s, %s)'
        cursor.execute(sql2, (Amount, Account_No, today))
        cursor.execute(sql1, (Amount, Account_No))
        conn.commit()
        print('\n\nAmount Withdrawn')
    else:
        print('\n\nClosed or Suspended Account or Insufficient Amount')
    wait = input('\n\nPress any key to continue......')
    conn.close()

def transaction_menu():
    while True:
        clear()
        print('Transaction Menu')
        print("\n1. Deposit Amount")
        print('\n2. Withdraw Amount')
        print('\n3. Back to Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice.....:'))
        if choice == 1:
            deposit_amount()
        if choice == 2:
            withdraw_amount()
        if choice == 3:
            break
def search_menu():
    conn = mysql.connector.connect(
        host='localhost', database='bankdb', user='sqluser', password='Prathmesh@13')
    cursor = conn.cursor()

    while True:
        clear()
        print('Search Menu')
        print("\n1. Account No")
        print("\n2. Aadhar Card No.")
        print("\n3. Phone No.")
        print("\n4. Email")
        print("\n5. Name")
        print("\n6. Back to Main Menu")
        
        choice = int(input('Enter your choice...:'))
        field_name = ''
        
        if choice == 1:
            field_name = 'Account_No'
        if choice == 3:
            field_name = '`Phone No.`'
        if choice == 4:
            field_name = '`Email ID`'
        if choice == 5:
            field_name = 'Name'
        if choice == 2:
            field_name = 'Aadhar No.'
        if choice == 6:
            break
        
        msg = 'Enter ' + field_name + ': '
        value = input(msg)
        
        if field_name == 'Account_No':
            sql = 'SELECT * FROM customer WHERE ' + field_name + ' = %s;'
        else:
            sql = 'SELECT * FROM customer WHERE ' + field_name + ' LIKE %s;'
            value = "%" + value + "%"  
        
        cursor.execute(sql, (value,))
        records = cursor.fetchall()
        n = len(records)
        clear()
        print('Search Result for', field_name, '', value)
        print('-' * 80)
        for record in records:
            print(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8])
        
        if n <= 0:
            print(field_name, '', value, 'does not exist')
        
        wait = input('\n\n\nPress any key to continue.....')
    
    conn.close()
    wait = input('\n\n\nPress any key to continue.....')


def account_details():
    clear()
    Account_No=input('Enter Account_No')
    conn = mysql.connector.connect(
        host='localhost', database='bankdb', user='sqluser', password='Prathmesh@13')
    cursor = conn.cursor()
    sql='Select * from customer where Account_No='+Account_No+';'
    sql1='Select TransactionID ,Date_Of_Transaction,Amount,Transaction_Type from transaction t where t.Account_No='+Account_No+';'
    cursor.execute(sql)
    result=cursor.fetchone()
    clear()
    print("Account Details")
    print('-'*120)
    print('Account No:',result[0])
    print('Customer Name:',result[1])
    print('Address:',result[2])
    print('Phone No.:',result[3])
    print('Email ID:',result[4])
    print('Aadhar No:',result[5])
    print('Account Type:',result[6])
    print('Account Status:',result[7])
    print('Current Balance:',result[8])
    print('-'*120)
    cursor.execute(sql1)
    results=cursor.fetchall()
    for result in results:
        print(result[0],result[1],result[2],result[3])
    
    conn.close()
    wait=input('\n\n\n Press any key to continue.....')

def add_account():
    conn = mysql.connector.connect(
        host='localhost', database='bankdb', user='sqluser', password='Prathmesh@13')
    cursor = conn.cursor()
    
    name = input('Enter Name: ')
    addr = input('Enter Address: ')
    phno = input('Enter Phone Number: ')
    email = input('Enter Email Address: ')
    aadhar = input('Enter Aadhar No: ')
    accnttype = input('Account type (saving/current): ')
    balance = input('Enter Opening balance: ')
    sql = 'INSERT INTO customer (`Name`, `Address`, `Phone No.`, `Email ID`, `Aadhar No.`, `Account_type`, `Balance`, `Status`) VALUES (%s, %s, %s, %s, %s, %s, %s, "Active")'
    cursor.execute(sql, (name, addr, phno, email, aadhar, accnttype, balance))
    print('\n\nNew Account Created Successfully')
    wait = input('\n\nPress any key to continue...')
    conn.commit()
    conn.close()

def modify_account():
    conn = mysql.connector.connect(
        host='localhost', database='bankdb', user='sqluser', password='Prathmesh@13')
    cursor = conn.cursor()
    clear()
    Account_No = input('Enter Account No: ')
    print('Modify Screen')
    print('\n1. Customer Name')
    print('\n2. Customer Address')
    print('\n3. Customer Phone No.')
    print('\n4. Customer Email Id')
    choice = int(input('What do you want to change?'))
    new_data = input('Enter New value: ')
    field_name = ''
    if choice == 1:
        field_name = 'Name'
    if choice == 2:
        field_name = 'Address'
    if choice == 3:
        field_name = 'Phone No.'
    if choice == 4:
        field_name = 'Email ID'
    
    if choice == 4:
        sql = 'UPDATE customer SET `Email ID` = %s WHERE Account_No = %s'
        cursor.execute(sql, (new_data, Account_No))
    elif choice ==3:
        sql = 'UPDATE customer SET `Phone No.` = %s WHERE Account_No = %s'
        cursor.execute(sql, (new_data, Account_No))
    else:
        sql = 'UPDATE customer SET ' + field_name + ' = %s WHERE Account_No = %s'
        cursor.execute(sql, (new_data, Account_No))
    print('\n\nCustomer Information Modified...')
    wait = input('\n\nPress any key to continue....')
    conn.commit()
    conn.close()

def close_account():
    conn = mysql.connector.connect(
        host='localhost', database='bankdb', user='sqluser', password='Prathmesh@13')
    cursor = conn.cursor()
    clear()
    Account_No = input('Enter Account No: ')
    sql = 'UPDATE customer SET Status = "Closed" WHERE Account_No = %s'
    cursor.execute(sql, (Account_No,))
    print('\n\nAccount Closed')
    wait = input('\n\nPress any key to continue....')
    conn.commit()
    conn.close()

def activate_account():
    conn = mysql.connector.connect(
        host='localhost', database='bankdb', user='sqluser', password='Prathmesh@13')
    cursor = conn.cursor()
    clear()
    Account_No = input('Enter Account No: ')
    sql = 'UPDATE customer SET Status = "Active" WHERE Account_No = %s'
    cursor.execute(sql, (Account_No,))
    print('\n\nAccount Activated')
    wait = input('\n\nPress any key to continue....')
    conn.commit()
    conn.close()

def main_menu():
    while True:
        clear()
        print('Main Menu')
        print("\n1. Add Account")
        print("\n2. Modify Account")
        print("\n3. Close Account")
        print("\n4. Activate Account")
        print("\n5. Transaction Menu")
        print("\n6. Search Menu")
        print("\n7. Close Application")
        print('\n\n')
        choice = int(input('Enter Your Choice...:'))
        if choice == 1:
            add_account()
        if choice == 2:
            modify_account()
        if choice == 3:
            close_account()
        if choice == 4:
            activate_account()
        if choice == 5:
            transaction_menu()
        if choice == 6:
            search_menu()
        if choice == 7:
            break
       
if __name__=="__main__":
    main_menu()