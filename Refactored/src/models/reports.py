from typing import override

class ReportBuilder:
    def __init__(self):
        self.car_id = None
        self.report_user = None
        self.report_name = None
        self.report_type = None
        self.report_data = None

    def com_report_user(self, report_user):
        self.report_user = report_user
        return self

    def com_car_id(self, car_id):
        self.car_id = car_id
        return self

    def com_report_name(self, report_name):
        self.report_name = report_name
        return self

    def com_report_type(self, report_type):
        self.report_type = report_type
        return self

    def com_report_data(self, report_data):
        self.report_data = report_data
        return self

    def builder(self):
        if not self.car_id:
            raise ValueError("Car ID is required")
        if not self.report_name:
            raise ValueError("Report Name is required")
        if not self.report_type:
            raise ValueError("Report Type is required")
        if not self.report_data:
            raise ValueError("Report Data is required")
        return Report(self.car_id, self.report_name, self.report_type, self.report_data, self.report_user)    

                    
class ServiceBuilder(ReportBuilder):
    def __init__(self):
        super().__init__()
        self.cost = None

    def com_cost(self, cost):
        self.cost = cost
        return self
        
    @override
    def builder(self):
        if not self.car_id:
            raise ValueError("Car ID is required")
        if not self.report_name:
            raise ValueError("Report Name is required")
        if not self.report_type:
            raise ValueError("Report Type is required")
        if not self.report_data:
            raise ValueError("Report Data is required")
        if not self.cost:
            raise ValueError("Cost is required")

        return Service(self.car_id, self.report_name, self.report_type, self.report_data, self.cost, self.report_user)

class Report:
    def __init__(self, car_id, report_name, report_type, report_data, user):
        self.car_id = car_id
        self.report_name = report_name
        self.report_type = report_type
        self.report_data = report_data
        self.report_user = user
    
    def __str__(self):
        return f"Car ID: {self.car_id}\nReport Name: {self.report_name}\nReport Type: {self.report_type}\nReport Data: {self.report_data}"

class Service(Report):
    def __init__(self, car_id, report_name, report_type, report_data, cost, user):
        super().__init__(car_id, report_name, report_type, report_data, user)
        self.cost = cost
    @override
    def __str__(self):
        return super().__str__() + f"\nCost: {self.cost}"