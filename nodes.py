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

@dataclass
class Quantifier(AST):
    quant: str
    var: str
    expr: AST

@dataclass
class Argument(AST):
    premise: AST
    conclusion: AST