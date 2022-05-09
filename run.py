import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
from time import sleep


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('mha_bank')

# sales = SHEET.worksheet('user_info')
# data = sales.get_all_values()


def get_user_details():
    '''
    Takes all the user info.
    Inside the function runs multiple functions inside
    '''
    BANK_LOGO = pyfiglet.figlet_format('MHA  BANK')
    print(BANK_LOGO)
    print('Hello and welcome to mha bank.\n')

    input('Press any BUTTON to start...')
    print('=========================================================================================')
    sleep(0.5)
    main()



def validate_data(user_typed):
    '''
    Instead of breaking a program, this raises an error if the user doesn't follow along.
    '''
    try:
        if int(user_typed):
            raise ValueError(
                'The typed value does not match with the given values.')
    except ValueError as err:
        print(f"Invalid data: {err} please try again. \n")

def deposit_money():
    '''
    Users inputs for deposit amount
    '''
    user_deposit_money = float(input('how much would you like to deposit money? £'))
    print(f'You deposit £{user_deposit_money} in your bank acc')
    return user_deposit_money

def withdraw_money(amount):
    '''
    Users inputs for withdrawl amount.
    '''
    user_withdraw_money = float(input('how much would you like to withdraw? £'))
    updated_bal = amount - user_withdraw_money
    print(f'you have taken £{user_withdraw_money} from your bank acc')
    return updated_bal
def view_balance(amount):
    '''
    Shows users to their total balance
    '''
    print(f'your updated balance is £{amount}')
    return amount

def main():
    '''
    User multiple choices inside.
    Runs multiple function.
    '''
    added_amount = deposit_money()
    removed_amount = withdraw_money(added_amount)
    total_balance = view_balance(removed_amount)

    while True:
        sleep(1.5)
        print('Please choose one of the following options: ')
        print('\n1. Deposit Money\n2. Withdraw Money\n3. View Balance\n')
        choose = input('Type here: ')
        if choose == '1':
            added_amount = deposit_money()
            added_amount = added_amount + total_balance
            print(f'your updated balance is £{added_amount}')
        elif choose == '2':
            removed_amount = withdraw_money(added_amount)
            removed_amount = removed_amount - total_balance
            print(removed_amount)
        elif choose == '3':
            view_balance(removed_amount)
        elif choose == '':
            print('please type a number')
        else:
            validate_data(choose)      


get_user_details()

