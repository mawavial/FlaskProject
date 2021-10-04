from models.person_model import Person


class Client(Person):
    """ Class representing a Client """
    def __init__(self, ci, age, name, email, cellphone, address, nit):
        super(Client, self).__init__(ci, age, name, email, cellphone, address)
        self.nit = nit

    def to_dict(self):
        dict_init = self.__dict__
        return dict_init
