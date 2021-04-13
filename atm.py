print("  welcome! please insert your card")
print("hi,please do not remove your chip card until the entire transaction")
language =input("please select your language:")
print(''' n 
        1 == english
        2 == hindi
        3 == telugu
        ''')
if language==1:
    print("english")
elif language==2:
    print("hindi")
else:
    print("telugu")
password = 5678
pin = int(input("please enter your pin"))
withdrawal_amount = 2000
deposit_amount = 5000
new_password = 7654
if pin==password:
    print('''
            1 == banking
            2 == balance enquiry
            3 == transfer
            ''')
    try:
        option = int(input("please enter your choice"))
    except:
        print("please choose a valid option")
    if option==1: 
        print(''' please  select transaction
                1 == withdrawal_amount
                2 == mini statement
                3 == pin change
                4 == deposite_amount
                ''')
        try:
            opt=int(input("please enter your choice")
        if opt==1:
            print(f"{withdrawal_amount} is debited in your account")
            current_balance = balance-withdrawal_amount
            print(f"the current balance is{current_balance}")
        elif opt==2:
            print("the mini statement is given below:")
            print("the recents transactions are:")
            print("=================================")
        elif opt==4:
            print(f"{deposit_amount} is credited into your account")
            current_balance = balance+deposit_amount
            print(f" the current balance is:{current_balance}")
        else:
            print(f"enter old password:{password}")
            print(f"enter new password:{new_password}")
            print(f"confirm new password:{new_password}")
    elif option==2:
        print("the balance is{balance}")
    else:
        print("the money transfer to account")
        print("===============================")
        print(''' if you want to receipt:
                yes == 1
                no == 0
                ''')
        receipt = int(input())
        if receipt == 1:
            print("the available balance is:{balance})
        else:
            print("thank you for visiting")
            
else:
    print("you entered wrong pin ,try again")


        
