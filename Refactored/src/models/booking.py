class BookingBuilder:
    def __init__(self):
        self.__id = None
        self.__car_id = None
        self.__customer_email = None
        self.__start_date = None
        self.__end_date = None
        self.__cost = None
        self.__longitude = None
        self.__latitude = None
    
    def com_location(self, longitude, latitude):
        self.__longitude = longitude
        self.__latitude = latitude
        return self

    def com_id(self, id_passed):
        self.__id = id_passed
        return self

    def com_car_id(self, car_id):
        self.__car_id = car_id
        return self

    def com_customer_email(self, customer_email):
        self.__customer_email = customer_email
        return self

    def com_start_date(self, start_date):
        self.__start_date = start_date
        return self

    def com_end_date(self, end_date):
        self.__end_date = end_date
        return self

    def com_cost(self, cost):
        self.__cost = cost
        return self

    def build(self):
        if self.__car_id is None:
            raise ValueError("Car ID is required")
        if self.__customer_email is None:
            raise ValueError("Customer ID is required")
        if self.__start_date is None:
            raise ValueError("Start date is required")
        if self.__end_date is None:
            raise ValueError("End date is required")
        if self.__cost is None:
            raise ValueError("Cost is required")

        return Booking(self.__car_id, self.__customer_email, self.__start_date, self.__end_date, self.__cost, self.__id, self.__longitude, self.__latitude)

class Booking:
    def __init__(self, car_id, customer_email, start_date, end_date, cost, id_passed, longitude, latitude):
        self.__car_id = car_id
        self.__customer_email = customer_email
        self.__start_date = start_date
        self.__car_id = car_id
        self.__customer_email = customer_email
        self.__start_date = start_date
        self.__end_date = end_date
        self.__cost = cost
        self.__id= id_passed
        self.__longitude = longitude
        self.__latitude = latitude
    
    def __str__(self):
        return f"Booking ID: {self.__id}\n  Car ID: {self.__car_id}\nCustomer Email: {self.__customer_email}\nStart Date: {self.__start_date}\nEnd Date: {self.__end_date}\nCost: {self.__cost}"

    def set_id(self, id):
        if self.__id is not None:
            raise ValueError("ID cannot be changed")
        self.__id = id

    @property
    def longitude(self):
        return self.__longitude

    @property
    def latitude(self):
        return self.__latitude

    @property
    def car_id(self):
        return self.__car_id

    @property
    def id(self):
        return self.__id
    
    @property
    def car_id(self):
        return self.__car_id

    @property
    def customer_email(self):
        return self.__customer_email

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date
    
    @property
    def customer_id(self):
        return self.__customer_id
