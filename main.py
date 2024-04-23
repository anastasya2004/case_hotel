import random
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
        factor = random.randint(1, 4)
        if factor == 2:
            chosen_room_tuple = None
        print(chosen_room_tuple)
    for apart in Room.all_rooms:
        if day in apart.occupied_dates:
            apart.occupied_dates.remove(day)


