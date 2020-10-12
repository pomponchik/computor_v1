from srcs.tokens.sign import Sign
from srcs.tokens.group import Group
from srcs.expression import Expression


class GroupsMaker:
    def __init__(self, tokens_list):
        self.tokens = tokens_list

    def cut_by_token(self, dilimiters_list, tokens):
        result = []
        item = []
        sign = Sign('+')
        for index, token in enumerate(tokens):
            if token in dilimiters_list:
                result.append({'sign': sign, 'tokens': item})
                item = []
                sign = token
            else:
                item.append(token)
        if item:
            result.append({'sign': sign, 'tokens': item})
        return result

    def get_pieces(self):
        halfs = self.cut_by_token([Sign('=')], self.tokens)
        #print(halfs)
        first_half = self.cut_by_token([Sign('-'), Sign('+')], halfs[0]['tokens'])
        second_half = self.cut_by_token([Sign('-'), Sign('+')], halfs[1]['tokens'])
        first_half = [Group(**x) for x in first_half]
        second_half = [Group(**x) for x in second_half]
        expression = first_half
        for group in second_half:
            expression.append(group.replase_sign())
        expression = Expression(expression)
        return expression
