from sys import argv
from srcs.basic_prover import BasicProver
from srcs.tokenizator import Tokenizator
from srcs.groups_maker import GroupsMaker


if __name__ == '__main__':
    if len(argv) != 2:
        print('Incorrect input. Usage: ./computor "{your expression}"')
        exit(1)
    source_string = argv[1]
    BasicProver(source_string).go()
    tokens_list = Tokenizator(source_string).get_list()
    #print(tokens_list)
    expression = GroupsMaker(tokens_list).get_pieces()
    print(f'Reduced form: {expression}')
