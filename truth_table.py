import itertools
from nodes import AST, BinaryOp, UnaryOp, Var, Quantifier, Argument

def get_vars(node: AST) -> set:
    if isinstance(node, Var):
        return {node.token}
    elif isinstance(node, UnaryOp):
        return get_vars(node.expr)
    elif isinstance(node, BinaryOp):
        return get_vars(node.left) | get_vars(node.right)
    elif isinstance(node, Quantifier):
        return get_vars(node.expr) - {node.var}
    elif isinstance(node, Argument):
        return get_vars(node.premise) | get_vars(node.conclusion)
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
    elif isinstance(node, Quantifier):
        ctx_true = context.copy(); ctx_true[node.var] = True
        ctx_false = context.copy(); ctx_false[node.var] = False
        t = evaluate(node.expr, ctx_true)
        f = evaluate(node.expr, ctx_false)
        return (t and f) if node.quant == 'forall' else (t or f)
    raise ValueError(f"Unknown node {node}")

def generate(ast: AST):
    # This remains the same generic generator
    variables = sorted(list(get_vars(ast)))
    combinations = list(itertools.product([True, False], repeat=len(variables)))
    
    yield variables, combinations