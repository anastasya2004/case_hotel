# Case- study #7 "Petrol station"
# Developers : Setskov M. (100%)
#              Osokina A. (90%)
# This program simulates the hotel room occupancy management process.

from Room import Room
from Client import Client


with open('fund.txt', 'r', encoding='utf-8') as info:
    for line in info:
        room = Room(line.split())

with open('booking.txt', 'r', encoding='utf-8') as info:
    for line in info:
        client_id = Client(line.split())

# Retrieve unique booking dates from all clients for analysis
analyzed_dates = Client.dates_to_modeling()

# Analyzing each booking day
for day in analyzed_dates:
    income = 0
    lost_income = 0
    day_clients = [client for client in Client.all_clients if client.booking_date == day]
    print('~' * 100)

    # Processing each client's booking for the day
    for certain_client in day_clients:
        chosen_room_tuple = Room.room_selection(certain_client.guests, certain_client.rental_days(),
                                                certain_client.money_to_spend)

        # If a suitable room is found for the client
        # Printing booking details
        if chosen_room_tuple:
            probability = chosen_room_tuple[2]
            income += chosen_room_tuple[1]
            print('Поступила заявка на бронирование:')
            print(certain_client)
            print('Найден:')
            print(f'Номер {chosen_room_tuple[0].number} {chosen_room_tuple[0].type} {chosen_room_tuple[0].comfort} '
                  f'рассчитан на {chosen_room_tuple[0].capacity} человек стоимость {chosen_room_tuple[0].price}')
            if probability == 2:
                print('Клиент отказался от бронирования')
            print('~' * 100)
        else:
            print('Поступила заявка на бронирование:')
            print(certain_client)
            print('Свободных номеров нет. В бронировании отказано.')
            lost_income += certain_client.money_to_spend
            print('~' * 100)

    # Printing the daily report
    print('/' * 100)
    print(f'Отчет за {day}')
    print(f'Количество занятых номеров {Room.busy_rooms(day)}')
    print(f'Количество свободных номеров {len(Room.all_rooms) - Room.busy_rooms(day)}')
    print(f'Процент загруженности одноместных номеров: {Room.busy_certain_type('одноместный', day)}%')
    print(f'Процент загруженности двухместный номеров: {Room.busy_certain_type('двухместный', day)}%')
    print(f'Процент загруженности полулюкс номеров: {Room.busy_certain_type('полулюкс', day)}%')
    print(f'Процент загруженности люкс номеров: {Room.busy_certain_type('люкс', day)}%')
    print(f'Процент загруженности гостиницы {round(Room.busy_rooms(day) / len(Room.all_rooms) * 100, 2)}%')
    print(f'Полученный доход за день: {income}')
    print(f'Упущенный доход за день: {lost_income}')
    print('/' * 100)

    # Updating occupied dates for each room
    for apart in Room.all_rooms:
        if day in apart.occupied_dates:
            apart.occupied_dates.remove(day)
