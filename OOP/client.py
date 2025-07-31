class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []
        
class IndividualClient(Client):
    def __init__(self, name, address, birth_date, ssn):
        super().__init__(address)
        self.name = name
        self.birth_date = birth_date
        self.ssn = ssn