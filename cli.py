import sys
from parser import Parser
from truth_table import generate, evaluate
from nodes import Argument

def format_bool(val):
    return "T" if val else "F"

def run_table(expression):
    try:
        parser = Parser(expression)
        ast = parser.parse()
        
        # Determine mode
        is_argument = isinstance(ast, Argument)
        
        # Generate contexts
        vars_gen = generate(ast)
        variables, combinations = next(vars_gen)

        # Prepare headers
        if is_argument:
            header = variables + ["Premise", "Conclusion"]
        else:
            header = variables + ["Result"]

        col_widths = [max(len(h), 5) for h in header]
        row_fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)

        print("\n" + row_fmt.format(*header))
        print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))

        valid_argument = True
        counter_examples = 0

        for combo in combinations:
            context = dict(zip(variables, combo))
            
            if is_argument:
                prem_val = evaluate(ast.premise, context)
                conc_val = evaluate(ast.conclusion, context)
                
                row_vals = list(combo) + [prem_val, conc_val]
                
                # Check Validity: Invalid if Premise is True AND Conclusion is False
                if prem_val and not conc_val:
                    valid_argument = False
                    counter_examples += 1
            else:
                res = evaluate(ast, context)
                row_vals = list(combo) + [res]

            print(row_fmt.format(*[format_bool(x) for x in row_vals]))

        print()
        if is_argument:
            if valid_argument:
                print(">> STATUS: VALID ARGUMENT (Conclusion follows from Premises)")
            else:
                print(f">> STATUS: INVALID ARGUMENT (Found {counter_examples} counter-examples)")
        # If not argument, we print nothing extra, as requested.

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

def main():
    print("Logic Engine")
    print("1. Truth Table:  enter expression (e.g. 'A & B')")
    print("2. Validity:     enter argument   (e.g. 'A & B |- A')")
    
    while True:
        try:
            expr = input("Logic > ").strip()
            if not expr: continue
            if expr.lower() in ['exit', 'quit']: break
            run_table(expr)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except EOFError:
            break

if __name__ == "__main__":
    main()