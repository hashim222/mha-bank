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
    Stores username information
    '''

    while True:
        username = input(
            "Create your username here, or enter your existing username if you are already a member.\nYour character should be between 5 and 10. \n").lower()

        if len(username) > 10:
            print('\nThe number of character should not exceed 10. Please try again.')
            continue
        elif len(username) < 5:
            print('\nA minimum of five character is required. Please try again.')
            continue
        return username


def check_user_existence(username):
    '''
    Checks if user exists in the spreadsheet
    '''

    user_info_ws = SHEET.worksheet("user_info")

    existing_user = user_info_ws.find(username, in_column=1)
    if existing_user:
        last_cell = user_info_ws.findall(username, in_column=1)[-1]
        balance = user_info_ws.row_values(last_cell.row)[-1]

        print(
            f"\nWelcome {username}.. Your current account balance is: {balance}")

    else:
        print(f"\nUsername not found\nCreating new user...")
        sleep(1.2)
        print(f'\nHello {username}, Thanx for joining MHA Bank')


def deposit_money():
    '''
    Users inputs for deposit amount
    '''

    while True:
        deposit_amount = input('How much would you like to deposit?\n£')
        if deposit_amount.isdigit():
            deposit_amount = float(deposit_amount)
            print('\nProcessing deposit....')
            sleep(1.5)
            print('Approved✅\n')
            sleep(1.2)
            print(
                f'Your bank account has been credited with £{deposit_amount}\n')
        else:
            print('\nPlease enter a number')
            continue
        return deposit_amount


def withdraw_money(amount):
    '''
    Users inputs for withdrawl amount.
    '''

    while True:
        user_choice_of_withdraw = input(
            'Do you wish to withdraw money? y/n\n').lower()
        if user_choice_of_withdraw == 'y' or user_choice_of_withdraw == 'yes':
            withdrawal_amount = input(
                '\nHow much would you like to withdraw?\n£')
            if withdrawal_amount.isdigit():
                withdrawal_amount = float(withdrawal_amount)
            else:
                print('\nPlease enter a number\n')
                continue

            if withdrawal_amount > amount:
                sleep(1.2)
                print('\nPayment Declined❌')
                sleep(1.2)
                print(
                    f'you have insufficient balance of £{amount} please withdraw £{amount} or less please\n')
                continue

            print('\nWithdrawal request processing...')
            sleep(1.5)
            print('Approved✅\n')
            sleep(1.2)
            print(
                f'You have taken £{withdrawal_amount} from your bank account\n')
        elif user_choice_of_withdraw == 'n' or user_choice_of_withdraw == 'no':
            withdrawal_amount = float(0)
            print('\nprocessing...')
            sleep(1.2)
            print('No money was withdrawn from your account\n')
        else:
            print('\nYou can proceed to the next step by typing yes or no')
            continue
        return withdrawal_amount


def view_balance(depo_amount, withd_amount):
    '''
    Shows users to their total balance
    '''

    get_total_amount = depo_amount - withd_amount
    print(f'You have an updated balance of £{get_total_amount}\n')
    return get_total_amount


def main():
    '''
    User multiple choices inside.
    Runs multiple function.
    '''

    user = enter_username()
    check_user_existence(user)
    added_amount = deposit_money()
    removed_amount = withdraw_money(added_amount)
    total_balance = view_balance(added_amount, removed_amount)

    # users = SHEET.worksheet("user_info").col_values(1)
    # for username in users:
    #     # index = 1
    #     if  username == user:
    #         SHEET.worksheet('user_info').row_values(user)
    #         print('user found', user)
    #         # user_row = index
    #         break
    #     else:
    #         append_row_in_spreadsheet = [user, added_amount, removed_amount, total_balance]
    #         SHEET.worksheet('user_info').append_row(append_row_in_spreadsheet)
    #         # index =+ 1

    # deposits = SHEET.worksheet("user_info").col_values(4)
    # user_deposit = deposits[1]
    # print(user_deposit)

    # sleep(1.2)
    # print(
    #     f'User Information:\nUsername - {user}\nBalance - £{total_balance}')

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
