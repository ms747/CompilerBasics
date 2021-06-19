class Base:
    def __init__(self, type, value):
        self.type  = type
        self.value = value

    def __repr__(self):
        if self.value == None:
            return f"{self.type}()"
        return f"{self.type}({self.value})"

    def __eq__(self, other):
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

class Plus(Base):
    def __init__(self, value=None):
        super().__init__("Plus", value)

class Dash(Base):
    def __init__(self, value=None):
        super().__init__("Dash", value)

class Asterisk(Base):
    def __init__(self, value=None):
        super().__init__("Asterisk", value)

class Slash(Base):
    def __init__(self, value=None):
        super().__init__("Slash", value)

class OpenParen(Base):
    def __init__(self, value=None):
        super().__init__("OpenParen", value)

class CloseParen(Base):
    def __init__(self, value=None):
        super().__init__("CloseParen", value)

