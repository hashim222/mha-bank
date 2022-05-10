from time import sleep
import gspread
from google.oauth2.service_account import Credentials
import pyfiglet



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('MHA_bank')


def get_user_details():
    '''
    Takes all the user info.
    Inside the function runs multiple functions inside
    '''
    BANK_LOGO = pyfiglet.figlet_format('MHA  BANK')
    print(BANK_LOGO)
    print('Hello and welcome to MHA Bank🏦.\n')

    input('Press any BUTTON to start...')
    print('=========================================================================================')
    sleep(0.5)
    enter_username()
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


def enter_username():
    '''
    Stores username
    '''
    while True:
        print('Please keep the letter below 10 and above 5')
        username = input('Create your username please: ')
        SHEET.worksheet('user_info').update('A4', username)
        if len(username) > 10:
            print('The number of letters should not exceed 10. Please try again')
            continue
        elif len(username) < 5:
            print('A minimum of five letters is required. Please try again')
            continue
        return username


def deposit_money():
    '''
    Users inputs for deposit amount
    '''
    user_deposit_money = float(
        input('how much would you like to deposit money? £'))
    SHEET.worksheet('user_info').update_acell('B4', user_deposit_money)
    print(f'You deposit £{user_deposit_money} in your bank acc')
    return user_deposit_money


def withdraw_money(amount):
    '''
    Users inputs for withdrawl amount.
    '''
    user_withdraw_money = float(
        input('how much would you like to withdraw? £'))
    SHEET.worksheet('user_info').update_acell('C4', user_withdraw_money)
    updated_bal = amount - user_withdraw_money
    print(f'you have taken £{user_withdraw_money} from your bank acc')
    return updated_bal


def view_balance(amount):
    '''
    Shows users to their total balance
    '''
    print(f'your updated balance is £{amount}')
    SHEET.worksheet('user_info').update_acell('D4', amount)
    return amount


def main():
    '''
    User multiple choices inside.
    Runs multiple function.
    '''
    added_amount = deposit_money()
    removed_amount = withdraw_money(added_amount)
    view_balance(removed_amount)
    # total_balance =
    # while True:
    #     sleep(1.5)
    #     print('Please choose one of the following options: ')
    #     print('\n1. Deposit Money\n2. Withdraw Money\n3. View Balance\n')
    #     choose = input('Type here: ')
    #     if choose == '1':
    #         added_amount = deposit_money()
    #         total_balance = total_balance + added_amount
    #         print(f'your updated balance is £{total_balance}')
    #     elif choose == '2':
    #         removed_amount = withdraw_money(added_amount)
    #         total_balance = total_balance - removed_amount
    #         print(total_balance)
    #     elif choose == '3':
    #         view_balance(removed_amount)
    #     elif choose == '':
    #         print('please type a number')
    #     else:
    #         validate_data(choose)


get_user_details()
