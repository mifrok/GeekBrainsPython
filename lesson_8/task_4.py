"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
склад. А также класс «Оргтехника», который будет базовым для
классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self):
        self.interface = 'USB'
        self.compatibility = 'Windows'


class Scaner(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.function = 'scan_only'


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.function = 'print_only'


class Xerox(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.function = 'multi_function'


