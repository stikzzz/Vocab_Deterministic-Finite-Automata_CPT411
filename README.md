# Deterministic Finite Automata (DFA) Vocabulary Extractor

This Python program implements an object-oriented Deterministic Finite Automaton (DFA) to scan through text files and identify, validate, and extract specific target keywords. 

The state machine reads a source text, normalizes the characters, and walks them through a defined state transition graph. Accepted words are highlighted in the final output, and a detailed summary table is generated with occurrence statistics.

## How to Run

1. Ensure you have Python installed on your system.
2. Clone or download this repository.
3. Open a terminal or command prompt in the project directory.
4. Run the script:
   ```bash
   python program.py
   ```

## ⚠️ Changing the Input File

To change the text file that the program reads and processes, you must manually edit the source code.

**Open `program.py` and modify Line 4:**
```python
filename = "text4.txt" # <------------- change this for any input file text
```
Simply replace `"text4.txt"` with the name or path of your desired input file (e.g., `"text3.txt"`).

## Features

- **Object-Oriented State Machine:** States and transitions are managed through a clean, dynamic `State` class, eliminating complex, hardcoded `if/else` branching.
- **Robust Text Normalization:** Words are automatically converted to lowercase and stripped of punctuation before the DFA processes them.
- **Interactive Debugging:** The program can walk you through the state machine character-by-character. To enable or disable this, toggle the `DEBUG` variable on Line 1 of `program.py`:
  - `DEBUG = True`: Pauses and prompts for the `Enter` key after every single state transition. This is perfect for verifying the automaton's exact pathways and identifying Trap States.
  - `DEBUG = False`: Skips the interactive prompts, instantly processes the entire document, and jumps straight to the final output.
- **Visual Highlighting:** Accepted vocabulary words are printed back in bold using terminal ANSI codes, so you can easily spot them in their original context.
- **Summary Statistics:** Generates a clean table at the end of the script showing each accepted word, how many times it occurred, and its exact starting character positions in the source text.
