## Before
class AccountType(object):
    pass


class Account(object):
    __slots__ = ['__account_type', '__rate']

    def __init__(self, account_type, rate):
        self.__account_type = account_type
        self.__rate = rate

    def interest_for_amount_days(self, amount, days):
        return self.__rate * amount * days / 365


##After
class AccountType2(object):
    __slots__ = ['__rate']

    def __init__(self, rate):
        self.__rate = rate

    def get_rate(self):
        return self.__rate


class Account2(object):
    __slots__ = ['__account_type']

    def __init__(self, account_type):
        self.__account_type = account_type

    def interest_for_amount_days(self, amount, days):
        return self.__account_type.get_rate() * amount * days / 365


if __name__ == '__main__':
    account = Account(AccountType(), 1.1)
    account2 = Account2(AccountType2(1.1))

    assert (account.interest_for_amount_days(1000, 100) ==
                account2.interest_for_amount_days(1000, 100))
