from sys import argv
from srcs.basic_prover import BasicProver
from srcs.tokenizator import Tokenizator
from srcs.normalizator import Normalizator
from srcs.groups_maker import GroupsMaker


if __name__ == '__main__':
    if len(argv) != 2:
        print('Incorrect input. Usage: python3 computor.py "{your expression}"')
        exit(1)
    source_string = argv[1]
    source_string = Normalizator(source_string).get_norm_version()
    BasicProver(source_string).go()
    tokens_list = Tokenizator(source_string).get_list()
    expression = GroupsMaker(tokens_list).get_pieces()
    print(f'Reduced form: {expression}')
    print(f'Polynomial degree: {expression.degree}')
    print(expression.solve())
