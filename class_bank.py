class bank_account:
    def __init__(self, user_name,pass_word,balance):
        self.name=user_name
        self.password=pass_word
        self.balance=balance
    def withdraw(self,amount):
        self.balance-=amount
    def deposit(self,amount):
        self.balance+=amount
#loop over n times create n object in a list
import getpass
total_account=[]
def create_account():
    number=int(input('How many accounts do you want to create now? '))
    for i in range(number):
        user_name=input('Enter username: ')
        password=getpass.getpass('Enter password: ')
        balance=float(input('Enter bank balance: '))
        total_account.append(bank_account(user_name,password,balance))
#display information
def display_account():
    for account in total_account:
        print(f'Username:{account.name}\nPassword:{account.password}\nBalance:{account.balance}\n')
#take username and password from user and then check with the object it belongs to
def find_account():
    username_input=input('enter your username: ')
    password_input=input('enter your password: ')
    for account in total_account:
        if account.name==username_input and account.password==password_input:
            print('The account is found.')
            print(f'Username: {account.name}\nPassword:{account.password}\nBalance:{account.balance}\n')
        else:
            print('Sorry, the account is not found.Check the details and try again:)')
#take username of a person who you want to send money
#Find the object with that username and withdraw amount from your account and deposit the required amount in receiver account 
def send_money():
    sender_username = input('Enter your username: ')
    sender_password = input('Enter your password: ')
    
    for account1 in total_account:
        if account1.name == sender_username and account1.password == sender_password:
            receiver_username = input('Enter the username of the account you want to send money to: ')
            for account2 in total_account:
                if account2.name == receiver_username:
                    amount = float(input('Enter the amount you want to send: '))
                    if account1.balance >= amount:
                        account1.withdraw(amount)
                        account2.deposit(amount)
                        print(f"Amount {amount} sent to {account2.name}'s account.")
                    else:
                        print("Insufficient balance.")
                else:
                    print("Receiver account not found.")
        else:
            print("Sender account not found.")

print('Welcome to our Bank!! How can I help you?')

while True:
    print('1. Create new account')
    print('2. Send money')
    print('3. Check account')
    print('4. Display all accounts')
    print('5. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        create_account()
    elif choice == '2':
        send_money()
    elif choice == '3':
        find_account()
    elif choice == '4':
        display_account()
    elif choice == '5':
        print('Exiting program. Have a good day! See you again:)')
        break
    else:
        print('Invalid choice. Please try again.')
