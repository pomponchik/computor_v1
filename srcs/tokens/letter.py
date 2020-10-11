from srcs.tokens.abstract_token import AbstractToken
from srcs.utils.error import error


class Letter(AbstractToken):
    def prove_of_piece(self):
        if not ('^' in self.piece_of_string):
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

    def get_content(self):
        splitted_piece = self.piece_of_string.split('^')
        return splitted_piece[0], int(splitted_piece[1])
