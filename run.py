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
        username = input("Create your username here, or type in your username if you're already a member: \n")
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
    deposit_amount = float(
        input('What amount would you like to deposit?\n£'))
    print(f'Your bank account has been credited with £{deposit_amount}')
    return deposit_amount


def withdraw_money():
    '''
    Users inputs for withdrawl amount.
    '''
    user_choice_of_withdraw = input(
        'Do you wish to withdraw money? y/n\n').lower()
    if user_choice_of_withdraw == 'y' or user_choice_of_withdraw == 'yes':
        withdrawal_amount = float(
            input('What amount would you like to withdraw?\n£'))
        print(f'You have taken £{withdrawal_amount} from your bank account')
    elif user_choice_of_withdraw == 'n' or user_choice_of_withdraw == 'no':
        withdrawal_amount = float(0)
        print('No money was withdrawn from your account')
    return withdrawal_amount

def view_balance(depo_amount, amount):
    '''
    Shows users to their total balance
    '''
    get_total = depo_amount - amount
    print(f'You have an updated balance of £{get_total}')
    return get_total


def main():
    '''
    User multiple choices inside.
    Runs multiple function.
    '''
    usr_name = enter_username()
    added_amount = deposit_money()
    removed_amount = withdraw_money()
    total_balance = view_balance(added_amount, removed_amount)

    add_total = [usr_name, added_amount, removed_amount, total_balance]

    SHEET.worksheet('user_info').append_row(add_total)

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
