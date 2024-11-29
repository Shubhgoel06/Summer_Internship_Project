from datetime import datetime

def format_datetime(dt_str):
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y %H:%M")

def validate_passport(passport_number):
    return len(passport_number) == 9 and passport_number.isdigit()
