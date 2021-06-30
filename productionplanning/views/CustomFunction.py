from datetime import *


def get_db_for_date(db_name):
    start_date = date(2017, 1, 1)
    now = datetime.now()
    now_date = date(now.year, now.month, now.day)
    year = now.year - start_date.year
    if start_date < now_date and year > 0:
        data = {}
        for x in range(1, year+1):
            date_increment = date(start_date.year + 1, start_date.month, start_date.day)
            db_count = db_name.objects.filter(date__range=(start_date, date_increment)).count()
            data[str(start_date)] = db_count
            start_date = date_increment
        return data
    else:
        return None
