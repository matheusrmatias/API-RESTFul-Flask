class Client():
    def __init__(self, name, fone, maritalStatus, address):
        self.__name = name
        self.__fone = fone
        self.__maritalStatus = maritalStatus
        self.__address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone):
        self.__fone = fone

    @property
    def maritalStatus(self):
        return self.__maritalStatus

    @maritalStatus.setter
    def maritalStatus(self, maritalStatus):
        self.__maritalStatus = maritalStatus

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address
