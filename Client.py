class Client:
    """
    Represents a hotel client with various booking details and functionalities.

    Attributes:
        all_clients (list): A list to store all created Client objects.

    Methods:
        __init__(txt_info): Initializes a Client object with given text information.
        rental_days(): Calculates rental days based on arrival date and duration of stay.
        dates_to_modeling(): Retrieves unique booking dates from all clients for modeling.
        __str__(): Returns a formatted string representation of the Client object.
    """

    all_clients = []

    def __init__(self, txt_info):
        """
        Initializes a Client object with given text information.

        Args:
            txt_info (list): A list containing booking date, name, number of guests,
                             arrival date, duration of stay, and budget per guest.
        """
        self.booking_date = txt_info[0]
        self.name = ' '.join(txt_info[1:4])
        self.guests = int(txt_info[4])
        self.arriving = txt_info[5]
        self.days = int(txt_info[6])
        self.money_to_spend = int(txt_info[7]) * self.guests
        self.dates_to_rent = self.rental_days()
        Client.all_clients.append(self)

    def rental_days(self):
        """
        Calculates rental days based on arrival date and duration of stay.

        Returns:
            list: A list of rental dates in the format 'dd.mm.yyyy'.
        """
        dates = []
        arrival_day = list(map(int, self.arriving.split('.')))
        for i in range(self.days + 1):
            dates.append([arrival_day[0] + i, arrival_day[1], arrival_day[2]])
        dates = [f'{day:02d}.{month:02d}.{year}' for day, month, year in dates]
        return dates

    @classmethod
    def dates_to_modeling(cls):
        """
        Retrieves unique booking dates from all clients for modeling.

        Returns:
            list: A sorted list of unique booking dates.
        """
        dates_to_modeling = []
        for order in Client.all_clients:
            dates_to_modeling.append(order.booking_date)
        dates_to_modeling = set(dates_to_modeling)
        return sorted(dates_to_modeling)

    def __str__(self):
        """
        Returns a formatted string representation of the Client object.

        Returns:
            str: A string containing booking details.
        """
        return (f'{self.booking_date} {self.name} {self.guests} {self.arriving}'
                f' {self.days} {self.money_to_spend / self.guests}')
