class Employee:
    def __init__(self, first_name, last_name, phone, salary):
        self._first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.salary = salary

    """getter"""
    @property
    def first_name(self):
        print('getter')
        return self._first_name

    """setter"""
    @first_name.setter
    def first_name(self, value):
        print('setter')
        self._first_name = value

    """deleter"""
    @first_name.deleter
    def first_name(self):
        print('del')
        self._first_name = None


g1 = Employee('a', 'b', "989898", 5000)
g1.first_name = 'ali'
print(g1.first_name)
del g1.first_name
print(g1.first_name)
