from business.person import Person

class Client(Person):
    def __init__(self, name, email, cellphone, address, nit):
        super(Client, self).__init__(name, email, cellphone, address)
        self.nit = nit

    def _to_dict(self):
        return self.__dict__

    def get_all_routes(self):
        pass