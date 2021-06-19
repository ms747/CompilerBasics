from types import *

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
                return Plus()
            elif self.token() == '-':
                self.move(1)
                return Dash()
            elif self.token() == '*':
                self.move(1)
                return Asterisk()
            elif self.token() == '/':
                self.move(1)
                return Slash()
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

tokenizer = Tokenizer("1024+2")

while True:
    token = tokenizer.next()
    if token != Eof():
        print(token)
    else:
        break
