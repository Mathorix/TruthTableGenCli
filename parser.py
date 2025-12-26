from typing import Tuple
from nodes import AST, BinaryOp, UnaryOp, Var # Updated import
from lexer import lex

class Parser:
    def __init__(self, text: str):
        self.tokens = list(lex(text))
        self.pos = 0

    def consume(self, expected_type: str = None) -> Tuple[str, str]:
        if self.pos >= len(self.tokens):
            raise SyntaxError("Unexpected end of input")
        current_type, current_val = self.tokens[self.pos]
        if expected_type and current_type != expected_type:
            raise SyntaxError(f"Expected {expected_type}, got {current_type}")
        self.pos += 1
        return current_type, current_val

    def peek(self) -> str:
        if self.pos >= len(self.tokens):
            return 'EOF'
        return self.tokens[self.pos][0]

    def parse(self) -> AST:
        return self.iff()

    def iff(self) -> AST:
        node = self.implies()
        while self.peek() == 'IFF':
            op = self.consume()[1]
            node = BinaryOp(left=node, op=op, right=self.implies())
        return node

    def implies(self) -> AST:
        node = self.expr()
        while self.peek() == 'IMPLIES':
            op = self.consume()[1]
            node = BinaryOp(left=node, op=op, right=self.expr())
        return node

    def expr(self) -> AST:
        node = self.term()
        while self.peek() == 'OR':
            op = self.consume()[1]
            node = BinaryOp(left=node, op=op, right=self.term())
        return node

    def term(self) -> AST:
        node = self.factor()
        while self.peek() == 'AND':
            op = self.consume()[1]
            node = BinaryOp(left=node, op=op, right=self.factor())
        return node

    def factor(self) -> AST:
        token_type = self.peek()
        if token_type == 'NOT':
            op = self.consume()[1]
            return UnaryOp(op=op, expr=self.factor())
        elif token_type == 'VAR':
            return Var(token=self.consume()[1])
        elif token_type == 'LPAREN':
            self.consume('LPAREN')
            node = self.iff()
            self.consume('RPAREN')
            return node
        raise SyntaxError(f"Unexpected token: {token_type}")