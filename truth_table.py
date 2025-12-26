import itertools
from nodes import AST, BinaryOp, UnaryOp, Var

def get_vars(node: AST) -> set:
    if isinstance(node, Var):
        return {node.token}
    elif isinstance(node, UnaryOp):
        return get_vars(node.expr)
    elif isinstance(node, BinaryOp):
        return get_vars(node.left) | get_vars(node.right)
    return set()

def evaluate(node: AST, context: dict) -> bool:
    if isinstance(node, Var):
        return context[node.token]
    elif isinstance(node, UnaryOp):
        val = evaluate(node.expr, context)
        return not val if node.op == '~' else val
    elif isinstance(node, BinaryOp):
        l = evaluate(node.left, context)
        r = evaluate(node.right, context)
        if node.op == '&': return l and r
        if node.op == '|': return l or r
        if node.op == '->': return (not l) or r
        if node.op == '<->': return l == r
    raise ValueError(f"Unknown node {node}")

def generate(ast: AST):
    variables = sorted(list(get_vars(ast)))
    combinations = list(itertools.product([True, False], repeat=len(variables)))
    
    yield variables + ["Result"]
    
    for combo in combinations:
        context = dict(zip(variables, combo))
        result = evaluate(ast, context)
        yield list(combo) + [result]