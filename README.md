# Truth Table Generator by Mathorix

A lightweight CLI tool for formal logic. It parses logical expressions and generates complete truth tables using a custom lexer, parser, and Abstract Syntax Tree (AST).

## Features

* **Interactive CLI**: Input expressions directly into the prompt.
* **Recursive Descent Parser**: Handles complex operator precedence and nested parentheses.
* **Custom AST**: Evaluates logic through tree traversal.
* **Full Operator Support**:
* `~` (NOT)
* `&` (AND)
* `|` (OR)
* `->` (IMPLIES)
* `<->` (IFF)



## Installation

Ensure you have Python 3.7+ installed. Clone the repository and navigate to the directory:

```bash
git clone https://github.com/mathorix/TruthTableGen.git
cd TruthTableGen

```

## Usage

Run the tool using the following command:

```bash
python cli.py

```

### Example

```text
Expression > A & (B | ~C) -> D

A     | B     | C     | D     | Result
--------------------------------------
T     | T     | T     | T     | T    
T     | T     | T     | F     | F    
T     | T     | F     | T     | T    
...

```

## Project Structure

* `nodes.py`: Defines the data structures for the expression tree (AST).
* `lexer.py`: Tokenizes the raw input string using regular expressions.
* `parser.py`: Converts tokens into an AST based on formal grammar rules.
* `truth_table.py`: Generates variable combinations and evaluates the AST.
* `cli.py`: The entry point for the interactive user interface.

## Logical Precedence

The parser evaluates expressions in the following order:

1. Parentheses `()`
2. Negation `~`
3. Conjunction `&`
4. Disjunction `|`
5. Implication `->`
6. Equivalence `<->`

---
