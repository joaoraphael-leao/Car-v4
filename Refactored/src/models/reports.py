from typing import override


class Report:
    def __init__(self, car_id, report_name, report_type, report_data):
        self.car_id = car_id
        self.report_name = report_name
        self.report_type = report_type
        self.report_data = report_data
    
    def __str__(self):
        return f"Car ID: {self.car_id}\nReport Name: {self.report_name}\nReport Type: {self.report_type}\nReport Data: {self.report_data}"

class Service(Report):
    def __init__(self, car_id, report_name, report_type, report_data, cost):
        super().__init__(car_id, report_name, report_type, report_data)
        self.cost = cost
    @override
    def __str__(self):
        return super().__str__() + f"\nCost: {self.cost}"