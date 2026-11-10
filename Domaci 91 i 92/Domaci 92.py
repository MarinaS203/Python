# 1.Kreirati klasu BankAccount koja predstavlja bankovni račun.
# Klasa treba da ima sledeće atribute:
# owner – ime vlasnika računa;
# balance – trenutno stanje na računu.

# Implementirati sledeće metode:
# 1.deposit(amount: float) -> BankAccount – uvećava stanje na
# računu za zadati iznos. Ako je iznos pozitivan, izvršava uplatu.
# Vraća objekat nad kojim je metoda pozvana.
# 2.withdraw(amount: float) -> BankAccount – umanjuje stanje
# na računu za zadati iznos. Isplata se izvršava samo ako je
# iznos pozitivan i ako na računu ima dovoljno novca. Vraća
# objekat nad kojim je metoda pozvana.
# 3.display_balance() -> None – ispisuje trenutno stanje na
# računu.
# Kreirati objekat klase BankAccount i omogućiti izvršavanje
# sledećeg niza poziva:
# account = BankAccount("Ana", 10000)
# account.deposit(5000).withdraw(2000).deposit(1000)
# account.display_balance()

# Očekivani izlaz:
# Stanje na racunu: 14000

class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance

    def __repr__(self):
        return f'Account owner: {self.owner}, Balance: {self.balance}'
    
    def deposit(self, amount:float):
        if amount>=0:
           self.balance+=amount 
        return self
    
    def withdraw(self, amount: float):
        if amount>=0 and self.balance>=amount:
            self.balance-=amount
        return self
    
    def display_balance(self) -> None:
        print (f'Stanje na racunu: {self.balance}')

account = BankAccount("Ana", 10000)
print(account)
account.deposit(5000).withdraw(2000).deposit(1000)
account.display_balance()
