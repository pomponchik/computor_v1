from srcs.tokens.sign import Sign
from srcs.tokens.group import Group
from srcs.tokens.letter import Letter
from srcs.tokens.number import Number
from srcs.tokens.unknown_variable import UnknownVariable


class Expression:
    def __init__(self, items):
        self.items = items
        self.redused_items = self.reduce()
        self.degree = self.get_degree()
        self.full_form, self.full_form_dict = self.get_full_form()

    def __repr__(self):
        return ' + '.join([str(x) for x in self.redused_items]) + ' = 0'

    def __getitem__(self, key):
        if type(key) is int:
            if key in self.full_form_dict:
                return self.full_form_dict[key][0]
            elif key > 0:
                return Group(Sign('+'), [Letter(f'{UnknownVariable().letter}^{key}'), Number('0')])
            raise KeyError(f'Expression "{self}" has no element with the degree "{key}"')
        elif type(key) is str:
            keys = {
                'a': 2,
                'b': 1,
                'c': 0,
            }
            if key not in keys:
                raise KeyError(f'The key "{key}" most be an int of a str of kind: "a", "b", "c" (from full form of the expression "ax^2 + bx + c")')
            index = keys[key]
            item = self[index]
            number = item.number.content
            return number

    def solve(self):
        if self.degree > 2:
            return "The polynomial degree is strictly greater than 2, I can't solve."
        if self.degree == 0:
            return 'The solution is:\n[-∞:+∞]'
        discriminant = self.discriminant()
        if self['a'] == 0:
            return 'Calculating the discriminant requires division by zero, and the equation has no solution.'
        if discriminant < 0:
            return 'The discriminant is less than zero, and the equation has no solutions.'
        elif discriminant == 0:
            result = -1 * (self['b'] / (2 * self['a']))
            return f'The solution is:\n{result}'
        result_1 = (-1 * self['b'] + self.root(discriminant)) / (2 * self['a'])
        result_2 = (-1 * self['b'] - self.root(discriminant)) / (2 * self['a'])
        return f'Discriminant is strictly positive, the two solutions are:\n{result_1}\n{result_2}'

    def discriminant(self):
        result = self['b'] * self['b'] - 4 * self['a'] * self['c']
        return result

    @staticmethod
    def root(number, precision_factor=0.0001):
        def square(n):
            return n * n
        def good_enough(guess, number):
            return abs(square(guess) - number) < precision_factor
        def improve(guess, number):
            return ((number/guess) + guess) / 2
        def sqrt_iter(guess, number):
            return guess if good_enough(guess, number) else sqrt_iter(improve(guess, number), number)
        return sqrt_iter(1.0, number)

    def get_full_form(self):
        if self.degree == 0:
            return self.redused_items, self.grouping_by_power(self.redused_items)
        groups = self.grouping_by_power(self.redused_items)
        sign = Sign('+')
        for number in range(self.degree):
            if number not in groups:
                number_item = Number('0')
                new_group = Group(sign, [Letter(f'{UnknownVariable().letter}^{number}'), number_item])
                groups[number] = [new_group]
        return self.groups_merger(groups), groups

    def get_degree(self):
        result = 0
        for item in self.redused_items:
            content = item.letter.content
            if content > result:
                result = content
        return result

    def reduce(self):
        groups_of_groups = self.grouping_by_power(self.items)
        result = self.groups_merger(groups_of_groups)
        return result

    def groups_merger(self, groups_dict):
        result = []
        sign = Sign('+')
        for key, value in groups_dict.items():
            number = Number('0')
            for item in value:
                number += item.number
            new_group = Group(sign, [Letter(f'{UnknownVariable().letter}^{key}'), number])
            result.append(new_group)
        result.sort(key=lambda x: x.letter.content)
        return result

    def grouping_by_power(self, items):
        result = {}
        for item in items:
            content = item.letter.content
            if content in result:
                result[content].append(item)
            else:
                result[content] = [item]
        return result
