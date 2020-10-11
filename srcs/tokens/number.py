from srcs.tokens.abstract_token import AbstractToken
from srcs.utils.error import error
from srcs.utils.is_number import is_number


class Number(AbstractToken):
    def prove_of_piece(self):
        if is_number(self.piece_of_string):
            return
        if not '.' in self.piece_of_string:
            error(f'token "{self.piece_of_string}" is not valid')
        splitted_piece = self.piece_of_string.split('.')
        if '' in splitted_piece:
            error(f'token "{self.piece_of_string}" is not completed')
        count_of_dots = 0
        count_of_numbers = 0
        for sign in self.piece_of_string:
            if sign == '.':
                count_of_dots += 1
            elif sign.isdigit():
                count_of_numbers += 1
            else:
                error(f'unidentified letter "{sign}" in the token "{self.piece_of_string}"')
        if count_of_dots != 1:
            error(f'very many dots in the token "{self.piece_of_string}"')

    def get_content(self):
        if '.' in self.piece_of_string:
            return float(self.piece_of_string)
        else:
            int(self.piece_of_string)
