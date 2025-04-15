from datetime import datetime
from application_agent import run_with_agent
import dateparser


def welcome_banner():
    banner = r"""
 __        __   _                            _          _   _          
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___ 
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|

                  👋 Welcome to Leave Application GPT! 📝
                     Type 'exit' anytime to quit.                   
    """
    print(banner)


def check_for_exit(input: str) -> bool:
    if input.lower() == "exit":
        print("Goodbye Learner! 🪂")
        return True
    return False


def language_validator(input: str) -> bool:
    if input.lower() == "en" or input.lower() == "bn":
        return True
    return False


def get_language_str(lang: str) -> str:
    if lang.lower() == "en":
        return "English"
    elif lang.lower() == "bn":
        return "Bangla"
    else:
        return "English"


def date_validator(date: str) -> bool:
    val = dateparser.parse(date, settings={"DATE_ORDER": "DMY"})
    if val:
        return True
    return False


def mix_date(fromdate: str, todate: str) -> str:
    return f"({fromdate} to {todate})"


def run_user_prompt():
    user_name_input = input(">>Name:: ")

    if check_for_exit(user_name_input):
        return

    user_date = input(">>Date: Example: (dd.mm.yyyy 01.01.2025):: ")

    if check_for_exit(user_date):
        return

    if not date_validator(user_date):
        print("Invalid Date Format!. ‼️")
        return

    user_language = input(">>(en/bn):: ")

    if check_for_exit(user_language):
        return

    if not language_validator(user_language):
        print("Invalid Language Selection!")
        return

    date_obj = datetime.strptime(user_date, "%d.%m.%Y")
    formatted_date = date_obj.strftime("%B %d, %Y")
    try:
        run_with_agent(
            f"write me a leave application in {get_language_str(user_language)} language",
            user_name_input,
            formatted_date,
        )
    except Exception as e:
        print(e)


welcome_banner()
run_user_prompt()
