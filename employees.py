class Company(object):

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def get_name(self):
        return self.name

    # Add the remaining methods to fill the requirements above
    def get_title(self):
        return self.title

    def get_start_date(self):
        return self.start_date

new_employee = Company('Russell', 'developer', '5-aug-2016')

print('{0} became a {1} on {2}'.format(new_employee.get_name(), new_employee.get_title(), new_employee.get_start_date()))


import code
code.interact(local=locals())
