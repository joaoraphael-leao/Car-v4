class CustomerBuilder:
    def __init__(self):
        self.__name = None
        self.__wallet = None
        self.age = None
        self.__email = None

    def com_name(self, name):
        self.__name = name
        return self

    def com_wallet(self, wallet):
        self.__wallet = wallet
        return self

    def com_age(self, age):
        self.age = age
        return self

    def com_email(self, email):
        self.__email = email
        return self

    def com_password(self, password):
        self.__password = password
        return self
    
    def build(self):
        if self.__name is None:
            raise ValueError("Name cannot be None")
        if self.__wallet is None:
            raise ValueError("Wallet cannot be None")
        if self.age is None:
            raise ValueError("Age cannot be None")
        if self.__email is None:
            raise ValueError("Email cannot be None")
        if self.__password is None:
            raise ValueError("Password cannot be None")

        return Customer(self.name, self.__wallet, self.age, self.__email, self.__password)

class Customer:
    def __init__(self, name, email, wallet, age, password):
        self.__name = name
        self.__wallet = wallet
        self.__age = age
        self.__email = email
        self.__password = password  
        self.__id = None # ID will be set later
    
    def __str__(self):
        return f"Customer: {self.name}, Email: {self.__email}, Wallet: {self.__wallet}"
    
    @property
    def wallet(self):
        return self.__wallet
    
    def wallet_add(self, amount):
        self.__wallet += amount

    def wallet_pay(self, amount):
        self.__wallet -= amount
    
    @property
    def email(self):
        return self.__email
    
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password