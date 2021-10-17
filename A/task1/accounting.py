class Employee:
    totalSalary = 0

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        Employee.totalSalary += salary

    def get_total_salary(self):
        return Employee.totalSalary


class ReceivedInvoice:
    receivedInvoiceByMonth = {}

    def __init__(self, date, amount):
        self.date = date
        self.amount = amount
        self.add_invoice()

    def add_invoice(self):
        key = str(self.date.year) + '.' + str(self.date.month)
        if key in ReceivedInvoice.receivedInvoiceByMonth:
            prev_state = ReceivedInvoice.receivedInvoiceByMonth.get(key)
            ReceivedInvoice.receivedInvoiceByMonth.update({key: prev_state + self.amount})
        else:
            ReceivedInvoice.receivedInvoiceByMonth[key] = self.amount

    def get_received_invoice_by_month(self):
        return ReceivedInvoice.receivedInvoiceByMonth


class IssuedInvoice:
    issuedInvoiceByMonth = {}

    def __init__(self, date, amount):
        self.date = date
        self.amount = amount
        self.add_invoice()

    def add_invoice(self):
        key = str(self.date.year) + '.' + str(self.date.month)
        if key in IssuedInvoice.issuedInvoiceByMonth:
            prev_state = IssuedInvoice.issuedInvoiceByMonth.get(key)
            IssuedInvoice.issuedInvoiceByMonth.update({key: prev_state + self.amount})
        else:
            IssuedInvoice.issuedInvoiceByMonth[key] = self.amount

    def get_issued_invoice_by_month(self):
        return IssuedInvoice.issuedInvoiceByMonth

