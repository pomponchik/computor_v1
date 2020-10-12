from srcs.tokens.abstract_token import AbstractToken
from srcs.utils.error import error
from srcs.tokens.unknown_variable import UnknownVariable


class Letter(AbstractToken):
    def prove_of_piece(self):
        if not ('^' in self.piece_of_string):
            raise ValueError(self.piece_of_string)
            error(f'the token "{self.piece_of_string}" most be contained a sign "^"')
        splitted_piece = self.piece_of_string.split('^')
        if '' in splitted_piece:
            error(f'token "{self.piece_of_string}" is not completed')
        if len(splitted_piece) != 2:
            error(f'very many symbols "^" in the token "{self.piece_of_string}"')
        if not splitted_piece[0].isalpha():
            error(f'the token "{self.piece_of_string}" most be contained a letter of the variable on the second position')
        if not splitted_piece[1].isdigit():
            error(f'the token "{self.piece_of_string}" most be contained a integer number on the second position')
        if int(splitted_piece[1]) > 2 or int(splitted_piece[1]) < 0:
            error(f'the power "{splitted_piece[1]}" of the variable "{splitted_piece[0]}" in the token "{self.piece_of_string}" is too large')

    def get_content(self):
        splitted_piece = self.piece_of_string.split('^')
        letter = splitted_piece[0]
        UnknownVariable(letter)
        return int(splitted_piece[1])

    def __mul__(self, other):
        first_content = self.content
        second_content = other.content
        new_content = first_content + second_content
        return self.__class__(f'{UnknownVariable().letter}^{new_content}')
