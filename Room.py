class Room:
    comfort_factor = {'стандарт': 1, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}
    room_price = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
    food_type = {'без питания': 0, 'завтрак': 280, 'полупансион': 1000}
    all_rooms = []

    def __init__(self, txt_info):
        self.number = txt_info[0]
        self.type = txt_info[1]
        self.capacity = int(txt_info[2])
        self.comfort = txt_info[3]
        self.comfort_coef = Room.comfort_factor[self.comfort]
        self.price = Room.room_price[self.type] * Room.comfort_factor[self.comfort] * self.capacity
        self.discount_price = self.price * 0.7
        self.occupied_dates = []
        Room.all_rooms.append(self)

    @staticmethod
    def best_price(room_price, comfort, food, max_price):
        best_result = room_price
        best_diff = abs(room_price - max_price)
        if max_price >= room_price:
            for coef in comfort:
                for num in list(food.values()):
                    new_result = room_price * coef + num
                    new_diff = abs(new_result - max_price)

                    if new_result <= max_price and new_diff <= best_diff:
                        best_result = new_result
                        best_diff = new_diff
                        comfort_type = coef
            return best_result, comfort_type
        else:
            return None

    '''
    недоделанный метод выбора комнаты под параметры клиента,
    нужно будет разобраться что делать, если количество гостей = 4
    '''

    @classmethod
    def room_selection(cls, guests, rental_days, money):
        suitable_iter_1 = [room for room in Room.all_rooms if room.capacity == guests
                           and not any(dates in rental_days for dates in room.occupied_dates)]
        if suitable_iter_1:
            coefs = []
            for rm in suitable_iter_1:
                coefs.append(rm.comfort_coef)
            coefs = list(set(coefs))
            info_tuple = Room.best_price(suitable_iter_1[0].price, coefs,
                                         Room.food_type, money)
            if info_tuple:
                best_price, comfort_coef = info_tuple[0], info_tuple[1]
                for apart in suitable_iter_1:
                    if apart.comfort_coef == comfort_coef:
                        for day in rental_days:
                            apart.occupied_dates.append(day)
                        return apart, best_price
            else:
                return None
        elif not suitable_iter_1:
            suitable_iter_2 = [room for room in Room.all_rooms if room.capacity == guests + 1
                               and not any(dates in rental_days for dates in room.occupied_dates)]
            if suitable_iter_2:
                coefs = []
                for rm in suitable_iter_2:
                    coefs.append(rm.comfort_coef)
                coefs = list(set(coefs))
                info_tuple = Room.best_price(suitable_iter_2[0].discount_price, coefs,
                                             Room.food_type, money)
                if info_tuple:
                    best_price, comfort_coef = info_tuple[0], info_tuple[1]
                    for apart in suitable_iter_2:
                        if apart.comfort_coef == comfort_coef:
                            apart.occupied_dates.append(rental_days)
                            return apart, best_price
                else:
                    return None
        else:
            return None
