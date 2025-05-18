from src.controllers.global_dicts import customers

class CustomerBuilder:
    def __init__(self):
        self.__name = None
        self.__wallet = None
        self.__email = None
        self.__password = None
        self.__id = None

    def com_id(self, id):
        self.__id = id
        return self

    def com_name(self, name):
        self.__name = name
        return self

    def com_wallet(self, wallet):
        self.__wallet = wallet
        return self

    def com_email(self, email):
        self.__email = email
        return self

    def com_password(self, password):
        self.__password = password
        return self
    
    def build(self):
        if customers.get(self.__email):
            raise ValueError("Email already in use")
        if self.__name is None:
            raise ValueError("Name cannot be None")
        if self.__wallet is None:
            raise ValueError("Wallet cannot be None")

        if self.__email is None:
            raise ValueError("Email cannot be None")
        if self.__password is None:
            raise ValueError("Password cannot be None")

        return Customer(self.__name, self.__email, self.__wallet, self.__password, self.__id)

class Customer:
    def __init__(self, name, email, wallet, password, id):
        self.__name = name
        self.__wallet = wallet
        self.__email = email
        self.__password = password  
        self.__id = id
        self.__debts = 0
    
    def __str__(self):
        return f"Customer: {self.name}, Email: {self.__email}, Wallet: {self.__wallet}"
    
    @property
    def wallet(self):
        return self.__wallet
    
    def wallet_add(self, amount):
        self.__wallet += amount

    def wallet_get(self, amount):
        self.__wallet -= amount
        return amount
    
    @property
    def email(self):
        return self.__email
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password
    
    def add_debts(self, amount):
        self.__debts += amount

    def has_debts(self):
        return self.__debts > 0
