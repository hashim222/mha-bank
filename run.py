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
    user_options()


def user_options():
    '''
    Gives users multiple options to choose from.
    '''
    while True:
        print('Please choose one of the following options: ')
        print('\n1. View Balance\n2. Deposit Money\n3. Withdraw Money')
        choose = input('Type here: ')

        if choose == '1':
            print('User wants to see their balance')
        elif choose == '2':
            print('User wants to deposit their money in ')
        elif choose == '3':
            print('User wants to withdraw thier money')
        elif choose == '':
            print('please type a number')
        else:
            validate_data(choose)


def validate_data(user_typed):
    '''
    Instead of breaking a program, this raises an error if the user doesn't follow along.
    '''
    try:
        if int(user_typed):
            raise ValueError(
                f'The typed value does not match with the given values. ')
    except ValueError as err:
        print(f"Invalid data: {err} please try again. \n")


get_user_details()
