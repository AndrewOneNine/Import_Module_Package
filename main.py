import emoji
from datetime import datetime
from application.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    print(emoji.emojize('Сегодняшняя дата 📅: '), datetime.now().date())
    print(get_employees('Михаил', 'Потапыч'))
    print(emoji.emojize('Его заработная плата 💸: '), calculate_salary(1000, 4000))
