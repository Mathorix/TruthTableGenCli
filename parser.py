from typing import Tuple
from nodes import AST, BinaryOp, UnaryOp, Var, Quantifier, Argument
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
        # Parse the left side (the premises)
        left = self.iff()
        
        # Check if we have a turnstile
        if self.peek() == 'TURNSTILE':
            self.consume('TURNSTILE')
            # Parse the right side (the conclusion)
            right = self.iff()
            return Argument(premise=left, conclusion=right)
        
        return left

    # --- Precedence Levels (Lowest to Highest) ---

    def quantifier(self) -> AST:
        if self.peek() in ('FORALL', 'EXISTS'):
            quant_type = self.consume()[1]
            var_name = self.consume('VAR')[1]
            body = self.quantifier() 
            return Quantifier(quant=quant_type, var=var_name, expr=body)
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
            # Reset to lowest precedence (quantifier) inside parens
            node = self.quantifier() 
            self.consume('RPAREN')
            return node
        elif token_type in ('FORALL', 'EXISTS'):
            # Allow jumping back to quantifier level if needed (e.g. ~(forall x P))
            return self.quantifier()
            
        raise SyntaxError(f"Unexpected token: {token_type}")