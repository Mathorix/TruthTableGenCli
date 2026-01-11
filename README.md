# Logic Engine CLI

A small Python command-line tool for working with propositional and basic first-order logic. It can generate truth tables for logical expressions and check the validity of arguments using truth-table semantics.

## Requirements
- Python 3.8 or newer
- No external dependencies

## How to Run
From the project directory:
python cli.py

You will enter an interactive prompt. Type a logical expression or an argument and press Enter. Type `exit` or `quit` to leave.

## Input Modes
Truth Table mode: enter a logical expression  
Example: A & B

Validity mode: enter an argument using a turnstile  
Example: A & B |- A

## Supported Syntax
Variables: identifiers starting with a letter (A, B, P, Q1, foo)

Operators:
~    NOT  
&    AND  
|    OR  
->   IMPLIES  
<->  IFF  

Parentheses are supported:
(A & B) -> C

Quantifiers:
forall x
exists x

Examples:
forall x (P -> Q)
exists x (P & Q)

## Output
- Variables are automatically detected and listed as table columns
- Truth values are displayed as T and F
- For arguments, the table shows Premise and Conclusion
- An argument is invalid if any row has Premise = T and Conclusion = F
- If no such row exists, the argument is valid

## Notes
- Free variables appear in the truth table
- Quantifiers evaluate by assigning the bound variable both True and False
- Syntax and lexer errors are printed without crashing the program

## Example Session
Logic > A & B  
Logic > A & B |- B  
Logic > ~(A | B) -> C  
Logic > exit

## License
Provided as-is for educational and experimental use.
