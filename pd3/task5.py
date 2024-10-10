import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.strip().split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return start

BNF = '''
E = L | E  &  L | E + L | E
L = x | y | ( E ) | ~ L 
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
