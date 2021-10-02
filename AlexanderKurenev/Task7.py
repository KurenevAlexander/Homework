from functools import total_ordering


@total_ordering
class Money:
    exchange_rate = {
        "EUR": 0.93,
        "BYN": 2.1,
        "USD": 1,
        "JPY": 3.58,
        "": 1
    }

    def __init__(self, value, currency="USD"):
        self.value = value
        self.currency = currency

    def __str__(self):
        return f"{self.value} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.value + other.value * Money.exchange_rate[self.currency] /
                         Money.exchange_rate[other.currency], self.currency)
        if isinstance(other, (int, float)):
            return Money(self.value + other, self.currency)
        raise AttributeError

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Money):
            return Money(self.value * (other.value * Money.exchange_rate[self.currency] /
                                       Money.exchange_rate[other.currency]), self.currency)
        if isinstance(other, (int, float)):
            return Money(self.value * other, self.currency)
        raise AttributeError

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Money):
            return Money(self.value / (other.value * Money.exchange_rate[self.currency] /
                                       Money.exchange_rate[other.currency]), self.currency)
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError
            return Money(self.value / other, self.currency)
        raise AttributeError

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Money(other / self.value, self.currency)
        raise AttributeError

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self.value - other.value * Money.exchange_rate[self.currency] /
                         Money.exchange_rate[other.currency], self.currency)
        if isinstance(other, (int, float)):
            return Money(self.value - other, self.currency)
        raise AttributeError

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Money(-self.value + other, self.currency)
        raise AttributeError

    def __eq__(self, other):
        print('run eq')
        if isinstance(other, Money):
            return self.value == other.value * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency]
        if isinstance(other, (int, float)):
            return self.value == other
        raise AttributeError

    def __lt__(self, other):
        print('lt run')
        if isinstance(other, Money):
            return self.value < other.value * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency]
        if isinstance(other, (int, float)):
            return self.value < other
        raise AttributeError

    def __le__(self, other):
        return self == other or self < other


if __name__ == '__main__':
    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")
    print(z + 3.11 * x + y * 0.8)

    lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    print(s)
