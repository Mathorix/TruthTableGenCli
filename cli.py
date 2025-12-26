import sys
from parser import Parser
from truth_table import generate

def format_bool(val):
    return "T" if val else "F"

def run_table(expression):
    try:
        parser = Parser(expression)
        ast = parser.parse()
        table_gen = generate(ast)

        header = next(table_gen)
        col_widths = [max(len(h), 5) for h in header]
        
        row_fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)
        print("\n" + row_fmt.format(*header))
        print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))

        for row in table_gen:
            fmt_row = [format_bool(x) for x in row]
            print(row_fmt.format(*fmt_row))
        print() # Newline

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

def main():
    print("Logic Truth Table Generator (Ctrl+C to exit)")
    while True:
        try:
            expr = input("Expression > ").strip()
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