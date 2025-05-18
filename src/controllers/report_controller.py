from src.controllers.customer_controller import login
from src.controllers.booking_controller import show_bookings_by_user
from src.models.reports import ReportBuilder, ServiceBuilder
from src.controllers.global_dicts import reports

report_types = ["Maintenance", "Damage", "Service"]
## list reports by user
def list_user_reports():
    email = input("Enter your email: ")
    for report in reports:
        if report.report_user == email:
            print(report)

## list all reports
def list_reports():
    if len(reports) == 0:
        print("No reports found.")
    else:
        for report in reports:
            print(report)
## add report
def add_relatory():
    customer = login().email
    show_bookings_by_user(customer)

    book_id = input("Choose the booking you want to report on: ")

    booking = bookings.get(book_id)
    if booking is None:
        print("Booking not found.")
        return None
    if booking.customer_email != customer:
        print("This booking does not belong to you.")
        return None
    
    ## TRANSFORM INTO SUBMENU CLASS
    print("Booking found.")
    print("Choose what you want to report")
    print("1 - Maintenance 🛠️")
    print("2 - Damage ⚠️")
    print("3 - Service 🔧")
    print("4 - Exit")
    choice = input("Enter your choice: ")
    if choice == "4":
        print("Exiting...")
        return None
    
    if choice == "3":
        builder = ServiceBuilder()
        cost = float(input("Enter the service cost: "))
        builder.com_cost(cost)
    else:
        builder = ReportBuilder()
    report_type = report_types[int(choice)-1]
    builder.com_report_type(report_type)

    description = input("Describe the issue: ")
    builder.com_report_data(description)
    builder.com_car_id(bookings[book_id].car_id)
    builder.com_report_user(customer)
    report = builder.build()
    reports.append(report)
    print("Report added successfully.")
    return None

    
## delete report
def delete_relatory():
    email = login().email
    list_user_reports(email)
    report = input("Enter the report you want to delete: ")
    if report not in reports:
        print("Report not found.")
        return None
    elif report.report_user != email:
        print("This report does not belong to you.")
        return None
    del reports[report]
    print("Report deleted successfully.")
    return None
