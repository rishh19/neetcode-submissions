class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)

        span = 1
        i = len(self.prices) - 2

        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1

        return span