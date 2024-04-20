from Room import Room
from Client import Client

with open('fund.txt', 'r', encoding='utf-8') as info:
    for line in info:
        room = Room(line.split())


with open('booking.txt', 'r', encoding='utf-8') as info:
    for line in info:
        client = Client(line.split())

for client in Client.all_clients:
