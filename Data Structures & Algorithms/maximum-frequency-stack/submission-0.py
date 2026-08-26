class FreqStack:

    def __init__(self):
        self.frequency = {}
        self.group = {}
        self.max_frequency = 0

    def push(self, val):
        self.frequency[val] = self.frequency.get(val, 0) + 1

        freq = self.frequency[val]

        if freq not in self.group:
            self.group[freq] = []

        self.group[freq].append(val)

        if freq > self.max_frequency:
            self.max_frequency = freq

    def pop(self):
        val = self.group[self.max_frequency].pop()

        self.frequency[val] -= 1

        if len(self.group[self.max_frequency]) == 0:
            self.max_frequency -= 1

        return val