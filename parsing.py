class PrimaryExpression:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Primary({self.value})"

class BinaryExpression:
    def __init__(self, left=None, op=None, right=None):
        self.left  = left
        self.op    = op
        self.right = right

    def __repr__(self):
        return f"Binary({self.left}, {self.op}, {self.right})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index  = 0

    def end(self):
        if self.index < len(self.tokens):
            return False
        return True

    def token(self):
        return self.tokens[self.index]

    def move(self, value):
        self.index += value

    def next(self):
        if not self.end():
            token = self.token()
            self.move(1)
            return token
        else:
            return None

    def peek(self):
        peek_index = self.index + 1
        if peek_index < len(self.tokens):
            return self.tokens[peek_index]
        else:
            return None

    def parse_binary_expression(self):
        expr = BinaryExpression(self.next(), self.next(), self.next())
        while self.peek() != None:
            op = self.next()
            right = self.next()
            expr = BinaryExpression(expr, op, right)
        return expr

    def parse_expression(self):
        return self.parse_binary_expression()
