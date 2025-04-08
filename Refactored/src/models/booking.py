import re
from turtle import st


class BookingBuilder:
    def __init__(self):
        self.__car_id = None
        self.__customer_id = None
        self.__start_date = None
        self.__end_date = None
    
    def com_car_id(self, car_id):
        self.__car_id = car_id
        return self

    def com_customer_id(self, customer_id):
        self.__customer_id = customer_id
        return self

    def com_start_date(self, start_date):
        self.__start_date = start_date
        return self

    def com_end_date(self, end_date):
        self.__end_date = end_date
        return self

    def build(self):
        if self.__car_id is None:
            raise ValueError("Car ID is required")
        if self.__customer_id is None:
            raise ValueError("Customer ID is required")
        if self.__start_date is None:
            raise ValueError("Start date is required")
        if self.__end_date is None:
            raise ValueError("End date is required")

        return Booking(self.__car_id, self.__customer_id, self.__start_date, self.__end_date)

class Booking:
    def __init__(self, car_id, customer_id, start_date, end_date):
        self.__car_id = car_id
        self.__customer_id = customer_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__id= None

    def set_id(self, id):
        if self.__id is not None:
            raise ValueError("ID cannot be changed")
        self.__id = id

    @property
    def id(self):
        return self.__id
    
    @property
    def car_id(self):
        return self.__car_id

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date
    
    def change_date(self, start_date, end_date):
        if start_date > end_date:
            raise ValueError("Start date must be before end date")

        self.__start_date = start_date
        self.__end_date = end_date
    
    def change_car_id(self, car_id):
        self.__car_id = car_id

    @property
    def customer_id(self):
        return self.__customer_id
