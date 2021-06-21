from types import *
from parsing import *

class Tokenizer:
    def __init__(self, buf):
        self.buf   = buf
        self.index = 0

    def token(self):
        return self.buf[self.index]

    def move(self, value):
        self.index += value

    def skip_whitespaces(self):
        while self.index < len(self.buf) and self.token().isspace():
            self.move(1)

    def next(self):
        self.skip_whitespaces()

        if self.index < len(self.buf):
            if self.token() == '+':
                self.move(1)
                return Symbol('+')
            elif self.token() == '-':
                self.move(1)
                return Symbol('-')
            elif self.token() == '*':
                self.move(1)
                return Symbol('*')
            elif self.token() == '/':
                self.move(1)
                return Symbol('/')
            elif self.token() == '(':
                self.move(1)
                return OpenParen()
            elif self.token() == ')':
                self.move(1)
                return CloseParen()
            else:
                if self.token().isnumeric():
                    number = int(self.token())
                    self.move(1)
                    while self.index < len(self.buf) and self.token().isnumeric():
                        number = number * 10 + int(self.token())
                        self.move(1)
                    return Number(number)
                else:
                    char = self.token()
                    self.move(1)
                    return Undefined(char)
        else:
            return Eof()

tokenizer = Tokenizer("1 + 2 + 3 + 4 + 5")
tokens = []

while True:
    token = tokenizer.next()
    if token != Eof():
        tokens.append(token)
    else:
        break

parser = Parser(tokens)

expression = parser.parse_expression()
print(expression)
