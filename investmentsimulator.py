from pyfiglet import Figlet


dictofbanks = {'JPMorgan Chase': 0.01, 'Bank of America': 0.01, 'Wells Fargo': 0.01,
               'Citi Bank': 0.01, 'US Bank': 3.40, 'Capital One': 3.00, 'PNC Bank': 0.01, 'Goldman Sachs': 3.40,
               'Triust': 0.01, 'TD Bank': 0.01}

class Account:
    def __init__(self, amount = 0, bank = None, years = None):
        self.amount = amount
        self.bank = bank
        self.years = years
        self.rate = dictofbanks[bank]

    def __str__(self):
        return str(self.amount)

    def simulate_interest(self):
        return self.amount * (1 + self.rate/100) ** self.years

def verify_bank(bank):
    if bank not in dictofbanks:
        print(f"Sorry, {bank} is not in our database!")
        return None
    else:
        return bank

def verify_years(years):
    if years < 0:
        print("Invalid Year Amount")
        return None
    return years



def verify_amount(amount):
    if amount < 0:
        print("Invalid Amount")
        return None
    return amount

f = Figlet(font="slant")
print(f.renderText("Bank Simulator"))

def main():
        while True:
            print(f"\nAvailable Banks!\n")
            for banks in dictofbanks:
                print(banks)
            bank = verify_bank(input("Choose a bank!: "))
            if bank:
                break

        while True:
            try:
                amount = int(input("How much are you depositing?: "))
            except ValueError:
                print("Input must be a number!")
                continue
            if amount < 0:
                print("Amount must be positive!")
                continue

            amount = verify_amount(amount)

            if bank == "US Bank" and amount < 25000:
                print(f"US Bank requires $25000 to open an account!")
                continue
            if amount:
                break

        while True:
            try:
                years = int(input("How many years to simulate?: "))
            except ValueError:
                print("Input must be a number!")
                continue
            if years:
                break

        account = Account(amount, bank, years)

        print(f"\n====== Investment Summary ========")
        print(f"Bank: {bank}")
        print(f"Interest Rate: {dictofbanks[bank]}% APY")
        print(f"Initial Deposit: ${amount:,.2f}")
        print(f"Years: {years}")
        print(f"Interest Earned: ${account.simulate_interest() - amount:,.2f}")
        print(f"Final Amount: ${account.simulate_interest():,.2f}")

if __name__ == "__main__":
    main()
