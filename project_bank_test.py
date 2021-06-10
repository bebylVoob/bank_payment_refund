bank_dict = {}
transaction_dict = {}
account = {}


class Bank:
    name = ''
    is_refund = False
    
    def create_bank(self, bank_name=''):
        self.name = input("ENTER BANK NAME : ").strip().lower() if not bank_name else bank_name
        refund = input("THIS BANK IS ALLOW TO REFUND? (y/n) : ").strip().lower()
        if not isinstance(refund, str) or refund not in ['y', 'n']:
            print('INVALID VALUE, PLEASE TRY AGAIN')
            self.create_bank()
        else:
            self.is_refund = True if refund == 'y' else False
            bank_dict.update({self.name: self.is_refund})
            print('BANK \'%s\' WAS CREATED' % self.name)

    def list_bank(self):
        print("BANK LIST: ")
        for bank_name in bank_dict:
            print('\t%s' % bank_name)


ch = ''


def makePayment(bank_name, amount):
    if bank_dict.get(bank_name, None) is not None:
        transaction_dict.update({bank_name: amount})
        print('TRANSACTION SUCCESS!!')
        refund = input("DO YOU NEED TO REFUND? (Y/N) : ").strip().lower()
        if not isinstance(refund, str) or refund not in ['y', 'n']:
            print('WRONG VALUE, NOT REFUND NOW!')
            return bank_name
        else:
            refund = True if refund is 'y' else False
            refundPayment(bank_name) if refund else bank_name
        return bank_name
    else:
        print('BANK ACCOUNT NOT REGISTER!!, PLEASE SIGN UP AND TRY AGAIN')
        bank = Bank()
        bank.create_bank()
        makePayment(bank.name, amount)

def refundPayment(bank_name=''):
    if bank_dict.get(bank_name, None) is not None or transaction_dict.get(bank_name, None):
        if bank_dict[bank_name]:
            transaction = transaction_dict[bank_name]
            del transaction_dict[bank_name]
            print('YOU GOT REFUND %s FROM %s SUCCESS' % (transaction, bank_name))
        else:
            print('THIS BANK CAN NOT REFUND, SORRY.')
    else:
        print('BANK ACCOUNT HAVE NO TRANSACTION')

while ch != 0:
    print("MAIN MENU")
    print("1. NEW BANK")
    print("2. LIST BANK")
    print("3. MAKE PAYMENT")
    print("4. MAKE PAYMENT LIST")
    print("5. MAKE REFUND")
    print("6. MAKE REFUND LIST")
    print("0. EXIT")
    ch = input('CHOICE MENU: ')
    
    if ch == '1':
        bank = Bank()
        bank.create_bank()
    elif ch == '2':
        bank = Bank()
        bank.list_bank()
    elif ch == '3':
        bank_name = input('ENTER BANK NAME : ').lower().strip()
        amount = int(input('ENTER YOUR AMOUNT: '))
        transaction_no = makePayment(bank_name, amount)
        print('RESPONSE OF MAKE PAYMENT FOR REFUND IS : %s' % transaction_no)
    elif ch == '4':
        bank_name_list = (input('ENTER BANK NAME LIST (EX: A, B, C): ').lower().strip()).split(',')
        amount = int(input('ENTER YOUR AMOUNT: '))
        for bank_name in bank_name_list:
            transaction_no = makePayment(bank_name, amount)
            print('RESPONSE MAKE PAYMENT OF %s FOR REFUND IS : %s' % (bank_name, transaction_no))
    elif ch == '5':
        bank_name = input('ENTER BANK NAME(TRANSACTION): ')
        refundPayment(bank_name)
    elif ch == '6':
        bank_name_list = (input('ENTER BANK NAME(TRANSACTION) LIST: ').lower().strip()).split(',')
        for bank_name in bank_name_list:
            refundPayment(bank_name)
    elif ch == '0':
        break
    else:
        print("Invalid choice")
