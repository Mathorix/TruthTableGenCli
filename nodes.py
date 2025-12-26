from dataclasses import dataclass

@dataclass
class AST:
    pass

@dataclass
class Var(AST):
    token: str

@dataclass
class UnaryOp(AST):
    op: str
    expr: AST

@dataclass
class BinaryOp(AST):
    left: AST
    op: str
    right: AST

