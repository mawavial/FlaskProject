from models.person_model import Person


class Driver(Person):
    """ Class representing a Client """
    def __init__(self, driver_id, name, email, cellphone, address, license_number, license_country):
        super(Driver, self).__init__(driver_id, name, email, cellphone, address)
        self.license_number = license_number
        self.license_country = license_country

    def to_dict(self):
        dict_init = self.__dict__
        return dict_init
