from datetime import datetime

def convert_date(date):
    return datetime.strptime(date, "%Y-%m-%d %H:%M")