# Python API for Google spreadsheets.
import gspread
from google.oauth2.service_account import Credentials
# Created a logo for app using pyfiglet.
import pyfiglet
# I've added sleep to delay my functions.
from time import sleep


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("MHA_bank")


def delay_print_message(message):
    '''
    End minutes were created before submitting.
    To delay functions, I had to repeat the sleep function
    multiple times, so I created this to reduce the code
    so that I don't have to repeat it multiple times.
    '''
    print(message)
    sleep(1.4)


def user_welcome_text():
    """
    Users first see message
    """
    BANK_LOGO = pyfiglet.figlet_format("MHA  BANK")
    print(BANK_LOGO)
    print("Hello and welcome to MHA Bank🏦.\n")
    delay_print_message("Press ENTER to start...")
    input("")
    delay_print_message(
        "==================================================================="
        "=======\n"
    )


def validate_data(user_typed):
    """
    Instead of breaking a program, this raises an error if the user doesn't
    follow along.
    """

    try:
        if int(user_typed) == 0 or int(user_typed) > 4:
            print(
                "Invalid Number: The typed value does not match with the "
                "given values. please try again."
            )
    except ValueError:
        print("Invalid data: Only intgers are allowed. please try again. \n")


def enter_username():
    """
    Here is where users enter their username.
    Checks the characters entered by the user don't exceed or fall below.
    """

    while True:
        username = input(
            "Create your username here, or enter your existing "
            "username if you are already a member."
            "\nYour character should be between 5 and 10. \n"
        ).lower()

        if len(username) > 10:
            print(
                "\nThe number of character should not exceed 10. "
                "Please try again."
            )
            continue
        elif len(username) < 5:
            print("\nA minimum of five character is required. "
                  "Please try again.")
            continue
        return username


def check_user_existence(username):
    """
    This function checks whether a user exists in the spreadsheet.
    If the user already exists it will restore their previous balance,
    if not, it will create a user name for them.
    """

    # Google Spreadsheet
    user_info_ws = SHEET.worksheet("user_info")

    existing_user = user_info_ws.find(username, in_column=1)
    if existing_user:

        # Gets username from the spreadsheet
        last_cell = user_info_ws.findall(username, in_column=1)[-1]

        # Gets user previus balance from the spreadsheet
        balance = user_info_ws.row_values(last_cell.row)[-1]
        delay_print_message("User checking....\n")
        delay_print_message("User found")
        delay_print_message(
            f"\nWelcome back {username}.. "
            f"Your current account balance is: £{float(balance):.2f}\n"
        )

        return username, float(balance)
    else:
        delay_print_message("User checking....")
        print("\nUsername not found\n" "Creating new user...")
        sleep(1.4)
        print(f"\nHello {username}, Thanx for joining MHA Bank")
        return username, 0


def deposit(user, balance):
    """
    Adds the user's amount to the bank.
    A user deposit is saved in the spreadsheet and if their balance is
    found in the spreadsheet previously their balance gets updated
    """

    while True:

        deposit_amount = input("How much would you like to deposit?\n£")
        if deposit_amount.replace(".", "", 1).isdigit():
            deposit_amount = float(deposit_amount)

            # Adds user deposits amount inside the spreadsheet
            append_rows_in_the_spreadsheet = [
                user,
                deposit_amount,
                "",
                balance + deposit_amount,
            ]
            SHEET.worksheet("user_info").append_row(
                append_rows_in_the_spreadsheet)

            delay_print_message("\nProcessing deposit....")
            delay_print_message("Approved✅\n")
            delay_print_message(
                f"Your bank account has been "
                f"credited with £{deposit_amount:.2f}\n"
            )
        else:
            print("\nPlease enter a number")
            continue
        return deposit_amount


def withdraw(user, amount):
    """
    Withdrawal input for the user.
    If there is enough money to withdraw, it will withdraw it for the user and
    store it in the spreadsheet.
    """

    while True:
        user_choice_of_withdraw = input(
            "Do you wish to withdraw money? y/n\n").lower()
        if user_choice_of_withdraw == "y" or user_choice_of_withdraw == "yes":
            withdrawal_amount = input(
                "\nHow much would you like to withdraw?\n£")
            if withdrawal_amount.replace(".", "", 1).isdigit():
                withdrawal_amount = float(withdrawal_amount)
            else:
                print("\nPlease enter a number\n")
                continue
            if withdrawal_amount > amount:

                sleep(1.4)
                delay_print_message("\nPayment Declined❌")
                delay_print_message(
                    f"You have insufficient balance of £{amount:.2f} "
                    f"please withdraw £{amount:.2f} or less\n"
                )
                continue
            # Adds user Withdrawal amount inside the spreadsheet
            append_rows_in_the_spreadsheet = [
                user,
                "",
                withdrawal_amount,
                amount - withdrawal_amount,
            ]
            SHEET.worksheet("user_info").append_row(
                append_rows_in_the_spreadsheet)

            delay_print_message("\nWithdrawal request processing...")
            delay_print_message("Approved✅\n")
            delay_print_message(
                f"You have taken £{withdrawal_amount} from your bank account")
        elif user_choice_of_withdraw == "n" or user_choice_of_withdraw == "no":
            withdrawal_amount = float(0)
            print("\nProcessing...")
            delay_print_message("No money was withdrawn from your account\n")
        else:
            print("\nYou can proceed to the next step by typing yes or no.")
            continue
        return withdrawal_amount


def view_balance(balance):
    """
    Display the total balance of users
    """

    get_total_amount = balance
    sleep(1.2)
    print(f"\nYou have an updated balance of £{get_total_amount:.2f}")
    return get_total_amount


def main():
    """
    Provides users with multiple options to choose from.
    Performs multiple functions inside.
    """
    user_welcome_text()
    user = enter_username()
    check_user, balance = check_user_existence(user)

    while True:
        delay_print_message("\nPlease choose one of the following options: ")

        print(
            "\n1. Deposit⬆️\n"
            "2. Withdraw🔻\n"
            "3. View Balance🪟\n"
            "4. Exit App👋\n")

        choose = input("Type here: ")
        if choose == "1":
            added_amount = deposit(check_user, balance)
            balance = balance + added_amount
        elif choose == "2":
            removed_amount = withdraw(check_user, balance)
            balance = balance - removed_amount
        elif choose == "3":
            balance = view_balance(balance)
        elif choose == "":
            print("Please type a number")
        elif choose == "4":
            print(f"\nSee you soon, {user}👋\n")
            quit()
        else:
            validate_data(choose)


if __name__ == "__main__":
    main()
