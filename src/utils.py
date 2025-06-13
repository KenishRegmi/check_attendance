from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")

def time_diff_minutes(d1, d2):
    return (d2 - d1).total_seconds() / 60
