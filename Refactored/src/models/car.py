from typing import override

class Car:
    def __init__(self, model, brand, year, license_plate, daily_rate, is_available=True):
        self.__id = None
        self.__model = model
        self.__brand = brand
        self.__year = year
        self.__license_plate = license_plate
        self.__daily_rate = daily_rate
        self.__is_available = is_available
    
    def set_id(self, id):
        if self.__id is not None:
            raise ValueError("ID cannot be changed")
        self.__id = id

    @property
    def id(self):
        return self.__id
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise TypeError("Model must be a string")
        if not value:
            raise ValueError("Model cannot be empty")
        self.__model = value
    
    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise TypeError("Brand must be a string")
        if not value:
            raise ValueError("Brand cannot be empty")
        self.__brand = value
    
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError("Year must be an integer")
        if value < 1900 or value > 2100:
            raise ValueError("Year must be between 1900 and 2100")
        self.__year = value
    
    @property
    def license_plate(self):
        return self.__license_plate
    
    @license_plate.setter
    def license_plate(self, value):
        if not isinstance(value, str):
            raise TypeError("License plate must be a string")
        if not value:
            raise ValueError("License plate cannot be empty")
        self.__license_plate = value
    
    @property
    def daily_rate(self):
        return self.__daily_rate
    
    @daily_rate.setter
    def daily_rate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Daily rate must be a number")
        if value <= 0:
            raise ValueError("Daily rate must be positive")
        self.__daily_rate = value
    
    @property
    def is_available(self):
        return self.__is_available
    
    @is_available.setter
    def is_available(self, value):
        if not isinstance(value, bool):
            raise TypeError("Availability must be a boolean")
        self.__is_available = value
    
    def check_availability(self):
        return self.is_available
    
    def __str__(self):
        return f"ID: {self.id}\nModel: {self.model}\nBrand: {self.brand}\nYear: {self.year}\nLicense Plate: {self.license_plate}\nDaily Rate: R${self.daily_rate}/day\nAvailable: {self.is_available}"


class CarBuilder:
    def __init__(self):
        self.id = None
        self.model = None
        self.brand = None
        self.year = None
        self.license_plate = None
        self.daily_rate = None
        self.is_available = True
    
    def com_id(self, id):
        self.id = id
        return self
    
    def com_model(self, model):
        self.model = model
        return self
    
    def com_brand(self, brand):
        self.brand = brand
        return self
    
    def com_year(self, year):
        self.year = year
        return self
    
    def com_license_plate(self, license_plate):
        self.license_plate = license_plate
        return self
    
    def com_daily_rate(self, daily_rate):
        self.daily_rate = daily_rate
        return self
    
    def com_availability(self, is_available):
        self.is_available = is_available
        return self
    
    def builder(self):
        if not self.id:
            raise ValueError("ID is required")
        if not self.model:
            raise ValueError("Model is required")
        if not self.brand:
            raise ValueError("Brand is required")
        if not self.year:
            raise ValueError("Year is required")
        if not self.license_plate:
            raise ValueError("License plate is required")
        if not self.daily_rate:
            raise ValueError("Daily rate is required")
        
        return Car(self.id, self.model, self.brand, self.year, 
                  self.license_plate, self.daily_rate, self.is_available)