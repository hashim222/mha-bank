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
    print('Choose one of these from the list: ')
    print('1. View Balance')
    print('2. Deposte Money')
    print('3. Withdraw Money')


get_user_details()
