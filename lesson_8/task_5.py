"""Продолжить работу над первым заданием. Разработать методы, отвечающие за
приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.
"""


class Warehouse:
    def __init__(self):
        self.equipment = {}

    def add_to_warehouse(self, equipment):
        try:
            amount = int(input('Type amount of {} to add to warehouse: '
                               .format(equipment.name)))
        except ValueError:
            print('Incorrect amount')
            return
        try:
            self.equipment[equipment.name] += amount
        except KeyError:
            self.equipment[equipment.name] = amount

    def send_equipment_to_company(self, company, equipment):
        try:
            amount = int(input('Type amount of {} to send to {}: '
                               .format(equipment.name, company.name)))
        except ValueError:
            print('Incorrect amount')
            return
        try:
            if self.equipment[equipment.name] < amount:
                print('Not enough equipment in warehouse')
                return
        except KeyError:
            print('Equipment "{}" out of stock'.format(equipment.name))
            return
        try:
            company.equipment[equipment.name] += amount
            self.equipment[equipment.name] -= amount
        except KeyError:
            company.equipment[equipment.name] = amount
            self.equipment[equipment.name] -= amount


class OfficeEquipment:
    def __init__(self):
        self.interface = 'USB'
        self.compatibility = 'Windows'


class Scaner(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.function = 'scan_only'
        self.name = 'Scaner'


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.function = 'print_only'
        self.name = 'Printer'


class Xerox(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.function = 'multi_function'
        self.name = 'Xerox'


class Department:
    def __init__(self, name):
        self.equipment = {}
        self.name = name


warehouse = Warehouse()
printer = Printer()
scaner = Scaner()
xerox = Xerox()
office = Department('Office')
factory = Department('Factory')
security = Department('Security')

warehouse.add_to_warehouse(printer)
warehouse.add_to_warehouse(scaner)
warehouse.add_to_warehouse(xerox)
warehouse.send_equipment_to_company(office, xerox)
warehouse.send_equipment_to_company(factory, printer)
warehouse.send_equipment_to_company(security, scaner)
print(warehouse.equipment)
print(office.equipment)
print(factory.equipment)
print(security.equipment)
