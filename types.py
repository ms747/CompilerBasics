class Base:
    def __init__(self, type, value):
        self.type  = type
        self.value = value

    def __repr__(self):
        if self.value == None:
            return f"{self.type}()"
        return f"{self.type}({self.value})"

    def __eq__(self, other):
        if other == None:
            return False
        return self.type == other.type and self.value == other.value

class Number(Base):
    def __init__(self, value):
        super().__init__("Number", value)

class Undefined(Base):
    def __init__(self, value=None):
        super().__init__("Undefined", value)

class Eof(Base):
    def __init__(self, value=None):
        super().__init__("Eof", value)

class Symbol(Base):
    def __init__(self, value):
        super().__init__("Symbol", value)

class OpenParen(Base):
    def __init__(self, value=None):
        super().__init__("OpenParen", value)

class CloseParen(Base):
    def __init__(self, value=None):
        super().__init__("CloseParen", value)

