
#Create new class for a CustomerBankAccount

class CustomerBankAccount:
    
    #Create fields for Account Number, Balance, Customer Name, Email, and Phone Number
    def __init__(self, account_number, balance, name, email, phone):
        self.account_number = account_number
        self.balance = balance
        self.name = name
        self.email = email
        self.phone = phone
        
    ## Write some getter and setters for each field
    
    # account_number GET
    @property
    def get_account_number(self):
        return self.account_number
    # account_number SET
    @get_account_number.setter
    def update_account_number(self, account_number):
        self.account_number = account_number
    # balance GET
    @property
    def get_balance(self):
        return self.balance
    # balance SET
    @get_balance.setter
    def update_balance(self, balance):
        self.balance = balance
    # name GET
    @property
    def get_name(self):
        return self.name
    # name SET
    @get_name.setter
    def update_name(self,name):
        self.name = name
    # email GET
    @property
    def get_email(self):
        return self.email
    # email SET
    @get_email.setter
    def update_email(self, email):
        self.email = email
    # phone GET
    @property
    def get_phone_number(self):
        return self.phone
    # phone SET
    @get_phone_number.setter
    def update_phone(self, phone):
        self.phone = phone
    
        
        
        
    ########
    ## Create two additional Methods
    # One to allow the customer to deposit the funds
    # One to allow the customer to withdraw funds
    
    # Deposits money to balance
    def save_money(self, amount):
        if isinstance(amount, int):
            print(f'You deposited {amount} in your account that previously had a balance of {self.balance}')
            self.balance = self.balance + amount
            print(f'Your new total balance is {self.balance}! Thanks for banking with us!')

    # Withdraws money if available within balance
    
    def take_money(self, amount):
        desired_change = self.balance - amount
        if isinstance(amount, int) and desired_change >= 0:
            print(f'Your previous balance was {self.balance}')
            self.balance = self.balance - amount
            print(f'You have successfully withdrawn {amount}, your new balance is {self.balance}')
        else:
            print("Insufficient funds.")
     
### Creating an instance###

account_number = 7867812
balance = 200
name = "Phil"
email = "phil@email.com"
phone = "407-867-5309"

############################

# Creating an instance
customer = CustomerBankAccount(account_number, balance, name, email, phone)

print(customer.balance)
customer.save_money(3200)
customer.take_money(1000)
customer.take_money(2200)
customer.save_money(200)
customer.take_money(500)
