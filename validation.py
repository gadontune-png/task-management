from datetime import datetime

def validate_task_title(title):
    if len(title) < 1:
        return False
    return True


def validate_task_description(description):
    if len(description) < 1:
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False