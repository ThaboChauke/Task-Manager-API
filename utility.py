from datetime import datetime
import re

from sqlalchemy import false


def convert_date(date):
    return datetime.strptime(date, "%Y-%m-%d %H:%M")

def find_re(text):
    list_of_re = re.findall(r'[^1a-zA-Z ]', text)

    if len(list_of_re) == 0:
        return True
    else:
        return False
