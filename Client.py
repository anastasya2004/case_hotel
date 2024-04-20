class Client:
    all_clients = []

    def __init__(self, txt_info):
        self.booking_gate = txt_info[0]
        self.name = ' '.join(txt_info[1:4])
        self.guests = int(txt_info[4])
        self.arriving = txt_info[5]
        self.days = int(txt_info[6])
        self.money_to_spend = int(txt_info[7]) * self.guests
        Client.all_clients.append(self)