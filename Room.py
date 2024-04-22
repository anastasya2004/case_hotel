class Room:
    comfort_factor = {'стандарт': 1, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}
    room_price = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
    all_rooms = []

    def __init__(self, txt_info):
        self.number = txt_info[0]
        self.type = txt_info[1]
        self.capacity = int(txt_info[2])
        self.comfort = txt_info[3]
        self.price = Room.room_price[self.type] * Room.comfort_factor[self.comfort] * self.capacity
        self.discount_price = self.price * 0.7
        self.occupied_dates = []
        Room.all_rooms.append(self)

    '''
    недоделанный метод выбора комнаты под параметры клиента
    '''
    @classmethod
    def room_selection(cls, guests, rental_days, price):
        suitable_iter_1 = []
        for room in Room.all_rooms:
            if room.capacity == guests:
                suitable_variants.append(room)

