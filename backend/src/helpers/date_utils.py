from datetime import datetime
import pytz

# Transform UTC to Toronto timezone
# Note: Need to think of data type for utc_date
def get_toronto_date(utc_date: str):
    toronto = pytz.timezone('America/Toronto')

    # Convert UTC date to Toronto date
    toronto_date = datetime.strptime(utc_date, "%Y-%m-%d %H:%M:%S").astimezone(toronto)

    return toronto_date

# [Usage]
# from src.helpers.date_utils import get_toronto_date
# # Call get_toronto_date() from date_utils.py
# print("Toronto Current Date/Time:", get_toronto_date())

