# Logic Engine Documentation

This tool generates truth tables and verifies logical arguments using a recursive descent parser and a truth-functional evaluator.

## Installation

Ensure all files (`cli.py`, `lexer.py`, `parser.py`, `nodes.py`, `truth_table.py`) are in the same directory. Run the program via:

```bash
python cli.py

```

## Supported Operators

| Logic Gate | Syntax |
| --- | --- |
| Negation (NOT) | `~` |
| Conjunction (AND) | `&` |
| Disjunction (OR) | ` |
| Conditional (IF/THEN) | `->` |
| Biconditional (IFF) | `<->` |
| Universal Quantifier | `forall x` |
| Existential Quantifier | `exists x` |
| Argument Turnstile | ` |

## Usage Examples

### Truth Table Generation

Enter any logical expression to see its full truth table.

```text
Logic > (A & B) -> C

```

### Validity Testing

Use the turnstile `|-` to separate a premise from a conclusion. The engine identifies an argument as **INVALID** if there is any case where the premise is True but the conclusion is False.

```text
Logic > P -> Q |- ~P
>> STATUS: INVALID ARGUMENT (Found 1 counter-examples)

```

## Logic Precedence

1. Parentheses `()`
2. Quantifiers `forall`, `exists`
3. Negation `~`
4. Conjunction `&`
5. Disjunction `|`
6. Implications `->`, `<->`

## Technical Overview

* **lexer.py**: Tokenizes strings using regex named groups.
* **parser.py**: Converts tokens into an Abstract Syntax Tree (AST) using recursive descent.
* **truth_table.py**: Iterates through  combinations of truth values to evaluate the AST.
* **cli.py**: Provides the interactive loop and table formatting.
