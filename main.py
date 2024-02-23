
from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):

    birthdays_per_week = defaultdict(list)
    
    today = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days == 0 and today.strftime('%A') == 'Saturday':
            birthday_weekday = 'Monday'
        else:
            birthday_weekday = (today + timedelta(days=delta_days)).strftime('%A')
        
        if 0 <= delta_days < 7 or (delta_days >= 7 and delta_days < 14):
            birthdays_per_week[birthday_weekday].append(name)
    
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

users = [
    {"name": "Bill", "birthday": datetime(1955, 3, 1)},
    {"name": "Jan", "birthday": datetime(1976, 2, 24)},
    {"name": "Jill", "birthday": datetime(1974, 7, 1)},
    {"name": "Kim", "birthday": datetime(1980, 10, 21)},
    {"name": "Alice", "birthday": datetime(1990, 5, 15)},
    {"name": "Bob", "birthday": datetime(1985, 2, 27)},
    {"name": "Charlie", "birthday": datetime(1978, 3, 10)},
    {"name": "David", "birthday": datetime(2002, 2, 28)},
    {"name": "Eve", "birthday": datetime(1982, 7, 18)},
]

get_birthdays_per_week(users)