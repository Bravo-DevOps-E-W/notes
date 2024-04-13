from .User import User

class Premium_User(User):
    def __init__(self, name, email, address, license):
        super().__init__(name, email, address, license, is_premium=True)
        
