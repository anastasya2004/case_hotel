import random
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

    @classmethod
    def room_selection(cls, guests, rental_days, money):
        factor = random.randint(1, 4)
        suitable_iter_1 = [room for room in Room.all_rooms if room.capacity == guests
                           and not any(dates in rental_days for dates in room.occupied_dates)]
        suitable_iter_1 = sorted(suitable_iter_1, key=lambda room: room.price, reverse=True)
        if suitable_iter_1:
            all_prices = []
            best_price = None
            for i in suitable_iter_1:
                all_prices.append(i.price)
            for i in suitable_iter_1:
                all_prices.append(i.price + Room.food_type['завтрак'])
            for i in suitable_iter_1:
                all_prices.append(i.price + Room.food_type['полупансион'])
            all_prices.sort(reverse=True)
            for i in all_prices:
                if i < money:
                    best_price = i
                    break
            if best_price:
                for i in suitable_iter_1:
                    if i.price <= best_price:
                        for j in rental_days:
                            i.occupied_dates.append(j)
                        return i, best_price, factor
            else:
                return None
        elif not suitable_iter_1:
            suitable_iter_2 = [room for room in Room.all_rooms if room.capacity == guests + 1
                               and not any(dates in rental_days for dates in room.occupied_dates)]
            suitable_iter_2 = sorted(suitable_iter_2, key=lambda room: room.discount_price, reverse=True)
            if suitable_iter_2:
                all_prices = []
                best_price = None
                for i in suitable_iter_2:
                    all_prices.append(i.discount_price)
                for i in suitable_iter_2:
                    all_prices.append(i.discount_price + Room.food_type['завтрак'])
                for i in suitable_iter_2:
                    all_prices.append(i.discount_price + Room.food_type['полупансион'])
                all_prices.sort(reverse=True)
                for i in all_prices:
                    if i < money:
                        best_price = i
                        break
                if best_price:
                    for i in suitable_iter_2:
                        if i.discount_price <= best_price:
                            for j in rental_days:
                                i.occupied_dates.append(j)
                            return i, best_price, factor
                else:
                    return None
        else:
            return None
