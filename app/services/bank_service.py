from app.libraries import OnlineBankingAbstracts


class BankService(object):

    def __init__(self, bank_lib):
        if not isinstance(bank_lib, OnlineBankingAbstracts):
            raise TypeError('The parameter bank_lib must be an instance of OnlineBankingAbstracts')

        self.bank_lib = bank_lib

        self.mutation_history = self.bank_lib.mutation_history
        self.mutation_since_today = self.bank_lib.mutation_since_today
        self.mutation_since_first_of_month = self.bank_lib.mutation_since_first_of_month
        self.mutation_since_1_week_ago = self.bank_lib.mutation_since_1_week_ago
        self.mutation_since_2_weeks_ago = self.bank_lib.mutation_since_2_weeks_ago
        self.mutation_since_3_weeks_ago = self.bank_lib.mutation_since_3_weeks_ago
        self.mutation_since_30_days_ago = self.bank_lib.mutation_since_30_days_ago