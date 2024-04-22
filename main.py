from Room import Room
from Client import Client

with open('fund.txt', 'r', encoding='utf-8') as info:
    for line in info:
        room = Room(line.split())

with open('booking.txt', 'r', encoding='utf-8') as info:
    for line in info:
        client = Client(line.split())
'''
Получаем информацию о уникальных датах, в которых было совершено бронирование,
то есть даты 01.03.2020 - 10.03.2020, чтобы бежать по ним общим циклом,
составлять ежедневные отчеты
'''
analyzed_dates = Client.dates_to_modeling()

'''
Начало большого цикла, в котором проиходит самомоделирование
идем циклом по каждому уникальному дню из файла booking.txt
в конце каждой итерации будет формироваться дневной отчет.
Идея такая, что при рассмотрении каждого клиента с помощью метода rental_days
будут выводиться даты, на которые клиент хочет заселиться
Для каждой комнаты в атрибуте occupied_dates будет храниться занятость комнаты
Даты желаемые клиентом будут сопоставляться с датами для каждой комнаты.
Таким образом будет реализована проверка на доступность комнаты.
Следующим шагом нужно реализовать подбор комнаты в отдельном методе класса Room or Client
со всеми 
'''
for day in analyzed_dates:
    day_clients = [client for client in Client.all_clients if client.booking_date == day]

