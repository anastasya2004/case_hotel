from Room import Room
from Client import Client


with open('fund.txt', 'r', encoding='utf-8') as info:
    for line in info:
        room = Room(line.split())

with open('booking.txt', 'r', encoding='utf-8') as info:
    for line in info:
        client_id = Client(line.split())

analyzed_dates = Client.dates_to_modeling()

for day in analyzed_dates:
    day_clients = [client for client in Client.all_clients if client.booking_date == day]
    for certain_client in day_clients:
        chosen_room_tuple = Room.room_selection(certain_client.guests, certain_client.rental_days(),
                                                certain_client.money_to_spend)
        if chosen_room_tuple:
            probability = chosen_room_tuple[2]
            print('Поступила заявка на бронирование:')
            print(certain_client)
            print('Найден:')
            print(f'Номер {chosen_room_tuple[0].number} {chosen_room_tuple[0].type} {chosen_room_tuple[0].comfort} '
                  f'рассчитан на {chosen_room_tuple[0].capacity} человека стоимость {chosen_room_tuple[0].price}')
            if probability == 2:
                print('Клиент отказался от бронирования')
            print()
        else:
            print('Поступила заявка на бронирование:')
            print(certain_client)
            print('Свободных номеров нет. В бронировании отказано.')
            print()

    for apart in Room.all_rooms:
        if day in apart.occupied_dates:
            apart.occupied_dates.remove(day)
