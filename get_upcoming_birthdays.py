from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
        delta_days = (birthday_this_year - today).days
        
        if 0 <= delta_days <= 7:
            birthday_weekday = birthday_this_year.weekday()
            congratulation_date = birthday_this_year
            
            if birthday_weekday == 5:
                congratulation_date += timedelta(days=2)
            elif birthday_weekday == 6:
                congratulation_date += timedelta(days=1)
            
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
                })
        
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.11"},
    {"name": "Jane Smith", "birthday": "1990.03.9"},
    {"name": "Bob Smith", "birthday": '2000.03.20'},
    {"name": "Anna Bie", "birthday": "2006.03.15"},
    {"name": "Mark Zuckerberg", "birthday": "1984.05.14"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)