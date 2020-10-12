from srcs.tokens.number import Number
from srcs.tokens.letter import Letter
from srcs.tokens.sign import Sign
from srcs.tokens.unknown_variable import UnknownVariable


class Group:
    def __init__(self, sign, tokens):
        self.sign = sign
        self.tokens = tokens
        self.number = self.type_items(Number, '1')
        self.letter = self.type_items(Letter, f'{UnknownVariable().letter}^0')

    def type_items(self, target_class, init):
        items = [x for x in self.tokens if x.__class__ is target_class]
        result = target_class(init)
        for x in items:
            result *= x
        return result

    def replase_sign(self):
        if self.sign == Sign('-'):
            self.sign = Sign('+')
        else:
            self.sign = Sign('-')
        self.number *= Number('-1')
        return self

    def __str__(self):
        result = f'{self.number.content} * {UnknownVariable().letter}^{self.letter.content}'
        return result

    def __repr__(self):
        result = f'{self.number.content} * {UnknownVariable().letter}^{self.letter.content}'
        return result
