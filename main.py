from types import *
from parsing import *
from tokenizer import *

tokenizer = Tokenizer("9 * 2 / 2")
tokens = []

while True:
    token = tokenizer.next()
    if token != Eof():
        tokens.append(token)
    else:
        break

parser = Parser(tokens)

expression = parser.parse_expression()
print(expression.execute())
