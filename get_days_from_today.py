from datetime import datetime


def get_days_from_today(date):
    input_date = datetime.strptime(date, '%Y-%m-%d').date()
    now = datetime.today().date()
    difference_date = now - input_date
    return difference_date.days
    
while True:
    date = input("Ведіть дату у форматі РРРР-ММ-ДД: ")
    try:
        days = get_days_from_today(date)
        break
    except ValueError:
        print('Невірний формат дати. Спробуйте ще раз у форматі РРРР-ММ-ДД.')


print(f"Кількість днів між заданою датою і поточною датою: {days} днів")

