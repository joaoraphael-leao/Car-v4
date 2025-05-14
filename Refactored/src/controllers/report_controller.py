from src.controllers.customer_controller import login
from src.controllers.booking_controller import show_bookings_by_user
from src.models.reports import ReportBuilder, ServiceBuilder
from src.controllers.global_dicts import reports

report_types = ["Maintenance", "Damage", "Service"]
## listar relatórios por usuário
def list_user_reports():
    email = input("Enter your email: ")
    for report in reports:
        if report.report_user == email:
            print(report)

## listar relatórios
def list_reports():
    if len(reports) == 0:
        print("Nenhum relatório encontrado.")
    else:
        for report in reports:
            print(report)
## adicionar relatório
def add_relatory():
    customer = login().email
    show_bookings_by_user(customer)

    book_id = input("Escolha a reserva no qual você tem um relatório a fazer: ")

    booking = bookings.get(book_id)
    if booking is None:
        print("Reserva não encontrada.")
        return None
    if booking.customer_email != customer:
        print("Essa reserva não pertence a você.")
        return None
    
    ## TRANSFORMAR EM CLASSE DE SUBMENU
    print("Reserva encontrada.")
    print("Escolha o que quer relatar")
    print("1 - Maintenance 🛠️")
    print("2 - Damage ⚠️")
    print("3 - Service 🔧")
    print("4 - Sair")
    choice = input("Digite sua escolha: ")
    if choice == "4":
        print("Saindo...")
        return None
    
    if choice == "3":
        builder = ServiceBuilder()
        cost = float(input("Digite o custo do serviço: "))
        builder.com_cost(cost)
    else:
        builder = ReportBuilder()
    report_type = report_types[int(choice)-1]
    builder.com_report_type(report_type)

    description = input("Descreva o problema: ")
    builder.com_report_data(description)
    builder.com_car_id(bookings[book].car_id)
    builder.com_report_user(customer)
    report = builder.build()
    reports.append(report)
    print("Relatório adicionado com sucesso.")
    return None

    
## excluir relatório
def delete_relatory():
    email = login().email
    list_user_reports(email)
    report = input("Digite o relatório que você quer excluir: ")
    if report not in reports:
        print("Relatório não encontrado.")
        return None
    elif report.report_user != email:
        print("Esse relatório não pertence a você.")
        return None
    del reports[report]
    print("Relatório excluído com sucesso.")
    return None
