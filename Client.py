class Client:
    all_clients = []

    def __init__(self, txt_info):
        self.booking_date = txt_info[0]
        self.name = ' '.join(txt_info[1:4])
        self.guests = int(txt_info[4])
        self.arriving = txt_info[5]
        self.days = int(txt_info[6])
        self.money_to_spend = int(txt_info[7]) * self.guests
        self.dates_to_rent = self.rental_days()
        Client.all_clients.append(self)

    def rental_days(self):
        dates = []
        arrival_day = list(map(int, self.arriving.split('.')))
        for i in range(self.days):
            dates.append([arrival_day[0] + i, arrival_day[1], arrival_day[2]])
        dates = [f'{day:02d}.{month:02d}.{year}' for day, month, year in dates]
        return dates

    @classmethod
    def dates_to_modeling(cls):
        dates_to_modeling = []
        for order in Client.all_clients:
            dates_to_modeling.append(order.booking_date)
        dates_to_modeling = set(dates_to_modeling)
        return sorted(dates_to_modeling)
