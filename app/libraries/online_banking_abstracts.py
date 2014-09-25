from abc import abstractmethod
from datetime import datetime, date


class OnlineBankingAbstracts(object):

    @abstractmethod
    def mutation_history(self, start_date, end_date):
        raise NotImplementedError('The method mutation_history is not implemented')

    def mutation_since_today(self):
        return self.mutation_history(start_date=self.today(),
                                     end_date=self.today())

    def mutation_since_first_of_month(self):
        return self.mutation_history(start_date=self.first_of_month(),
                                     end_date=self.today())

    def mutation_since_1_week_ago(self):
        return self.mutation_history(start_date=self.one_week_ago(),
                                     end_date=self.today())

    def mutation_since_2_weeks_ago(self):
        return self.mutation_history(start_date=self.two_weeks_ago(),
                                     end_date=self.today())

    def mutation_since_3_weeks_ago(self):
        return self.mutation_history(start_date=self.three_weeks_ago(),
                                     end_date=self.today())

    def mutation_since_30_days_ago(self):
        return self.mutation_history(start_date=self.thirty_days_ago(),
                                     end_date=self.today())

    def today(self):
        return datetime.now()

    def first_of_month(self):
        d = self.today()
        return date(d.year, d.month, 1)

    def yesterday(self):
        return self.x_days_ago(1)

    def one_week_ago(self):
        return self.x_days_ago(7)

    def two_weeks_ago(self):
        return self.x_days_ago(14)

    def three_weeks_ago(self):
        return self.x_days_ago(21)

    def thirty_days_ago(self):
        return self.x_days_ago(30)

    def x_days_ago(self, x):
        return date.fromordinal(date.today().toordinal()-x)
