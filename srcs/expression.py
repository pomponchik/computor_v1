class Expression:
    def __init__(self, items):
        self.items = items
        self.redused_items = self.reduce()

    def __repr__(self):
        return ' + '.join([str(x) for x in self.redused_items]) + ' = 0'

    def reduce(self):
        return self.items

    def grouping_by_power(self, items):
        pass
