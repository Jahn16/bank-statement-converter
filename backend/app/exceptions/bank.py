class BankNotSupported(Exception):
    def __init__(self, bank_name: str):
        self.bank_name = bank_name
        super().__init__(f"Bank {bank_name} is not supported")
