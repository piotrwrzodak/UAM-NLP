from datetime import datetime
from task1.accounting import *
import csv


def parse_employees_salary():
    with open("task1/csv_data/employee.csv", 'r') as employee_file:
        csv_reader = csv.reader(employee_file)
        # skip header
        next(csv_reader)
        for row in csv_reader:
            emp = Employee(row[0], row[1], int(row[2]))

    return Employee.get_total_salary(emp)


def parse_issued_invoice():
    with open("task1/csv_data/issued_invoice.csv", 'r') as issued_invoice_file:
        csv_reader = csv.reader(issued_invoice_file)
        # skip header
        next(csv_reader)
        for row in csv_reader:
            ii = IssuedInvoice(datetime.strptime(row[0], '%Y-%m-%d'), int(row[1]))

    return IssuedInvoice.get_issued_invoice_by_month(ii)


def parse_received_invoice():
    with open("task1/csv_data/received_invoice.csv", 'r') as received_invoice_file:
        csv_reader = csv.reader(received_invoice_file)
        # skip header
        next(csv_reader)
        for row in csv_reader:
            ri = ReceivedInvoice(datetime.strptime(row[0], '%Y-%m-%d'), int(row[1]))

    return ReceivedInvoice.get_received_invoice_by_month(ri)


def calculate_budget():
    issued_invoice = parse_issued_invoice()
    received_invoice = parse_received_invoice()
    employees_salary = parse_employees_salary()

    # print('issued', issued_invoice)
    # print('received', received_invoice)
    # print('employees', employees_salary)
    # print('')

    keys = list(issued_invoice.keys())
    keys.extend(received_invoice.keys())
    final_keys = list(dict.fromkeys(keys))

    budget_by_month = {}
    for k in final_keys:
        budget_by_month[k] = issued_invoice[k] - received_invoice[k] - employees_salary

    for key, value in budget_by_month.items():
        print(key, value)
