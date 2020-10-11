class AbstractToken:
    def __init__(self, piece_of_string):
        self.piece_of_string = piece_of_string
        self.prove_of_piece()
        self.content = self.get_content()

    def __repr__(self):
        name = self.__class__.__name__
        base = f'{name}("{self.piece_of_string}")'
        return base

    def prove_of_piece(self):
        raise NotImplementedError()

    def get_content(self):
        raise NotImplementedError()
