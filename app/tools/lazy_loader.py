from datetime import datetime, timedelta

def build_date_range(center_date: datetime, days: int, direction: str):
    if direction == "up":
        start_date = center_date - timedelta(days=days)
        end_date = center_date
    elif direction == "down":
        start_date = center_date
        end_date = center_date + timedelta(days=days)
    else:  # center
        start_date = center_date - timedelta(days=days)
        end_date = center_date + timedelta(days=days)
    return start_date, end_date
