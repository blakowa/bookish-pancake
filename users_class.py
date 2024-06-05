
class Users:
    def __init__(self, first_name, last_name, birth, department, internal_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.department = department
        self.internal_phone = internal_phone
        self.login_attempts = 0
        
    def describe_user(self):
        print(f'Ten użytkownik nazywa się {self.first_name.title()} {self.last_name.title()}, urodzony {self.birth}, pracuje w {self.department}, jego wewenętrzny numer telefonu to {self.internal_phone}.')

    def greet_user(self):
        print(f'Witaj {self.first_name.title()}!')

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

marek_nowak = Users('Marek', 'Nowak', '12/07/2000', 'accounting', 1234)
marek_nowak.describe_user()
marek_nowak.greet_user()

marek_nowak.increment_login_attempts()
print(f'{marek_nowak.login_attempts}')
marek_nowak.increment_login_attempts()
marek_nowak.increment_login_attempts()
marek_nowak.increment_login_attempts()
print(f'{marek_nowak.login_attempts}')
marek_nowak.reset_login_attempts()
print(f'{marek_nowak.login_attempts}')

# ala_makota = Users('ala', 'makota', '03/04/1987', 'HR', 3421)
# ala_makota.describe_user()
# ala_makota.greet_user()

# jan_kowalski = Users('jan', 'kowalski', '14/02/1969', 'stores', 3246)
# jan_kowalski.describe_user()
# jan_kowalski.greet_user()